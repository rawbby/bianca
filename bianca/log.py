import logging

from bianca.bootstrap import *
from bianca.llama_wrapper import *

__all__ = ["logging", "logging_uvicorn_lifespan"]

_Scalar = int | float
_Color = str | float | tuple[_Scalar, _Scalar, _Scalar] | None

_none = ""
_reset = "\x1b[0m"


def _scalar(s: _Scalar) -> int:
    if isinstance(s, int):
        v = float(s) / 255.0
    elif isinstance(s, float):
        v = s
    else:
        # noinspection PyStringConversionWithoutDunderMethod
        raise NotImplementedError(f"Type {type(s)} is not supported as scalar")

    # gamma correction
    l = v ** (1.0 / 2.2)
    l = max(0.0, min(1.0, l))
    return int(l * 255.0)


def _rgb(r: _Scalar, g: _Scalar, b: _Scalar, bold: bool = False) -> str:
    r = _scalar(r)
    g = _scalar(g)
    b = _scalar(b)
    bold = "1;" if bold else ""
    return f"\x1b[{bold}38;2;{r};{g};{b}m"


def _grey(p: _Scalar, bold: bool = False) -> str:
    s = _scalar(p)
    bold = "1;" if bold else ""
    return f"\x1b[{bold}38;2;{s};{s};{s}m"


def _color(color: _Color = None) -> str:
    if isinstance(color, str):
        return color
    if isinstance(color, float):
        return _grey(color)
    if isinstance(color, tuple):
        r, g, b = color
        return _rgb(r, g, b)
    return _none


def _fmt(text: _Color = None, level: _Color = None):
    text_ = _color(text)
    level_ = _color(level)
    _level = text_ or _reset
    _text = _reset if text_ else _none
    return f"{text_}[%(asctime)s] {level_}%(levelname)s {_level}%(name)s: %(message)s{_text}"


_formats = {
    logging.DEBUG: _fmt(0.3),
    logging.INFO: _fmt(0.4, _rgb(0, 0.4, 0.4)),
    logging.WARNING: _fmt(0.5, _rgb(0.4, 0.4, 0)),
    logging.ERROR: _fmt(0.6, _rgb(0.4, 0, 0)),
    logging.CRITICAL: _fmt(_rgb(0.4, 0, 0), _rgb(0.4, 0, 0, bold=True)),
}


class _InterceptFormatter(logging.Formatter):
    def format(self, record: LogRecord) -> str:
        if record.name.startswith("uvicorn."):
            record.name = "uvicorn.py"

        formatter = logging.Formatter(
            _formats.get(record.levelno, _fmt()),
            datefmt="%Y-%m-%d %H:%M:%S")

        if record.exc_info:
            record.exc_text = formatter.formatException(record.exc_info)

        return formatter.format(record)


class _InterceptHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self, sys.stdout)
        logging.StreamHandler.setFormatter(self, _InterceptFormatter())

    def emit(self, record: LogRecord):
        logging.StreamHandler.emit(self, record)


logging.root.handlers = [_InterceptHandler()]
logging.root.setLevel(logging.INFO)

GGML_LOG_LEVEL_NONE = 0
GGML_LOG_LEVEL_DEBUG = 1
GGML_LOG_LEVEL_INFO = 2
GGML_LOG_LEVEL_WARN = 3
GGML_LOG_LEVEL_ERROR = 4
GGML_LOG_LEVEL_CONT = 5

_llama_logger = logging.getLogger("llama.cpp")
_llama_log_level = {
    0: logging.NOTSET,  # LLAMA_NONE
    1: logging.DEBUG,  # LLAMA_DEBUG
    2: logging.INFO,  # LLAMA_INFO
    3: logging.WARNING,  # LLAMA_WARN
    4: logging.ERROR,  # LLAMA_ERROR
}

LlamaLogCallback = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)


# noinspection PyUnusedLocal
@LlamaLogCallback
def _llama_log_callback(level: int, text: bytes, user_data: ctypes.c_void_p):
    if level == 5:  # LLAMA_CONTINUE
        level = getattr(_llama_log_callback, "cont")

    msg = text.decode('utf-8', errors='ignore').strip()
    if msg:
        _llama_logger.log(_llama_log_level.get(level, logging.NOTSET), msg)

    setattr(_llama_log_callback, "cont", level)


setattr(_llama_log_callback, "cont", 0)
c_llama_log_set(_llama_log_callback, None)


@asynccontextmanager
async def logging_uvicorn_lifespan(_):
    """lifespan to add when running fastapi with uvicorn"""
    for name in logging.root.manager.loggerDict.keys():
        if name.startswith("uvicorn"):
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True
    yield
