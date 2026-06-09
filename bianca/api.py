from bianca.bootstrap import *
from bianca.llama_router import *
from bianca.registry import *
from bianca.log import *

from fastapi import *
from pathlib import Path
import uvicorn
import hashlib

__all__ = ["api", "serve"]

mpr = ModelProfileRegistry()
llama_router = Router()

api = FastAPI(
    title="Ollama Compatible API",
    description="A server compatible with Ollama and OpenAI APIs using LlamaRouter.",
    version="v0.1.0",
    lifespan=logging_uvicorn_lifespan)


@api.middleware("http")
async def track_requests(request: Request, call_next):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H:%M:%S.%f")[:-5]

    body = await request.body()
    h = hashlib.sha256(body).hexdigest()[:8]
    filename_base = f"{timestamp}-{h}"

    response = await call_next(request)

    status_code = response.status_code
    endpoint = request.url.path.strip("/") or "root"
    directory = PROJECT_DIR / "store" / endpoint / str(status_code)
    directory.mkdir(parents=True, exist_ok=True)

    req_data = {
        "timestamp": timestamp,
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "body": json.loads(body.decode())
    }

    with open(directory / f"{filename_base}-request.json", "w") as f:
        json.dump(req_data, f, indent=2)

    if hasattr(response, "body_iterator"):
        original_iterator = response.body_iterator

        async def body_wrapper():
            full_response = []
            try:
                async for chunk in original_iterator:
                    full_response.append(chunk)
                    yield chunk
            finally:
                with open(directory / f"{filename_base}-response.json", "w") as f:
                    json.dump({
                        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f")[:-5],
                        "status_code": status_code,
                        "headers": dict(response.headers),
                        "body": json.loads(b"".join(full_response).decode())
                    }, f, indent=2)

        response.body_iterator = body_wrapper()
    else:
        resp_content = response.body
        resp_data = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f")[:-5],
            "status_code": status_code,
            "headers": dict(response.headers),
            "body": json.loads(resp_content.decode())
        }

        with open(directory / f"{filename_base}-response.json", "w") as f:
            json.dump(resp_data, f, indent=2)

    return response


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:24]}"


def _fork_config_for_request(base_config: ModelProfile, options: dict,
                             system_prompt: str | None = None) -> ModelProfile:
    """Forks a configuration to apply end-user request overrides."""
    req_sampler_kwargs = base_config.sampler_kwargs.copy()

    for key in ["temperature", "top_k", "top_p", "min_p", "seed"]:
        if key in options and options[key] is not None:
            req_sampler_kwargs[key] = options[key]

    if system_prompt is None:
        system_prompt = options.get("system_prompt") or options.get("system")

    fallback = None
    if base_config.fallback is not None:
        fallback = _fork_config_for_request(base_config.fallback, options, system_prompt)

    return base_config.fork(
        model_path=base_config.model_path.decode(),
        sampler_kwargs=req_sampler_kwargs,
        system_prompt=system_prompt,
        fallback=fallback
    )


@api.get("/")
@api.head("/")
async def root():
    return {"status": "Bianca is running"}


@api.post("/api/generate")
async def generate(request: Request):
    body = await request.json()
    model_name = body.get("model")
    prompt = body.get("prompt")
    stream = body.get("stream", True)
    options = body.get("options", {})
    system_prompt = body.get("system")

    if model_name not in mpr:
        raise HTTPException(status_code=404, detail=f"Model '{model_name}' not found")

    forked_config = _fork_config_for_request(mpr[model_name], options, system_prompt)
    max_tokens = options.get("num_predict", 512)

    if stream:
        async def stream_generator():
            for piece in llama_router.stream_completion(forked_config, prompt, max_tokens=max_tokens):
                payload = {
                    "model": model_name,
                    "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "response": piece,
                    "done": False
                }
                yield json.dumps(payload) + "\n"

            yield json.dumps({
                "model": model_name,
                "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "response": "",
                "done": True
            }) + "\n"

        return responses.StreamingResponse(stream_generator(), media_type="application/x-ndjson")
    else:
        response_text = llama_router.completion(forked_config, prompt, max_tokens=max_tokens)
        return {
            "model": model_name,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "response": response_text,
            "done": True
        }


@api.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    model_name = body.get("model")
    messages = body.get("messages", [])
    stream = body.get("stream", True)
    options = body.get("options", {})
    system_prompt = body.get("system")

    if model_name not in mpr:
        raise HTTPException(status_code=404, detail=f"Model '{model_name}' not found")

    base_config = mpr[model_name]
    forked_config = _fork_config_for_request(base_config, options, system_prompt)
    max_tokens = options.get("num_predict", 512)

    if stream:
        async def stream_generator():
            for piece in llama_router.stream_chat_completion(forked_config, messages, max_tokens=max_tokens):
                payload = {
                    "model": model_name,
                    "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "message": {
                        "role": "assistant",
                        "content": piece
                    },
                    "done": False
                }
                yield json.dumps(payload) + "\n"

            yield json.dumps({
                "model": model_name,
                "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "done": True
            }) + "\n"

        return responses.StreamingResponse(stream_generator(), media_type="application/x-ndjson")
    else:
        response_text = llama_router.chat_completion(forked_config, messages, max_tokens=max_tokens)
        return {
            "model": model_name,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "message": {"role": "assistant", "content": response_text},
            "done": True,
        }


@api.get("/api/tags")
async def list_local_models(request: Request):
    models = []
    for name, config in mpr.items():
        path = Path(config.model_path.decode())
        is_qwen = "qwen" in path.name.lower()
        models.append({
            "name": name,
            "modified_at": datetime.datetime.fromtimestamp(path.stat().st_mtime,
                                                           datetime.timezone.utc).isoformat() if path.exists() else datetime.datetime.now(
                datetime.timezone.utc).isoformat(),
            "size": path.stat().st_size if path.exists() else 0,
            "digest": "sha256:0000000000000000000000000000000000000000000000000000000000000000",
            "details": {
                "format": "gguf",
                "family": "llama",
                "families": ["llama"],
                "parameter_size": "27B" if is_qwen else "31B",
                "quantization_level": "Q5_K_M"
            }
        })
    return {"models": models}


@api.get("/api/version")
async def version(request: Request):
    return {"version": "0.1.0"}


@api.post("/v1/chat/completions")
async def openai_chat_completions(request: Request):
    body = await request.json()
    model_name = body.get("model")
    messages = body.get("messages", [])
    stream = body.get("stream", False)

    if model_name not in mpr:
        raise HTTPException(404, "Model not found")

    base_config = mpr[model_name]
    forked_config = _fork_config_for_request(base_config, body)
    max_tokens = body.get("max_tokens", 512)

    if stream:
        try:
            gen = llama_router.stream_chat_completion(forked_config, messages, max_tokens=max_tokens)

            # We wrap the generator in a synchronous function so FastAPI runs it in a threadpool
            def stream_generator():
                try:
                    chat_id = _id("chatcmpl")
                    created = int(time.time())
                    for piece in gen:
                        chunk = {
                            "id": chat_id,
                            "object": "chat.completion.chunk",
                            "created": created,
                            "model": model_name,
                            "choices": [{"index": 0, "delta": {"content": piece}, "finish_reason": None}]
                        }
                        yield f"data: {json.dumps(chunk)}\n\n"

                    final_chunk = {
                        "id": chat_id,
                        "object": "chat.completion.chunk",
                        "created": created,
                        "model": model_name,
                        "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]
                    }
                    yield f"data: {json.dumps(final_chunk)}\n\n"
                    yield "data: [DONE]\n\n"
                except Exception as e:
                    yield f"data: {json.dumps({'error': {'message': str(e), 'type': 'invalid_request_error'}})}\n\n"
                    yield "data: [DONE]\n\n"

            return responses.StreamingResponse(stream_generator(), media_type="text/event-stream")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        try:
            response_text = llama_router.chat_completion(forked_config, messages, max_tokens=max_tokens)
            return {
                "id": _id("chatcmpl"),
                "object": "chat.completion",
                "created": int(time.time()),
                "model": model_name,
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant", "content": response_text},
                    "logprobs": None,
                    "finish_reason": "stop"
                }],
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                "system_fingerprint": "fp_bianca",
                "service_tier": "default"
            }
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


@api.post("/v1/completions")
async def openai_completions(request: Request):
    body = await request.json()
    model_name = body.get("model")
    prompt = body.get("prompt")
    stream = body.get("stream", False)

    if model_name not in mpr:
        raise HTTPException(404, "Model not found")

    base_config = mpr[model_name]
    forked_config = _fork_config_for_request(base_config, body)
    max_tokens = body.get("max_tokens", 512)

    if stream:
        try:
            gen = llama_router.stream_completion(forked_config, prompt, max_tokens=max_tokens)

            async def stream_generator():
                compl_id = _id("cmpl")
                created = int(time.time())
                for piece in gen:
                    chunk = {
                        "id": compl_id,
                        "object": "text_completion",
                        "created": created,
                        "model": model_name,
                        "choices": [{"text": piece, "index": 0, "logprobs": None, "finish_reason": None}]
                    }
                    yield f"data: {json.dumps(chunk)}\n\n"

                final_chunk = {
                    "id": compl_id,
                    "object": "text_completion",
                    "created": created,
                    "model": model_name,
                    "choices": [{"text": "", "index": 0, "logprobs": None, "finish_reason": "stop"}]
                }
                yield f"data: {json.dumps(final_chunk)}\n\n"
                yield "data: [DONE]\n\n"

            return responses.StreamingResponse(stream_generator(), media_type="text/event-stream")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        response_text = llama_router.completion(forked_config, prompt, max_tokens=max_tokens)
        return {
            "id": _id("cmpl"),
            "object": "text_completion",
            "created": int(time.time()),
            "model": model_name,
            "choices": [{"text": response_text, "index": 0, "logprobs": None, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            "system_fingerprint": "fp_bianca"
        }


@api.get("/v1/models")
async def list_models():
    data = []
    for name, config in mpr.items():
        path = Path(config.model_path.decode())
        created = int(path.stat().st_mtime) if path.exists() else int(time.time())
        data.append({
            "id": name,
            "object": "model",
            "created": created,
            "owned_by": "bianca"
        })
    return {
        "object": "list",
        "data": data
    }


@api.get("/v1/models/{model}")
async def retrieve_model(model: str):
    if model not in mpr:
        raise HTTPException(status_code=404, detail=f"Model '{model}' not found")

    config = mpr[model]
    path = Path(config.model_path.decode())
    created = int(path.stat().st_mtime) if path.exists() else int(time.time())

    return {
        "id": model,
        "object": "model",
        "created": created,
        "owned_by": "bianca"
    }


@api.post("/api/pull")
@api.post("/api/push")
@api.post("/api/create")
@api.post("/api/copy")
@api.delete("/api/delete")
@api.post("/api/show")
@api.post("/api/embed")
@api.post("/api/embeddings")
@api.post("/v1/embeddings")
@api.post("/v1/responses")
@api.get("/v1/responses/{response_id}")
@api.delete("/v1/responses/{response_id}")
@api.post("/v1/responses/{response_id}/cancel")
@api.get("/v1/responses/{response_id}/input_items")
@api.post("/v1/responses/input_tokens")
@api.post("/v1/responses/compact")
@api.post("/v1/conversations")
@api.get("/v1/conversations/{conversation_id}")
@api.post("/v1/conversations/{conversation_id}")
@api.post("/v1/conversations/{conversation_id}/items")
@api.get("/v1/conversations/{conversation_id}/items")
@api.get("/v1/conversations/{conversation_id}/items/{item_id}")
@api.delete("/v1/conversations/{conversation_id}/items/{item_id}")
@api.delete("/v1/conversations/{conversation_id}")
@api.post("/v1/files")
@api.get("/v1/files")
@api.get("/v1/files/{file_id}")
@api.get("/v1/files/{file_id}/content")
@api.delete("/v1/files/{file_id}")
@api.post("/v1/moderations")
@api.post("/v1/fine_tuning/jobs")
@api.get("/v1/fine_tuning/jobs")
@api.post("/v1/batches")
@api.get("/v1/batches")
@api.post("/v1/uploads")
@api.post("/v1/vector_stores")
@api.post("/v1/audio/speech")
@api.post("/v1/audio/transcriptions")
@api.post("/v1/audio/translations")
async def forbidden():
    raise HTTPException(403, "Forbidden")


@api.post("/restart", status_code=status.HTTP_202_ACCEPTED)
async def restart(background_tasks: BackgroundTasks):
    def _restart():
        time.sleep(1)
        os.execv(sys.executable, sys.orig_argv)

    background_tasks.add_task(_restart)
    return {"status": "accepted", "detail": "Server is restarting."}


@api.post("/reload", status_code=status.HTTP_202_ACCEPTED)
async def reload():
    mpr.reload()
    return {"status": "accepted", "detail": "Server is reloaded."}


def serve(host="0.0.0.0", port=11434):
    try:
        config = mpr["gemma-4-26b-a4b"]
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a short haiku about coding in C++."}
        ]
        print(llama_router.chat_completion(config, messages, 100))
    except Exception as e:
        print(e)

    uvicorn.run(api, host=host, port=port, log_config=None)
