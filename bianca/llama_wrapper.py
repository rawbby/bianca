from bianca.bootstrap import *

__all__ = [
    "llama",
    "LlamaModelParams",
    "LlamaContextParams",
    "LlamaBatch",
    "LlamaSamplerChainParams",
    "LlamaChatMessage",
    "LlamaModelPointer",
    "LlamaContextPointer",
    "LlamaVocabPointer",
    "LlamaSamplerChainPointer",
    "LlamaLogCallback",
]

llama = ctypes.CDLL(LLAMA_LIB)


class LlamaModelParams(ctypes.Structure):
    _fields_ = [
        ("devices", ctypes.c_void_p),
        ("tensor_buft_overrides", ctypes.c_void_p),
        ("n_gpu_layers", ctypes.c_int32),
        ("split_mode", ctypes.c_int32),
        ("main_gpu", ctypes.c_int32),
        ("tensor_split", ctypes.POINTER(ctypes.c_float)),
        ("progress_callback", ctypes.c_void_p),
        ("progress_callback_user_data", ctypes.c_void_p),
        ("kv_overrides", ctypes.c_void_p),
        ("vocab_only", ctypes.c_bool),
        ("use_mmap", ctypes.c_bool),
        ("use_direct_io", ctypes.c_bool),
        ("use_mlock", ctypes.c_bool),
        ("check_tensors", ctypes.c_bool),
        ("use_extra_bufts", ctypes.c_bool),
        ("no_host", ctypes.c_bool),
        ("no_alloc", ctypes.c_bool),
    ]


class LlamaContextParams(ctypes.Structure):
    _fields_ = [
        ("n_ctx", ctypes.c_uint32),
        ("n_batch", ctypes.c_uint32),
        ("n_ubatch", ctypes.c_uint32),
        ("n_seq_max", ctypes.c_uint32),
        ("n_rs_seq", ctypes.c_uint32),
        ("n_outputs_max", ctypes.c_uint32),
        ("n_threads", ctypes.c_int32),
        ("n_threads_batch", ctypes.c_int32),
        ("ctx_type", ctypes.c_int32),
        ("rope_scaling_type", ctypes.c_int32),
        ("pooling_type", ctypes.c_int32),
        ("attention_type", ctypes.c_int32),
        ("flash_attn_type", ctypes.c_int32),
        ("rope_freq_base", ctypes.c_float),
        ("rope_freq_scale", ctypes.c_float),
        ("yarn_ext_factor", ctypes.c_float),
        ("yarn_attn_factor", ctypes.c_float),
        ("yarn_beta_fast", ctypes.c_float),
        ("yarn_beta_slow", ctypes.c_float),
        ("yarn_orig_ctx", ctypes.c_uint32),
        ("defrag_thold", ctypes.c_float),
        ("cb_eval", ctypes.c_void_p),
        ("cb_eval_user_data", ctypes.c_void_p),
        ("type_k", ctypes.c_int32),
        ("type_v", ctypes.c_int32),
        ("abort_callback", ctypes.c_void_p),
        ("abort_callback_data", ctypes.c_void_p),
        ("embeddings", ctypes.c_bool),
        ("offload_kqv", ctypes.c_bool),
        ("no_perf", ctypes.c_bool),
        ("op_offload", ctypes.c_bool),
        ("swa_full", ctypes.c_bool),
        ("kv_unified", ctypes.c_bool),
        ("samplers", ctypes.c_void_p),
        ("n_samplers", ctypes.c_size_t),
    ]


class LlamaBatch(ctypes.Structure):
    _fields_ = [
        ("n_tokens", ctypes.c_int32),
        ("token", ctypes.POINTER(ctypes.c_int32)),
        ("embd", ctypes.POINTER(ctypes.c_float)),
        ("pos", ctypes.POINTER(ctypes.c_int32)),
        ("n_seq_id", ctypes.POINTER(ctypes.c_int32)),
        ("seq_id", ctypes.POINTER(ctypes.POINTER(ctypes.c_int32))),
        ("logits", ctypes.POINTER(ctypes.c_int8)),
    ]


class LlamaSamplerChainParams(ctypes.Structure):
    _fields_ = [
        ("no_perf", ctypes.c_bool)
    ]


class LlamaChatMessage(ctypes.Structure):
    _fields_ = [
        ("role", ctypes.c_char_p),
        ("content", ctypes.c_char_p)
    ]


LlamaModelPointer = ctypes.c_void_p
LlamaContextPointer = ctypes.c_void_p
LlamaVocabPointer = ctypes.c_void_p
LlamaSamplerChainPointer = ctypes.c_void_p
LlamaMemoryPointer = ctypes.c_void_p

LlamaLogCallback = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)

llama.llama_backend_init.argtypes = []
llama.llama_backend_init.restype = None

llama.llama_backend_free.argtypes = []
llama.llama_backend_free.restype = None

llama.llama_model_default_params.argtypes = []
llama.llama_model_default_params.restype = LlamaModelParams

llama.llama_context_default_params.argtypes = []
llama.llama_context_default_params.restype = LlamaContextParams

llama.llama_sampler_chain_default_params.argtypes = []
llama.llama_sampler_chain_default_params.restype = LlamaSamplerChainParams

llama.llama_model_load_from_file.argtypes = [ctypes.c_char_p, LlamaModelParams]
llama.llama_model_load_from_file.restype = LlamaModelPointer

llama.llama_model_free.argtypes = [LlamaModelPointer]
llama.llama_model_free.restype = None

llama.llama_model_get_vocab.argtypes = [LlamaModelPointer]
llama.llama_model_get_vocab.restype = LlamaVocabPointer

llama.llama_model_chat_template.argtypes = [LlamaModelPointer, ctypes.c_char_p]
llama.llama_model_chat_template.restype = ctypes.c_char_p

llama.llama_init_from_model.argtypes = [LlamaModelPointer, LlamaContextParams]
llama.llama_init_from_model.restype = LlamaContextPointer

llama.llama_free.argtypes = [LlamaContextPointer]
llama.llama_free.restype = None

llama.llama_tokenize.argtypes = [
    LlamaVocabPointer,
    ctypes.c_char_p,
    ctypes.c_int32,
    ctypes.POINTER(ctypes.c_int32),
    ctypes.c_int32,
    ctypes.c_bool, ctypes.c_bool
]
llama.llama_tokenize.restype = ctypes.c_int32

llama.llama_token_to_piece.argtypes = [
    LlamaVocabPointer,
    ctypes.c_int32,
    ctypes.c_char_p,
    ctypes.c_int32,
    ctypes.c_int32,
    ctypes.c_bool
]
llama.llama_token_to_piece.restype = ctypes.c_int32

llama.llama_vocab_is_eog.argtypes = [LlamaVocabPointer, ctypes.c_int32]
llama.llama_vocab_is_eog.restype = ctypes.c_bool

llama.llama_batch_get_one.argtypes = [ctypes.POINTER(ctypes.c_int32), ctypes.c_int32]
llama.llama_batch_get_one.restype = LlamaBatch

llama.llama_decode.argtypes = [LlamaContextPointer, LlamaBatch]
llama.llama_decode.restype = ctypes.c_int32

llama.llama_chat_apply_template.argtypes = [
    ctypes.c_char_p,
    ctypes.POINTER(LlamaChatMessage),
    ctypes.c_size_t,
    ctypes.c_bool,
    ctypes.c_char_p,
    ctypes.c_int32
]
llama.llama_chat_apply_template.restype = ctypes.c_int32

llama.llama_sampler_chain_init.argtypes = [LlamaSamplerChainParams]
llama.llama_sampler_chain_init.restype = LlamaSamplerChainPointer

llama.llama_sampler_init_temp.argtypes = [ctypes.c_float]
llama.llama_sampler_init_temp.restype = LlamaSamplerChainPointer

llama.llama_sampler_init_top_k.argtypes = [ctypes.c_int32]
llama.llama_sampler_init_top_k.restype = LlamaSamplerChainPointer

llama.llama_sampler_init_top_p.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_top_p.restype = LlamaSamplerChainPointer

llama.llama_sampler_init_min_p.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_min_p.restype = LlamaSamplerChainPointer

llama.llama_sampler_init_dist.argtypes = [ctypes.c_uint32]
llama.llama_sampler_init_dist.restype = LlamaSamplerChainPointer

llama.llama_sampler_chain_add.argtypes = [LlamaSamplerChainPointer, LlamaSamplerChainPointer]
llama.llama_sampler_chain_add.restype = None

llama.llama_sampler_sample.argtypes = [LlamaSamplerChainPointer, LlamaContextPointer, ctypes.c_int32]
llama.llama_sampler_sample.restype = ctypes.c_int32

llama.llama_sampler_accept.argtypes = [LlamaSamplerChainPointer, ctypes.c_int32]
llama.llama_sampler_accept.restype = None

llama.llama_sampler_free.argtypes = [LlamaSamplerChainPointer]
llama.llama_sampler_free.restype = None

llama.llama_model_n_embd.argtypes = [LlamaModelPointer]
llama.llama_model_n_embd.restype = ctypes.c_int32

llama.llama_get_embeddings.argtypes = [LlamaContextPointer]
llama.llama_get_embeddings.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_embeddings_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_embeddings_ith.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_n_ctx.argtypes = [LlamaContextPointer]
llama.llama_n_ctx.restype = ctypes.c_uint32

llama.llama_n_batch.argtypes = [LlamaContextPointer]
llama.llama_n_batch.restype = ctypes.c_uint32

llama.llama_get_memory.argtypes = [LlamaContextPointer]
llama.llama_get_memory.restype = LlamaMemoryPointer

llama.llama_memory_clear.argtypes = [LlamaMemoryPointer, ctypes.c_bool]
llama.llama_memory_clear.restype = None

llama.llama_log_set.argtypes = [LlamaLogCallback, ctypes.c_void_p]
llama.llama_log_set.restype = None
