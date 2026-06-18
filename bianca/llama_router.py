from bianca.bootstrap import *
from bianca.llama_wrapper import *

__all__ = [
    "ModelProfile",
    "Backend",
    "Model",
    "Context",
    "SamplerChain",
    "Router",
]

logger = logging.getLogger("c_py")


def tstr(obj) -> str:
    if isinstance(obj, str):
        return "str"
    if isinstance(obj, float):
        return "float"
    if isinstance(obj, bool):
        return "bool"
    if isinstance(obj, int):
        return "int"
    if isinstance(obj, tuple):
        return f"({", ".join([tstr(it) for it in list(obj)])})"
    if isinstance(obj, list):
        return f"[{", ".join([tstr(it) for it in obj])}]"
    if isinstance(obj, dict):
        return f"{{{", ".join([f"{tstr(k)}: {tstr(v)}" for k, v in obj.items()])}}}"
    return f"{type(obj)}"


def sstr(obj) -> str:
    if isinstance(obj, str):
        return f"\"{obj}\""
    if isinstance(obj, tuple):
        return f"({", ".join([sstr(it) for it in list(obj)])})"
    if isinstance(obj, list):
        return f"[{", ".join([sstr(it) for it in obj])}]"
    if isinstance(obj, dict):
        return f"{{{", ".join([f"{sstr(k)}: {sstr(v)}" for k, v in obj.items()])}}}"
    return str(obj)


def mstr(obj) -> str:
    if isinstance(obj, str):
        return obj
    return sstr(obj)


class ModelProfile:
    model_id: int
    model_path: bytes
    model_params: LlamaModelParams
    context_id: int
    context_params: LlamaContextParams
    sampler_chain_id: int
    sampler_chain_params: LlamaSamplerChainParams
    sampler_kwargs: dict
    system_prompt: str | None
    fallback: "ModelProfile | None"

    def __init__(self, model_path: str | bytes,
                 model_params: None | LlamaModelParams = None,
                 model_kwargs: None | dict = None,
                 context_params: None | LlamaContextParams = None,
                 context_kwargs: None | dict = None,
                 sampler_chain_params: None | LlamaSamplerChainParams = None,
                 sampler_chain_kwargs: None | dict = None,
                 sampler_kwargs: None | dict = None,
                 system_prompt: str | None = None,
                 fallback: "ModelProfile | None" = None):
        """collects all configs required to make a chat completion"""

        def _create_params(default_params, kwargs: None | dict):
            if kwargs:
                for k, v in kwargs.items():
                    assert hasattr(default_params, k), f"Parameter {k} not found in struct."
                    setattr(default_params, k, v)
            return default_params

        model_params = model_params or c_llama_model_default_params()
        context_params = context_params or c_llama_context_default_params()
        sampler_chain_params = sampler_chain_params or c_llama_sampler_chain_default_params()

        if isinstance(model_path, str):
            self.model_path: bytes = model_path.encode()
        else:
            self.model_path: bytes = model_path

        self.model_params = _create_params(model_params, model_kwargs)
        self.model_id = abs(hash(self.model_path) ^ hash(bytes(self.model_params))) | 1

        self.context_params = _create_params(context_params, context_kwargs)
        self.context_id = abs(hash(bytes(self.context_params))) | 1

        self.sampler_chain_params = _create_params(sampler_chain_params, sampler_chain_kwargs)
        self.sampler_chain_id = abs(hash(bytes(self.sampler_chain_params))) | 1

        # Store dynamic sampler arguments (top_k, top_p, etc.) separate from the struct parameters
        self.sampler_kwargs = sampler_kwargs or {}
        self.system_prompt = system_prompt
        self.fallback = fallback

    def fork(self, model_path: None | str = None,
             model_kwargs: None | dict = None,
             context_kwargs: None | dict = None,
             sampler_chain_kwargs: None | dict = None,
             sampler_kwargs: None | dict = None,
             system_prompt: str | None = None,
             fallback: "ModelProfile | None" = None):
        """overwrites chosen parameter for a new config"""

        assert isinstance(self.model_path, bytes), f"model_path must be bytes, got {type(self.model_path)}"

        return ModelProfile(
            model_path=model_path.encode() if model_path else self.model_path,
            model_params=self.model_params,
            model_kwargs=model_kwargs,
            context_params=self.context_params,
            context_kwargs=context_kwargs,
            sampler_chain_params=self.sampler_chain_params,
            sampler_chain_kwargs=sampler_chain_kwargs,
            sampler_kwargs=sampler_kwargs or self.sampler_kwargs,
            system_prompt=system_prompt or self.system_prompt,
            fallback=fallback or self.fallback)


# noinspection PyMethodMayBeStatic
class Backend:
    def __init__(self):
        c_llama_backend_init()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        c_llama_backend_free()

    def __del__(self):
        self.close()


class Model:
    model_id: int
    pointer: LlamaModelPointer
    vocab: LlamaVocabPointer
    template: bytes

    def __init__(self, config: ModelProfile):
        self.model_id = config.model_id
        self.pointer = c_llama_model_load_from_file(config.model_path, config.model_params)
        if not self.pointer:
            raise RuntimeError("Failed to load model")
        self.vocab = c_llama_model_get_vocab(self.pointer)
        self.template = c_llama_model_chat_template(self.pointer, None)
        if not self.template:
            raise RuntimeError("Failed to get chat template")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def convert_messages(messages: list[dict[str, bytes]]):
        c_messages = (LlamaChatMessage * len(messages))()

        for i, message in enumerate(messages):
            c_messages[i].role = message["role"]
            c_messages[i].content = message["content"]

        return c_messages

    def convert_input(self, messages: list[dict]) -> bytes:
        encoded = [
            {k: v.encode("utf-8") if isinstance(v, str) else v for k, v in msg.items()}
            for msg in messages
        ]
        c_messages = self.convert_messages(encoded)
        size = c_llama_chat_apply_template(self.template, c_messages, len(c_messages), True, None, 0)
        if size < 0:
            raise ValueError("Failed to calculate template size")
        c_buffer = ctypes.create_string_buffer(size + 1)
        result = c_llama_chat_apply_template(self.template, c_messages, len(c_messages), True, c_buffer, size + 1)
        if result < 0:
            raise ValueError("Failed to apply chat template")
        return c_buffer.raw[:result]

    def tokenize(self, c_buffer: bytes, max_output_tokens: int):
        max_tokens = len(c_buffer) + max_output_tokens

        c_tokens = (ctypes.c_int32 * max_tokens)()
        n_tokens = c_llama_tokenize(
            self.vocab, c_buffer, len(c_buffer), c_tokens, max_tokens, True, True)

        if n_tokens < 0:
            raise ValueError("Tokenize failed")

        return c_tokens, n_tokens

    def close(self):
        if hasattr(self, "pointer"):
            c_llama_model_free(self.pointer)
            del self.pointer
            if hasattr(self, "vocab"):
                del self.vocab

    def __del__(self):
        self.close()


class Context:
    context_id: int
    pointer: LlamaContextPointer

    def __init__(self, model: Model, config: ModelProfile):
        self.context_id = config.context_id
        self.pointer = c_llama_init_from_model(
            model.pointer,
            config.context_params)
        if not self.pointer:
            raise RuntimeError("Failed to initialize context")

    def decode(self, c_tokens: ctypes.Array, n_tokens: int):
        if n_tokens > self.n_ctx:
            raise ValueError(f"Context exceeded")

        n_batch = self.n_batch
        c_tokens_iterator = ctypes.addressof(c_tokens)
        for i in range(0, n_tokens, n_batch):
            num_to_decode = min(n_tokens - i, n_batch)
            c_batch_tokens = ctypes.cast(c_tokens_iterator, ctypes.POINTER(ctypes.c_int32))

            c_batch = c_llama_batch_get_one(c_batch_tokens, num_to_decode)
            if c_llama_decode(self.pointer, c_batch) != 0:
                raise RuntimeError("Decode failed")

            c_tokens_iterator += num_to_decode * ctypes.sizeof(ctypes.c_int32)

    @property
    def n_ctx(self):
        return c_llama_n_ctx(self.pointer)

    @property
    def n_batch(self):
        return c_llama_n_batch(self.pointer)

    def get_memory(self):
        return c_llama_get_memory(self.pointer)

    def clear(self):
        memory = self.get_memory()
        if memory:
            c_llama_memory_clear(memory, True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if hasattr(self, "pointer"):
            c_llama_free(self.pointer)
            del self.pointer

    def __del__(self):
        self.close()


class SamplerChain:
    sampler_chain_id: int
    pointer: LlamaSamplerPointer

    def __init__(self, config: ModelProfile):
        self.sampler_chain_id = config.sampler_chain_id
        self.pointer = c_llama_sampler_chain_init(config.sampler_chain_params)
        # c_llama_sampler_chain_init(config.sampler_chain_params)

        if not self.pointer:
            raise RuntimeError("Failed to initialize sampler chain")

        if "top_k" in config.sampler_kwargs:
            top_k = c_llama_sampler_init_top_k(config.sampler_kwargs["top_k"])
            c_llama_sampler_chain_add(self.pointer, top_k)
        if "top_p" in config.sampler_kwargs:
            top_p = c_llama_sampler_init_top_p(config.sampler_kwargs["top_p"], 1)
            c_llama_sampler_chain_add(self.pointer, top_p)
        if "min_p" in config.sampler_kwargs:
            min_p = c_llama_sampler_init_min_p(config.sampler_kwargs["min_p"], 1)
            c_llama_sampler_chain_add(self.pointer, min_p)
        if "temperature" in config.sampler_kwargs:
            temperature = c_llama_sampler_init_temp(config.sampler_kwargs["temperature"])
            c_llama_sampler_chain_add(self.pointer, temperature)

        seed = config.sampler_kwargs.get("seed", 0xFFFFFFFF)
        c_llama_sampler_chain_add(self.pointer, c_llama_sampler_init_dist(seed))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if hasattr(self, "pointer"):
            c_llama_sampler_free(self.pointer)
            del self.pointer

    def __del__(self):
        self.close()


class Router:
    _backend: Backend
    _model: None | Model
    _context: None | Context

    def __init__(self):
        self._backend = Backend()
        self._model = None
        self._context = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _unload_model(self):
        assert self._model, "No model to unload"
        self._model.close()
        self._model = None

    def _load_model(self, config: ModelProfile):
        assert not self._model, "Model already loaded"
        self._model = Model(config)

    def _unload_context(self):
        assert self._context, "No context to unload"
        self._context.close()
        self._context = None

    def _load_context(self, config: ModelProfile):
        assert not self._context, "Context already loaded"
        assert self._model, "Model must be loaded before context"
        self._context = Context(self._model, config)

    def load(self, config: ModelProfile):
        if self._model and self._model.model_id == config.model_id:
            if not self._context or self._context.context_id != config.context_id:
                if self._context:
                    self._unload_context()
                self._load_context(config)
        else:
            self.unload()
            self._load_model(config)
            self._load_context(config)

    def unload(self):
        if self._context:
            self._unload_context()
        if self._model:
            self._unload_model()

    def _yield_tokens(self, sampler_chain: SamplerChain, max_tokens: int) -> Generator[str, None, None]:
        assert self._model, "Model not loaded"
        assert self._context, "Context not loaded"

        c_piece = ctypes.create_string_buffer(128)

        for _ in range(max_tokens):
            token = ctypes.c_int32(c_llama_sampler_sample(sampler_chain.pointer, self._context.pointer, -1))
            c_llama_sampler_accept(sampler_chain.pointer, token.value)

            if c_llama_vocab_is_eog(self._model.vocab, token.value):
                break

            c_piece_written = c_llama_token_to_piece(self._model.vocab, token.value, c_piece, 128, 0, True)
            if c_piece_written > 0:
                yield c_piece.value[:c_piece_written].decode()

            batch = c_llama_batch_get_one(ctypes.pointer(token), 1)
            if c_llama_decode(self._context.pointer, batch) != 0:
                break

    def chat_completion(self, config: ModelProfile, messages: list[dict], max_tokens: int = 512) -> str:
        return "".join(self.stream_chat_completion(config, messages, max_tokens))

    def stream_chat_completion(self, config: ModelProfile, messages: list[dict], max_tokens: int = 512):
        try:
            self.load(config)
            assert self._model, "Model failed to load"
            assert self._context, "Context failed to load"
            self._context.clear()

            prompt_bytes = self._model.convert_input(messages)
    
            c_tokens, n_tokens = self._model.tokenize(prompt_bytes, max_tokens)
            self._context.decode(c_tokens, n_tokens)
    
            def _gen():
                with SamplerChain(config) as sampler_chain:
                    yield from self._yield_tokens(sampler_chain, max_tokens)
    
            return _gen()
        except ValueError as e:
            if str(e) == "Context exceeded" and config.fallback is not None:
                return self.stream_chat_completion(config.fallback, messages, max_tokens)
            raise

    def completion(self, config: ModelProfile, prompt: str, max_tokens: int = 512) -> str:
        return "".join(self.stream_completion(config, prompt, max_tokens))

    def stream_completion(self, config: ModelProfile, prompt: str, max_tokens: int = 512):
        try:
            self.load(config)
            assert self._model, "Model failed to load"
            assert self._context, "Context failed to load"
            self._context.clear()
    
            c_tokens, n_tokens = self._model.tokenize(prompt.encode(), max_tokens)
            self._context.decode(c_tokens, n_tokens)
    
            def _gen():
                with SamplerChain(config) as sampler_chain:
                    yield from self._yield_tokens(sampler_chain, max_tokens)
    
            return _gen()
        except ValueError as e:
            if str(e) == "Context exceeded" and config.fallback is not None:
                return self.stream_completion(config.fallback, prompt, max_tokens)
            raise

    def close(self):
        if self._context:
            self._context.close()
            self._context = None
        if self._model:
            self._model.close()
            self._model = None
        if hasattr(self, "_backend"):
            self._backend.close()
            del self._backend

    def __del__(self):
        self.close()
