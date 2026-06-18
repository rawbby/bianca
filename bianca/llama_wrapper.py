from bianca.bootstrap import *

__all__ = [
    "LlamaBatch",
    "PyLlamaBatch",
    "LlamaModelKvOverride",
    "PyLlamaModelKvOverride",
    "LlamaModelTensorBuftOverride",
    "PyLlamaModelTensorBuftOverride",
    "LlamaModelParams",
    "PyLlamaModelParams",
    "LlamaSamplerSeqConfig",
    "PyLlamaSamplerSeqConfig",
    "LlamaContextParams",
    "PyLlamaContextParams",
    "LlamaSamplerChainParams",
    "PyLlamaSamplerChainParams",
    "LlamaChatMessage",
    "PyLlamaChatMessage",
    "LlamaSamplerI",
    "PyLlamaSamplerI",
    "LlamaSampler",
    "PyLlamaSampler",
    "LlamaTokenPointer",
    "LlamaVocabPointer",
    "LlamaModelTensorBuftOverridePointer",
    "LlamaSeqIdPointer",
    "LlamaContextPointer",
    "LlamaModelPointer",
    "LlamaPosPointer",
    "LlamaModelKvOverridePointer",
    "LlamaSamplerIPointer",
    "LlamaSamplerSeqConfigPointer",
    "LlamaSamplerPointer",
    "LlamaChatMessagePointer",
    "c_llama_model_default_params",
    "llama_model_default_params",
    "c_llama_context_default_params",
    "llama_context_default_params",
    "c_llama_sampler_chain_default_params",
    "llama_sampler_chain_default_params",
    "c_llama_backend_init",
    "llama_backend_init",
    "c_llama_backend_free",
    "llama_backend_free",
    "c_llama_model_load_from_file",
    "llama_model_load_from_file",
    "c_llama_model_free",
    "llama_model_free",
    "c_llama_init_from_model",
    "llama_init_from_model",
    "c_llama_free",
    "llama_free",
    "c_llama_n_ctx",
    "llama_n_ctx",
    "c_llama_n_batch",
    "llama_n_batch",
    "c_llama_get_memory",
    "llama_get_memory",
    "c_llama_model_get_vocab",
    "llama_model_get_vocab",
    "c_llama_model_chat_template",
    "llama_model_chat_template",
    "c_llama_memory_clear",
    "llama_memory_clear",
    "c_llama_batch_get_one",
    "llama_batch_get_one",
    "c_llama_decode",
    "llama_decode",
    "c_llama_vocab_is_eog",
    "llama_vocab_is_eog",
    "c_llama_tokenize",
    "llama_tokenize",
    "c_llama_token_to_piece",
    "llama_token_to_piece",
    "c_llama_chat_apply_template",
    "llama_chat_apply_template",
    "c_llama_sampler_init",
    "llama_sampler_init",
    "c_llama_sampler_accept",
    "llama_sampler_accept",
    "c_llama_sampler_free",
    "llama_sampler_free",
    "c_llama_sampler_chain_init",
    "llama_sampler_chain_init",
    "c_llama_sampler_chain_add",
    "llama_sampler_chain_add",
    "c_llama_sampler_init_dist",
    "llama_sampler_init_dist",
    "c_llama_sampler_init_top_k",
    "llama_sampler_init_top_k",
    "c_llama_sampler_init_top_p",
    "llama_sampler_init_top_p",
    "c_llama_sampler_init_min_p",
    "llama_sampler_init_min_p",
    "c_llama_sampler_init_temp",
    "llama_sampler_init_temp",
    "c_llama_sampler_sample",
    "llama_sampler_sample",
    "c_llama_log_set",
    "llama_log_set",
]

llama = ctypes.CDLL(LLAMA_LIB)


class LlamaContext(ctypes.Structure):
    pass


class LlamaModel(ctypes.Structure):
    pass


class LlamaPos(ctypes.Structure):
    pass


class LlamaSeqId(ctypes.Structure):
    pass


class LlamaToken(ctypes.Structure):
    pass


class LlamaVocab(ctypes.Structure):
    pass


class LlamaBatch(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaBatch':
        return PyLlamaBatch(
            n_tokens=self.n_tokens,
            token=self.token,
            embd=self.embd,
            pos=self.pos,
            n_seq_id=self.n_seq_id,
            seq_id=self.seq_id,
            logits=self.logits,
        )

    @py.setter
    def py(self, value: 'PyLlamaBatch'):
        setattr(self, "n_tokens", value.c.n_tokens)
        setattr(self, "token", value.c.token)
        setattr(self, "embd", value.c.embd)
        setattr(self, "pos", value.c.pos)
        setattr(self, "n_seq_id", value.c.n_seq_id)
        setattr(self, "seq_id", value.c.seq_id)
        setattr(self, "logits", value.c.logits)


class LlamaModelKvOverride(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaModelKvOverride':
        return PyLlamaModelKvOverride(
            tag=self.tag,
            key=self.key,
        )

    @py.setter
    def py(self, value: 'PyLlamaModelKvOverride'):
        setattr(self, "tag", value.c.tag)
        setattr(self, "key", value.c.key)


class LlamaModelTensorBuftOverride(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaModelTensorBuftOverride':
        return PyLlamaModelTensorBuftOverride(
            pattern=self.pattern,
            buft=self.buft,
        )

    @py.setter
    def py(self, value: 'PyLlamaModelTensorBuftOverride'):
        setattr(self, "pattern", value.c.pattern)
        setattr(self, "buft", value.c.buft)


class LlamaModelParams(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaModelParams':
        return PyLlamaModelParams(
            devices=self.devices,
            tensor_buft_overrides=self.tensor_buft_overrides,
            n_gpu_layers=self.n_gpu_layers,
            split_mode=self.split_mode,
            main_gpu=self.main_gpu,
            tensor_split=self.tensor_split,
            progress_callback=self.progress_callback,
            progress_callback_user_data=self.progress_callback_user_data,
            kv_overrides=self.kv_overrides,
            vocab_only=self.vocab_only,
            use_mmap=self.use_mmap,
            use_direct_io=self.use_direct_io,
            use_mlock=self.use_mlock,
            check_tensors=self.check_tensors,
            use_extra_bufts=self.use_extra_bufts,
            no_host=self.no_host,
            no_alloc=self.no_alloc,
        )

    @py.setter
    def py(self, value: 'PyLlamaModelParams'):
        setattr(self, "devices", value.c.devices)
        setattr(self, "tensor_buft_overrides", value.c.tensor_buft_overrides)
        setattr(self, "n_gpu_layers", value.c.n_gpu_layers)
        setattr(self, "split_mode", value.c.split_mode)
        setattr(self, "main_gpu", value.c.main_gpu)
        setattr(self, "tensor_split", value.c.tensor_split)
        setattr(self, "progress_callback", value.c.progress_callback)
        setattr(self, "progress_callback_user_data", value.c.progress_callback_user_data)
        setattr(self, "kv_overrides", value.c.kv_overrides)
        setattr(self, "vocab_only", value.c.vocab_only)
        setattr(self, "use_mmap", value.c.use_mmap)
        setattr(self, "use_direct_io", value.c.use_direct_io)
        setattr(self, "use_mlock", value.c.use_mlock)
        setattr(self, "check_tensors", value.c.check_tensors)
        setattr(self, "use_extra_bufts", value.c.use_extra_bufts)
        setattr(self, "no_host", value.c.no_host)
        setattr(self, "no_alloc", value.c.no_alloc)


class LlamaSamplerSeqConfig(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaSamplerSeqConfig':
        return PyLlamaSamplerSeqConfig(
            seq_id=self.seq_id,
            sampler=self.sampler,
        )

    @py.setter
    def py(self, value: 'PyLlamaSamplerSeqConfig'):
        setattr(self, "seq_id", value.c.seq_id)
        setattr(self, "sampler", value.c.sampler)


class LlamaContextParams(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaContextParams':
        return PyLlamaContextParams(
            n_ctx=self.n_ctx,
            n_batch=self.n_batch,
            n_ubatch=self.n_ubatch,
            n_seq_max=self.n_seq_max,
            n_rs_seq=self.n_rs_seq,
            n_outputs_max=self.n_outputs_max,
            n_threads=self.n_threads,
            n_threads_batch=self.n_threads_batch,
            ctx_type=self.ctx_type,
            rope_scaling_type=self.rope_scaling_type,
            pooling_type=self.pooling_type,
            attention_type=self.attention_type,
            flash_attn_type=self.flash_attn_type,
            rope_freq_base=self.rope_freq_base,
            rope_freq_scale=self.rope_freq_scale,
            yarn_ext_factor=self.yarn_ext_factor,
            yarn_attn_factor=self.yarn_attn_factor,
            yarn_beta_fast=self.yarn_beta_fast,
            yarn_beta_slow=self.yarn_beta_slow,
            yarn_orig_ctx=self.yarn_orig_ctx,
            defrag_thold=self.defrag_thold,
            cb_eval=self.cb_eval,
            cb_eval_user_data=self.cb_eval_user_data,
            type_k=self.type_k,
            type_v=self.type_v,
            abort_callback=self.abort_callback,
            abort_callback_data=self.abort_callback_data,
            embeddings=self.embeddings,
            offload_kqv=self.offload_kqv,
            no_perf=self.no_perf,
            op_offload=self.op_offload,
            swa_full=self.swa_full,
            kv_unified=self.kv_unified,
            samplers=self.samplers,
            n_samplers=self.n_samplers,
            ctx_other=self.ctx_other,
        )

    @py.setter
    def py(self, value: 'PyLlamaContextParams'):
        setattr(self, "n_ctx", value.c.n_ctx)
        setattr(self, "n_batch", value.c.n_batch)
        setattr(self, "n_ubatch", value.c.n_ubatch)
        setattr(self, "n_seq_max", value.c.n_seq_max)
        setattr(self, "n_rs_seq", value.c.n_rs_seq)
        setattr(self, "n_outputs_max", value.c.n_outputs_max)
        setattr(self, "n_threads", value.c.n_threads)
        setattr(self, "n_threads_batch", value.c.n_threads_batch)
        setattr(self, "ctx_type", value.c.ctx_type)
        setattr(self, "rope_scaling_type", value.c.rope_scaling_type)
        setattr(self, "pooling_type", value.c.pooling_type)
        setattr(self, "attention_type", value.c.attention_type)
        setattr(self, "flash_attn_type", value.c.flash_attn_type)
        setattr(self, "rope_freq_base", value.c.rope_freq_base)
        setattr(self, "rope_freq_scale", value.c.rope_freq_scale)
        setattr(self, "yarn_ext_factor", value.c.yarn_ext_factor)
        setattr(self, "yarn_attn_factor", value.c.yarn_attn_factor)
        setattr(self, "yarn_beta_fast", value.c.yarn_beta_fast)
        setattr(self, "yarn_beta_slow", value.c.yarn_beta_slow)
        setattr(self, "yarn_orig_ctx", value.c.yarn_orig_ctx)
        setattr(self, "defrag_thold", value.c.defrag_thold)
        setattr(self, "cb_eval", value.c.cb_eval)
        setattr(self, "cb_eval_user_data", value.c.cb_eval_user_data)
        setattr(self, "type_k", value.c.type_k)
        setattr(self, "type_v", value.c.type_v)
        setattr(self, "abort_callback", value.c.abort_callback)
        setattr(self, "abort_callback_data", value.c.abort_callback_data)
        setattr(self, "embeddings", value.c.embeddings)
        setattr(self, "offload_kqv", value.c.offload_kqv)
        setattr(self, "no_perf", value.c.no_perf)
        setattr(self, "op_offload", value.c.op_offload)
        setattr(self, "swa_full", value.c.swa_full)
        setattr(self, "kv_unified", value.c.kv_unified)
        setattr(self, "samplers", value.c.samplers)
        setattr(self, "n_samplers", value.c.n_samplers)
        setattr(self, "ctx_other", value.c.ctx_other)


class LlamaSamplerChainParams(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaSamplerChainParams':
        return PyLlamaSamplerChainParams(
            no_perf=self.no_perf,
        )

    @py.setter
    def py(self, value: 'PyLlamaSamplerChainParams'):
        setattr(self, "no_perf", value.c.no_perf)


class LlamaChatMessage(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaChatMessage':
        return PyLlamaChatMessage(
            role=self.role,
            content=self.content,
        )

    @py.setter
    def py(self, value: 'PyLlamaChatMessage'):
        setattr(self, "role", value.c.role)
        setattr(self, "content", value.c.content)


class LlamaSamplerI(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaSamplerI':
        return PyLlamaSamplerI(
            name=self.name,
            accept=self.accept,
            apply=self.apply,
            reset=self.reset,
            clone=self.clone,
            free=self.free,
            backend_init=self.backend_init,
            backend_accept=self.backend_accept,
            backend_apply=self.backend_apply,
            backend_set_input=self.backend_set_input,
        )

    @py.setter
    def py(self, value: 'PyLlamaSamplerI'):
        setattr(self, "name", value.c.name)
        setattr(self, "accept", value.c.accept)
        setattr(self, "apply", value.c.apply)
        setattr(self, "reset", value.c.reset)
        setattr(self, "clone", value.c.clone)
        setattr(self, "free", value.c.free)
        setattr(self, "backend_init", value.c.backend_init)
        setattr(self, "backend_accept", value.c.backend_accept)
        setattr(self, "backend_apply", value.c.backend_apply)
        setattr(self, "backend_set_input", value.c.backend_set_input)


class LlamaSampler(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaSampler':
        return PyLlamaSampler(
            iface=self.iface,
            ctx=self.ctx,
        )

    @py.setter
    def py(self, value: 'PyLlamaSampler'):
        setattr(self, "iface", value.c.iface)
        setattr(self, "ctx", value.c.ctx)


LlamaChatMessagePointer = ctypes.POINTER(LlamaChatMessage)
LlamaContextPointer = ctypes.c_void_p
LlamaModelKvOverridePointer = ctypes.POINTER(LlamaModelKvOverride)
LlamaModelPointer = ctypes.c_void_p
LlamaModelTensorBuftOverridePointer = ctypes.POINTER(LlamaModelTensorBuftOverride)
LlamaPosPointer = ctypes.c_void_p
LlamaSamplerIPointer = ctypes.POINTER(LlamaSamplerI)
LlamaSamplerPointer = ctypes.POINTER(LlamaSampler)
LlamaSamplerSeqConfigPointer = ctypes.POINTER(LlamaSamplerSeqConfig)
LlamaSeqIdPointer = ctypes.c_void_p
LlamaTokenPointer = ctypes.c_void_p
LlamaVocabPointer = ctypes.c_void_p

LlamaBatch._fields_ = [
    ("n_tokens", ctypes.c_int32),
    ("token", LlamaTokenPointer),
    ("embd", ctypes.POINTER(ctypes.c_float)),
    ("pos", LlamaPosPointer),
    ("n_seq_id", ctypes.POINTER(ctypes.c_int32)),
    ("seq_id", ctypes.POINTER(LlamaSeqIdPointer)),
    ("logits", ctypes.POINTER(ctypes.c_int8)),
]

LlamaModelKvOverride._fields_ = [
    ("tag", ctypes.c_int32),
    ("key", (ctypes.c_char * 128)),
]

LlamaModelTensorBuftOverride._fields_ = [
    ("pattern", ctypes.c_char_p),
    ("buft", ctypes.c_void_p),
]

LlamaModelParams._fields_ = [
    ("devices", ctypes.POINTER(ctypes.c_void_p)),
    ("tensor_buft_overrides", LlamaModelTensorBuftOverridePointer),
    ("n_gpu_layers", ctypes.c_int32),
    ("split_mode", ctypes.c_int32),
    ("main_gpu", ctypes.c_int32),
    ("tensor_split", ctypes.POINTER(ctypes.c_float)),
    ("progress_callback", ctypes.c_void_p),
    ("progress_callback_user_data", ctypes.c_void_p),
    ("kv_overrides", LlamaModelKvOverridePointer),
    ("vocab_only", ctypes.c_bool),
    ("use_mmap", ctypes.c_bool),
    ("use_direct_io", ctypes.c_bool),
    ("use_mlock", ctypes.c_bool),
    ("check_tensors", ctypes.c_bool),
    ("use_extra_bufts", ctypes.c_bool),
    ("no_host", ctypes.c_bool),
    ("no_alloc", ctypes.c_bool),
]

LlamaSamplerSeqConfig._fields_ = [
    ("seq_id", ctypes.c_void_p),
    ("sampler", LlamaSamplerPointer),
]

LlamaContextParams._fields_ = [
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
    ("abort_callback", ctypes.c_int),
    ("abort_callback_data", ctypes.c_void_p),
    ("embeddings", ctypes.c_bool),
    ("offload_kqv", ctypes.c_bool),
    ("no_perf", ctypes.c_bool),
    ("op_offload", ctypes.c_bool),
    ("swa_full", ctypes.c_bool),
    ("kv_unified", ctypes.c_bool),
    ("samplers", LlamaSamplerSeqConfigPointer),
    ("n_samplers", ctypes.c_size_t),
    ("ctx_other", LlamaContextPointer),
]

LlamaSamplerChainParams._fields_ = [
    ("no_perf", ctypes.c_bool),
]

LlamaChatMessage._fields_ = [
    ("role", ctypes.c_char_p),
    ("content", ctypes.c_char_p),
]

LlamaSamplerI._fields_ = [
    ("name", ctypes.c_void_p),
    ("accept", ctypes.c_void_p),
    ("apply", ctypes.c_void_p),
    ("reset", ctypes.c_void_p),
    ("clone", ctypes.c_void_p),
    ("free", ctypes.c_void_p),
    ("backend_init", ctypes.c_void_p),
    ("backend_accept", ctypes.c_void_p),
    ("backend_apply", ctypes.c_void_p),
    ("backend_set_input", ctypes.c_void_p),
]

LlamaSampler._fields_ = [
    ("iface", LlamaSamplerIPointer),
    ("ctx", ctypes.c_void_p),
]

llama.llama_model_default_params.argtypes = []
llama.llama_model_default_params.restype = LlamaModelParams

llama.llama_context_default_params.argtypes = []
llama.llama_context_default_params.restype = LlamaContextParams

llama.llama_sampler_chain_default_params.argtypes = []
llama.llama_sampler_chain_default_params.restype = LlamaSamplerChainParams

llama.llama_backend_init.argtypes = []
llama.llama_backend_init.restype = None

llama.llama_backend_free.argtypes = []
llama.llama_backend_free.restype = None

llama.llama_model_load_from_file.argtypes = [ctypes.c_char_p, LlamaModelParams]
llama.llama_model_load_from_file.restype = LlamaModelPointer

llama.llama_model_free.argtypes = [LlamaModelPointer]
llama.llama_model_free.restype = None

llama.llama_init_from_model.argtypes = [LlamaModelPointer, LlamaContextParams]
llama.llama_init_from_model.restype = LlamaContextPointer

llama.llama_free.argtypes = [LlamaContextPointer]
llama.llama_free.restype = None

llama.llama_n_ctx.argtypes = [LlamaContextPointer]
llama.llama_n_ctx.restype = ctypes.c_uint32

llama.llama_n_batch.argtypes = [LlamaContextPointer]
llama.llama_n_batch.restype = ctypes.c_uint32

llama.llama_get_memory.argtypes = [LlamaContextPointer]
llama.llama_get_memory.restype = ctypes.c_void_p

llama.llama_model_get_vocab.argtypes = [LlamaModelPointer]
llama.llama_model_get_vocab.restype = LlamaVocabPointer

llama.llama_model_chat_template.argtypes = [LlamaModelPointer, ctypes.c_char_p]
llama.llama_model_chat_template.restype = ctypes.c_char_p

llama.llama_memory_clear.argtypes = [ctypes.c_void_p, ctypes.c_bool]
llama.llama_memory_clear.restype = None

llama.llama_batch_get_one.argtypes = [LlamaTokenPointer, ctypes.c_int32]
llama.llama_batch_get_one.restype = LlamaBatch

llama.llama_decode.argtypes = [LlamaContextPointer, LlamaBatch]
llama.llama_decode.restype = ctypes.c_int32

llama.llama_vocab_is_eog.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_vocab_is_eog.restype = ctypes.c_int

llama.llama_tokenize.argtypes = [LlamaVocabPointer, ctypes.c_char_p, ctypes.c_int32, LlamaTokenPointer, ctypes.c_int32,
                                 ctypes.c_bool, ctypes.c_bool]
llama.llama_tokenize.restype = ctypes.c_int32

llama.llama_token_to_piece.argtypes = [LlamaVocabPointer, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int32,
                                       ctypes.c_int32, ctypes.c_bool]
llama.llama_token_to_piece.restype = ctypes.c_int32

llama.llama_chat_apply_template.argtypes = [ctypes.c_char_p, LlamaChatMessagePointer, ctypes.c_size_t, ctypes.c_bool,
                                            ctypes.c_char_p, ctypes.c_int32]
llama.llama_chat_apply_template.restype = ctypes.c_int32

llama.llama_sampler_init.argtypes = [LlamaSamplerIPointer, ctypes.c_void_p]
llama.llama_sampler_init.restype = LlamaSamplerPointer

llama.llama_sampler_accept.argtypes = [LlamaSamplerPointer, ctypes.c_void_p]
llama.llama_sampler_accept.restype = None

llama.llama_sampler_free.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_free.restype = None

llama.llama_sampler_chain_init.argtypes = [LlamaSamplerChainParams]
llama.llama_sampler_chain_init.restype = LlamaSamplerPointer

llama.llama_sampler_chain_add.argtypes = [LlamaSamplerPointer, LlamaSamplerPointer]
llama.llama_sampler_chain_add.restype = None

llama.llama_sampler_init_dist.argtypes = [ctypes.c_uint32]
llama.llama_sampler_init_dist.restype = LlamaSamplerPointer

llama.llama_sampler_init_top_k.argtypes = [ctypes.c_int32]
llama.llama_sampler_init_top_k.restype = LlamaSamplerPointer

llama.llama_sampler_init_top_p.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_top_p.restype = LlamaSamplerPointer

llama.llama_sampler_init_min_p.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_min_p.restype = LlamaSamplerPointer

llama.llama_sampler_init_temp.argtypes = [ctypes.c_float]
llama.llama_sampler_init_temp.restype = LlamaSamplerPointer

llama.llama_sampler_sample.argtypes = [LlamaSamplerPointer, LlamaContextPointer, ctypes.c_int32]
llama.llama_sampler_sample.restype = ctypes.c_void_p

llama.llama_log_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
llama.llama_log_set.restype = None


class PyLlamaBatch:
    def __init__(self, n_tokens=None, token=None, embd=None, pos=None, n_seq_id=None, seq_id=None, logits=None):
        self.n_tokens = n_tokens
        self.token = token
        self.embd = embd
        self.pos = pos
        self.n_seq_id = n_seq_id
        self.seq_id = seq_id
        self.logits = logits

    @property
    def c(self) -> 'LlamaBatch':
        c_obj = LlamaBatch()
        if self.n_tokens is not None:
            c_obj.n_tokens = self.n_tokens
        if self.token is not None:
            c_obj.token = self.token
        if self.embd is not None:
            c_obj.embd = self.embd
        if self.pos is not None:
            c_obj.pos = self.pos
        if self.n_seq_id is not None:
            c_obj.n_seq_id = self.n_seq_id
        if self.seq_id is not None:
            c_obj.seq_id = self.seq_id
        if self.logits is not None:
            c_obj.logits = self.logits
        return c_obj

    @c.setter
    def c(self, value: 'LlamaBatch'):
        py_obj = value.py
        self.n_tokens = py_obj.n_tokens
        self.token = py_obj.token
        self.embd = py_obj.embd
        self.pos = py_obj.pos
        self.n_seq_id = py_obj.n_seq_id
        self.seq_id = py_obj.seq_id
        self.logits = py_obj.logits


class PyLlamaModelKvOverride:
    def __init__(self, tag=None, key=None):
        self.tag = tag
        self.key = key

    @property
    def c(self) -> 'LlamaModelKvOverride':
        c_obj = LlamaModelKvOverride()
        if self.tag is not None:
            c_obj.tag = self.tag
        if self.key is not None:
            c_obj.key = self.key
        return c_obj

    @c.setter
    def c(self, value: 'LlamaModelKvOverride'):
        py_obj = value.py
        self.tag = py_obj.tag
        self.key = py_obj.key


class PyLlamaModelTensorBuftOverride:
    def __init__(self, pattern=None, buft=None):
        self.pattern = pattern
        self.buft = buft

    @property
    def c(self) -> 'LlamaModelTensorBuftOverride':
        c_obj = LlamaModelTensorBuftOverride()
        if self.pattern is not None:
            c_obj.pattern = self.pattern
        if self.buft is not None:
            c_obj.buft = self.buft
        return c_obj

    @c.setter
    def c(self, value: 'LlamaModelTensorBuftOverride'):
        py_obj = value.py
        self.pattern = py_obj.pattern
        self.buft = py_obj.buft


class PyLlamaModelParams:
    def __init__(self, devices=None, tensor_buft_overrides=None, n_gpu_layers=None, split_mode=None, main_gpu=None,
                 tensor_split=None, progress_callback=None, progress_callback_user_data=None, kv_overrides=None,
                 vocab_only=None, use_mmap=None, use_direct_io=None, use_mlock=None, check_tensors=None,
                 use_extra_bufts=None, no_host=None, no_alloc=None):
        self.devices = devices
        self.tensor_buft_overrides = tensor_buft_overrides
        self.n_gpu_layers = n_gpu_layers
        self.split_mode = split_mode
        self.main_gpu = main_gpu
        self.tensor_split = tensor_split
        self.progress_callback = progress_callback
        self.progress_callback_user_data = progress_callback_user_data
        self.kv_overrides = kv_overrides
        self.vocab_only = vocab_only
        self.use_mmap = use_mmap
        self.use_direct_io = use_direct_io
        self.use_mlock = use_mlock
        self.check_tensors = check_tensors
        self.use_extra_bufts = use_extra_bufts
        self.no_host = no_host
        self.no_alloc = no_alloc

    @property
    def c(self) -> 'LlamaModelParams':
        c_obj = LlamaModelParams()
        if self.devices is not None:
            c_obj.devices = self.devices
        if self.tensor_buft_overrides is not None:
            c_obj.tensor_buft_overrides = self.tensor_buft_overrides
        if self.n_gpu_layers is not None:
            c_obj.n_gpu_layers = self.n_gpu_layers
        if self.split_mode is not None:
            c_obj.split_mode = self.split_mode
        if self.main_gpu is not None:
            c_obj.main_gpu = self.main_gpu
        if self.tensor_split is not None:
            c_obj.tensor_split = self.tensor_split
        if self.progress_callback is not None:
            c_obj.progress_callback = self.progress_callback
        if self.progress_callback_user_data is not None:
            c_obj.progress_callback_user_data = self.progress_callback_user_data
        if self.kv_overrides is not None:
            c_obj.kv_overrides = self.kv_overrides
        if self.vocab_only is not None:
            c_obj.vocab_only = self.vocab_only
        if self.use_mmap is not None:
            c_obj.use_mmap = self.use_mmap
        if self.use_direct_io is not None:
            c_obj.use_direct_io = self.use_direct_io
        if self.use_mlock is not None:
            c_obj.use_mlock = self.use_mlock
        if self.check_tensors is not None:
            c_obj.check_tensors = self.check_tensors
        if self.use_extra_bufts is not None:
            c_obj.use_extra_bufts = self.use_extra_bufts
        if self.no_host is not None:
            c_obj.no_host = self.no_host
        if self.no_alloc is not None:
            c_obj.no_alloc = self.no_alloc
        return c_obj

    @c.setter
    def c(self, value: 'LlamaModelParams'):
        py_obj = value.py
        self.devices = py_obj.devices
        self.tensor_buft_overrides = py_obj.tensor_buft_overrides
        self.n_gpu_layers = py_obj.n_gpu_layers
        self.split_mode = py_obj.split_mode
        self.main_gpu = py_obj.main_gpu
        self.tensor_split = py_obj.tensor_split
        self.progress_callback = py_obj.progress_callback
        self.progress_callback_user_data = py_obj.progress_callback_user_data
        self.kv_overrides = py_obj.kv_overrides
        self.vocab_only = py_obj.vocab_only
        self.use_mmap = py_obj.use_mmap
        self.use_direct_io = py_obj.use_direct_io
        self.use_mlock = py_obj.use_mlock
        self.check_tensors = py_obj.check_tensors
        self.use_extra_bufts = py_obj.use_extra_bufts
        self.no_host = py_obj.no_host
        self.no_alloc = py_obj.no_alloc


class PyLlamaSamplerSeqConfig:
    def __init__(self, seq_id=None, sampler=None):
        self.seq_id = seq_id
        self.sampler = sampler

    @property
    def c(self) -> 'LlamaSamplerSeqConfig':
        c_obj = LlamaSamplerSeqConfig()
        if self.seq_id is not None:
            c_obj.seq_id = self.seq_id
        if self.sampler is not None:
            c_obj.sampler = self.sampler
        return c_obj

    @c.setter
    def c(self, value: 'LlamaSamplerSeqConfig'):
        py_obj = value.py
        self.seq_id = py_obj.seq_id
        self.sampler = py_obj.sampler


class PyLlamaContextParams:
    def __init__(self, n_ctx=None, n_batch=None, n_ubatch=None, n_seq_max=None, n_rs_seq=None, n_outputs_max=None,
                 n_threads=None, n_threads_batch=None, ctx_type=None, rope_scaling_type=None, pooling_type=None,
                 attention_type=None, flash_attn_type=None, rope_freq_base=None, rope_freq_scale=None,
                 yarn_ext_factor=None, yarn_attn_factor=None, yarn_beta_fast=None, yarn_beta_slow=None,
                 yarn_orig_ctx=None, defrag_thold=None, cb_eval=None, cb_eval_user_data=None, type_k=None, type_v=None,
                 abort_callback=None, abort_callback_data=None, embeddings=None, offload_kqv=None, no_perf=None,
                 op_offload=None, swa_full=None, kv_unified=None, samplers=None, n_samplers=None, ctx_other=None):
        self.n_ctx = n_ctx
        self.n_batch = n_batch
        self.n_ubatch = n_ubatch
        self.n_seq_max = n_seq_max
        self.n_rs_seq = n_rs_seq
        self.n_outputs_max = n_outputs_max
        self.n_threads = n_threads
        self.n_threads_batch = n_threads_batch
        self.ctx_type = ctx_type
        self.rope_scaling_type = rope_scaling_type
        self.pooling_type = pooling_type
        self.attention_type = attention_type
        self.flash_attn_type = flash_attn_type
        self.rope_freq_base = rope_freq_base
        self.rope_freq_scale = rope_freq_scale
        self.yarn_ext_factor = yarn_ext_factor
        self.yarn_attn_factor = yarn_attn_factor
        self.yarn_beta_fast = yarn_beta_fast
        self.yarn_beta_slow = yarn_beta_slow
        self.yarn_orig_ctx = yarn_orig_ctx
        self.defrag_thold = defrag_thold
        self.cb_eval = cb_eval
        self.cb_eval_user_data = cb_eval_user_data
        self.type_k = type_k
        self.type_v = type_v
        self.abort_callback = abort_callback
        self.abort_callback_data = abort_callback_data
        self.embeddings = embeddings
        self.offload_kqv = offload_kqv
        self.no_perf = no_perf
        self.op_offload = op_offload
        self.swa_full = swa_full
        self.kv_unified = kv_unified
        self.samplers = samplers
        self.n_samplers = n_samplers
        self.ctx_other = ctx_other

    @property
    def c(self) -> 'LlamaContextParams':
        c_obj = LlamaContextParams()
        if self.n_ctx is not None:
            c_obj.n_ctx = self.n_ctx
        if self.n_batch is not None:
            c_obj.n_batch = self.n_batch
        if self.n_ubatch is not None:
            c_obj.n_ubatch = self.n_ubatch
        if self.n_seq_max is not None:
            c_obj.n_seq_max = self.n_seq_max
        if self.n_rs_seq is not None:
            c_obj.n_rs_seq = self.n_rs_seq
        if self.n_outputs_max is not None:
            c_obj.n_outputs_max = self.n_outputs_max
        if self.n_threads is not None:
            c_obj.n_threads = self.n_threads
        if self.n_threads_batch is not None:
            c_obj.n_threads_batch = self.n_threads_batch
        if self.ctx_type is not None:
            c_obj.ctx_type = self.ctx_type
        if self.rope_scaling_type is not None:
            c_obj.rope_scaling_type = self.rope_scaling_type
        if self.pooling_type is not None:
            c_obj.pooling_type = self.pooling_type
        if self.attention_type is not None:
            c_obj.attention_type = self.attention_type
        if self.flash_attn_type is not None:
            c_obj.flash_attn_type = self.flash_attn_type
        if self.rope_freq_base is not None:
            c_obj.rope_freq_base = self.rope_freq_base
        if self.rope_freq_scale is not None:
            c_obj.rope_freq_scale = self.rope_freq_scale
        if self.yarn_ext_factor is not None:
            c_obj.yarn_ext_factor = self.yarn_ext_factor
        if self.yarn_attn_factor is not None:
            c_obj.yarn_attn_factor = self.yarn_attn_factor
        if self.yarn_beta_fast is not None:
            c_obj.yarn_beta_fast = self.yarn_beta_fast
        if self.yarn_beta_slow is not None:
            c_obj.yarn_beta_slow = self.yarn_beta_slow
        if self.yarn_orig_ctx is not None:
            c_obj.yarn_orig_ctx = self.yarn_orig_ctx
        if self.defrag_thold is not None:
            c_obj.defrag_thold = self.defrag_thold
        if self.cb_eval is not None:
            c_obj.cb_eval = self.cb_eval
        if self.cb_eval_user_data is not None:
            c_obj.cb_eval_user_data = self.cb_eval_user_data
        if self.type_k is not None:
            c_obj.type_k = self.type_k
        if self.type_v is not None:
            c_obj.type_v = self.type_v
        if self.abort_callback is not None:
            c_obj.abort_callback = self.abort_callback
        if self.abort_callback_data is not None:
            c_obj.abort_callback_data = self.abort_callback_data
        if self.embeddings is not None:
            c_obj.embeddings = self.embeddings
        if self.offload_kqv is not None:
            c_obj.offload_kqv = self.offload_kqv
        if self.no_perf is not None:
            c_obj.no_perf = self.no_perf
        if self.op_offload is not None:
            c_obj.op_offload = self.op_offload
        if self.swa_full is not None:
            c_obj.swa_full = self.swa_full
        if self.kv_unified is not None:
            c_obj.kv_unified = self.kv_unified
        if self.samplers is not None:
            c_obj.samplers = self.samplers
        if self.n_samplers is not None:
            c_obj.n_samplers = self.n_samplers
        if self.ctx_other is not None:
            c_obj.ctx_other = self.ctx_other
        return c_obj

    @c.setter
    def c(self, value: 'LlamaContextParams'):
        py_obj = value.py
        self.n_ctx = py_obj.n_ctx
        self.n_batch = py_obj.n_batch
        self.n_ubatch = py_obj.n_ubatch
        self.n_seq_max = py_obj.n_seq_max
        self.n_rs_seq = py_obj.n_rs_seq
        self.n_outputs_max = py_obj.n_outputs_max
        self.n_threads = py_obj.n_threads
        self.n_threads_batch = py_obj.n_threads_batch
        self.ctx_type = py_obj.ctx_type
        self.rope_scaling_type = py_obj.rope_scaling_type
        self.pooling_type = py_obj.pooling_type
        self.attention_type = py_obj.attention_type
        self.flash_attn_type = py_obj.flash_attn_type
        self.rope_freq_base = py_obj.rope_freq_base
        self.rope_freq_scale = py_obj.rope_freq_scale
        self.yarn_ext_factor = py_obj.yarn_ext_factor
        self.yarn_attn_factor = py_obj.yarn_attn_factor
        self.yarn_beta_fast = py_obj.yarn_beta_fast
        self.yarn_beta_slow = py_obj.yarn_beta_slow
        self.yarn_orig_ctx = py_obj.yarn_orig_ctx
        self.defrag_thold = py_obj.defrag_thold
        self.cb_eval = py_obj.cb_eval
        self.cb_eval_user_data = py_obj.cb_eval_user_data
        self.type_k = py_obj.type_k
        self.type_v = py_obj.type_v
        self.abort_callback = py_obj.abort_callback
        self.abort_callback_data = py_obj.abort_callback_data
        self.embeddings = py_obj.embeddings
        self.offload_kqv = py_obj.offload_kqv
        self.no_perf = py_obj.no_perf
        self.op_offload = py_obj.op_offload
        self.swa_full = py_obj.swa_full
        self.kv_unified = py_obj.kv_unified
        self.samplers = py_obj.samplers
        self.n_samplers = py_obj.n_samplers
        self.ctx_other = py_obj.ctx_other


class PyLlamaSamplerChainParams:
    def __init__(self, no_perf=None):
        self.no_perf = no_perf

    @property
    def c(self) -> 'LlamaSamplerChainParams':
        c_obj = LlamaSamplerChainParams()
        if self.no_perf is not None:
            c_obj.no_perf = self.no_perf
        return c_obj

    @c.setter
    def c(self, value: 'LlamaSamplerChainParams'):
        py_obj = value.py
        self.no_perf = py_obj.no_perf


class PyLlamaChatMessage:
    def __init__(self, role=None, content=None):
        self.role = role
        self.content = content

    @property
    def c(self) -> 'LlamaChatMessage':
        c_obj = LlamaChatMessage()
        if self.role is not None:
            c_obj.role = self.role
        if self.content is not None:
            c_obj.content = self.content
        return c_obj

    @c.setter
    def c(self, value: 'LlamaChatMessage'):
        py_obj = value.py
        self.role = py_obj.role
        self.content = py_obj.content


class PyLlamaSamplerI:
    def __init__(self, name=None, accept=None, apply=None, reset=None, clone=None, free=None, backend_init=None,
                 backend_accept=None, backend_apply=None, backend_set_input=None):
        self.name = name
        self.accept = accept
        self.apply = apply
        self.reset = reset
        self.clone = clone
        self.free = free
        self.backend_init = backend_init
        self.backend_accept = backend_accept
        self.backend_apply = backend_apply
        self.backend_set_input = backend_set_input

    @property
    def c(self) -> 'LlamaSamplerI':
        c_obj = LlamaSamplerI()
        if self.name is not None:
            c_obj.name = self.name
        if self.accept is not None:
            c_obj.accept = self.accept
        if self.apply is not None:
            c_obj.apply = self.apply
        if self.reset is not None:
            c_obj.reset = self.reset
        if self.clone is not None:
            c_obj.clone = self.clone
        if self.free is not None:
            c_obj.free = self.free
        if self.backend_init is not None:
            c_obj.backend_init = self.backend_init
        if self.backend_accept is not None:
            c_obj.backend_accept = self.backend_accept
        if self.backend_apply is not None:
            c_obj.backend_apply = self.backend_apply
        if self.backend_set_input is not None:
            c_obj.backend_set_input = self.backend_set_input
        return c_obj

    @c.setter
    def c(self, value: 'LlamaSamplerI'):
        py_obj = value.py
        self.name = py_obj.name
        self.accept = py_obj.accept
        self.apply = py_obj.apply
        self.reset = py_obj.reset
        self.clone = py_obj.clone
        self.free = py_obj.free
        self.backend_init = py_obj.backend_init
        self.backend_accept = py_obj.backend_accept
        self.backend_apply = py_obj.backend_apply
        self.backend_set_input = py_obj.backend_set_input


class PyLlamaSampler:
    def __init__(self, iface=None, ctx=None):
        self.iface = iface
        self.ctx = ctx

    @property
    def c(self) -> 'LlamaSampler':
        c_obj = LlamaSampler()
        if self.iface is not None:
            c_obj.iface = self.iface
        if self.ctx is not None:
            c_obj.ctx = self.ctx
        return c_obj

    @c.setter
    def c(self, value: 'LlamaSampler'):
        py_obj = value.py
        self.iface = py_obj.iface
        self.ctx = py_obj.ctx


def c_llama_model_default_params() -> 'LlamaModelParams':
    return llama.llama_model_default_params()


def llama_model_default_params() -> 'PyLlamaModelParams':
    return c_llama_model_default_params().py


def c_llama_context_default_params() -> 'LlamaContextParams':
    return llama.llama_context_default_params()


def llama_context_default_params() -> 'PyLlamaContextParams':
    return c_llama_context_default_params().py


def c_llama_sampler_chain_default_params() -> 'LlamaSamplerChainParams':
    return llama.llama_sampler_chain_default_params()


def llama_sampler_chain_default_params() -> 'PyLlamaSamplerChainParams':
    return c_llama_sampler_chain_default_params().py


def c_llama_backend_init():
    return llama.llama_backend_init()


def llama_backend_init():
    return c_llama_backend_init()


def c_llama_backend_free():
    return llama.llama_backend_free()


def llama_backend_free():
    return c_llama_backend_free()


def c_llama_model_load_from_file(path_model: bytes, params: 'LlamaModelParams') -> 'LlamaModelPointer':
    return llama.llama_model_load_from_file(path_model, params)


def llama_model_load_from_file(path_model: bytes, params: 'PyLlamaModelParams') -> 'LlamaModelPointer':
    return c_llama_model_load_from_file(path_model, params.c)


def c_llama_model_free(model: 'LlamaModelPointer'):
    return llama.llama_model_free(model)


def llama_model_free(model: 'LlamaModelPointer'):
    return c_llama_model_free(model)


def c_llama_init_from_model(model: 'LlamaModelPointer', params: 'LlamaContextParams') -> 'LlamaContextPointer':
    return llama.llama_init_from_model(model, params)


def llama_init_from_model(model: 'LlamaModelPointer', params: 'PyLlamaContextParams') -> 'LlamaContextPointer':
    return c_llama_init_from_model(model, params.c)


def c_llama_free(ctx: 'LlamaContextPointer'):
    return llama.llama_free(ctx)


def llama_free(ctx: 'LlamaContextPointer'):
    return c_llama_free(ctx)


def c_llama_n_ctx(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_ctx(ctx)


def llama_n_ctx(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_ctx(ctx)


def c_llama_n_batch(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_batch(ctx)


def llama_n_batch(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_batch(ctx)


def c_llama_get_memory(ctx: 'LlamaContextPointer') -> Any:
    return llama.llama_get_memory(ctx)


def llama_get_memory(ctx: 'LlamaContextPointer') -> Any:
    return c_llama_get_memory(ctx)


def c_llama_model_get_vocab(model: 'LlamaModelPointer') -> 'LlamaVocabPointer':
    return llama.llama_model_get_vocab(model)


def llama_model_get_vocab(model: 'LlamaModelPointer') -> 'LlamaVocabPointer':
    return c_llama_model_get_vocab(model)


def c_llama_model_chat_template(model: 'LlamaModelPointer', name: bytes) -> bytes:
    return llama.llama_model_chat_template(model, name)


def llama_model_chat_template(model: 'LlamaModelPointer', name: bytes) -> bytes:
    return c_llama_model_chat_template(model, name)


def c_llama_memory_clear(mem, data: bool):
    return llama.llama_memory_clear(mem, data)


def llama_memory_clear(mem, data: bool):
    return c_llama_memory_clear(mem, data)


def c_llama_batch_get_one(tokens: 'LlamaTokenPointer', n_tokens: int) -> 'LlamaBatch':
    return llama.llama_batch_get_one(tokens, n_tokens)


def llama_batch_get_one(tokens: 'LlamaTokenPointer', n_tokens: int) -> 'PyLlamaBatch':
    return c_llama_batch_get_one(tokens, n_tokens).py


def c_llama_decode(ctx: 'LlamaContextPointer', batch: 'LlamaBatch') -> int:
    return llama.llama_decode(ctx, batch)


def llama_decode(ctx: 'LlamaContextPointer', batch: 'PyLlamaBatch') -> int:
    return c_llama_decode(ctx, batch.c)


def c_llama_vocab_is_eog(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_vocab_is_eog(vocab, token)


def llama_vocab_is_eog(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_vocab_is_eog(vocab, token)


def c_llama_tokenize(vocab: 'LlamaVocabPointer', text: bytes, text_len: int, tokens: 'LlamaTokenPointer',
                     n_tokens_max: int, add_special: bool, parse_special: bool) -> int:
    return llama.llama_tokenize(vocab, text, text_len, tokens, n_tokens_max, add_special, parse_special)


def llama_tokenize(vocab: 'LlamaVocabPointer', text: bytes, text_len: int, tokens: 'LlamaTokenPointer',
                   n_tokens_max: int, add_special: bool, parse_special: bool) -> int:
    return c_llama_tokenize(vocab, text, text_len, tokens, n_tokens_max, add_special, parse_special)


def c_llama_token_to_piece(vocab: 'LlamaVocabPointer', token, buf: bytes, length: int, lstrip: int,
                           special: bool) -> int:
    return llama.llama_token_to_piece(vocab, token, buf, length, lstrip, special)


def llama_token_to_piece(vocab: 'LlamaVocabPointer', token, buf: bytes, length: int, lstrip: int, special: bool) -> int:
    return c_llama_token_to_piece(vocab, token, buf, length, lstrip, special)


def c_llama_chat_apply_template(tmpl: bytes, chat: 'LlamaChatMessagePointer', n_msg: int, add_ass: bool, buf: bytes,
                                length: int) -> int:
    return llama.llama_chat_apply_template(tmpl, chat, n_msg, add_ass, buf, length)


def llama_chat_apply_template(tmpl: bytes, chat: 'LlamaChatMessagePointer', n_msg: int, add_ass: bool, buf: bytes,
                              length: int) -> int:
    return c_llama_chat_apply_template(tmpl, chat, n_msg, add_ass, buf, length)


def c_llama_sampler_init(iface: 'LlamaSamplerIPointer', ctx) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init(iface, ctx)


def llama_sampler_init(iface: 'LlamaSamplerIPointer', ctx) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init(iface, ctx)


def c_llama_sampler_accept(smpl: 'LlamaSamplerPointer', token):
    return llama.llama_sampler_accept(smpl, token)


def llama_sampler_accept(smpl: 'LlamaSamplerPointer', token):
    return c_llama_sampler_accept(smpl, token)


def c_llama_sampler_free(smpl: 'LlamaSamplerPointer'):
    return llama.llama_sampler_free(smpl)


def llama_sampler_free(smpl: 'LlamaSamplerPointer'):
    return c_llama_sampler_free(smpl)


def c_llama_sampler_chain_init(params: 'LlamaSamplerChainParams') -> 'LlamaSamplerPointer':
    return llama.llama_sampler_chain_init(params)


def llama_sampler_chain_init(params: 'PyLlamaSamplerChainParams') -> 'LlamaSamplerPointer':
    return c_llama_sampler_chain_init(params.c)


def c_llama_sampler_chain_add(chain: 'LlamaSamplerPointer', smpl: 'LlamaSamplerPointer'):
    return llama.llama_sampler_chain_add(chain, smpl)


def llama_sampler_chain_add(chain: 'LlamaSamplerPointer', smpl: 'LlamaSamplerPointer'):
    return c_llama_sampler_chain_add(chain, smpl)


def c_llama_sampler_init_dist(seed: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_dist(seed)


def llama_sampler_init_dist(seed: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_dist(seed)


def c_llama_sampler_init_top_k(k: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_top_k(k)


def llama_sampler_init_top_k(k: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_top_k(k)


def c_llama_sampler_init_top_p(p: float, min_keep: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_top_p(p, min_keep)


def llama_sampler_init_top_p(p: float, min_keep: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_top_p(p, min_keep)


def c_llama_sampler_init_min_p(p: float, min_keep: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_min_p(p, min_keep)


def llama_sampler_init_min_p(p: float, min_keep: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_min_p(p, min_keep)


def c_llama_sampler_init_temp(t: float) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_temp(t)


def llama_sampler_init_temp(t: float) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_temp(t)


def c_llama_sampler_sample(smpl: 'LlamaSamplerPointer', ctx: 'LlamaContextPointer', idx: int) -> Any:
    return llama.llama_sampler_sample(smpl, ctx, idx)


def llama_sampler_sample(smpl: 'LlamaSamplerPointer', ctx: 'LlamaContextPointer', idx: int) -> Any:
    return c_llama_sampler_sample(smpl, ctx, idx)


def c_llama_log_set(log_callback, user_data):
    return llama.llama_log_set(log_callback, user_data)


def llama_log_set(log_callback, user_data):
    return c_llama_log_set(log_callback, user_data)
