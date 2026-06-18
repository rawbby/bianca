# bianca

A simple LLaMA router and model profile registry package for interacting with LLM agents.

## Features

- **Model Registry:** Simple profile registry for LLM models.
- **LLaMA Router:** Provides an easy-to-use API to handle stream chat completions.
- **FastAPI Integration:** Easily expose LLM capabilities through APIs.

## Installation

```bash
pip install git+https://github.com/rawbby/bianca.git@v0.1.1
```

## Example

```python
import logging
from bianca.registry import ModelProfileRegistry
from bianca.llama_router import Router


def main():
    mpr = ModelProfileRegistry()
    config = mpr["default"]

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello, world!"
        }
    ]

    with Router() as router:
        response = "".join([it for it in router.stream_chat_completion(
            config, messages, max_tokens=1024
        )])
        logging.getLogger("example").info(response)


if __name__ == "__main__":
    main()
```
