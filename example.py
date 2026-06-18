from bianca.llama_router import Backend, Router, ModelProfile
from bianca.registry import ModelProfileRegistry

if __name__ == '__main__':
    mpr = ModelProfileRegistry()
    config = mpr["art"]

    with Backend(), Router() as router:
        messages = [
            {"role": "user", "content": "Say hello in one sentence."}
        ]

        print("=== chat_completion ===")
        result = router.chat_completion(config, messages, max_tokens=64)
        assert isinstance(result, str) and len(result) > 0, "chat_completion returned empty result"
        print(result)

        print("\n=== stream_chat_completion ===")
        chunks = list(router.stream_chat_completion(config, messages, max_tokens=64))
        assert len(chunks) > 0, "stream_chat_completion yielded no chunks"
        assert all(isinstance(c, str) for c in chunks), "non-string chunk in stream"
        print("".join(chunks))

        print("\n=== completion ===")
        result = router.completion(config, "The capital of France is", max_tokens=16)
        assert isinstance(result, str) and len(result) > 0, "completion returned empty result"
        print(result)

        print("\nAll checks passed.")
