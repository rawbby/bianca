from bianca.bootstrap import *

__all__ = [
    "GgmlTensor",
    "PyGgmlTensor",
    "LlamaTokenData",
    "PyLlamaTokenData",
    "LlamaTokenDataArray",
    "PyLlamaTokenDataArray",
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
    "LlamaModelTensorOverride",
    "PyLlamaModelTensorOverride",
    "LlamaModelImatrixData",
    "PyLlamaModelImatrixData",
    "LlamaModelQuantizeParams",
    "PyLlamaModelQuantizeParams",
    "LlamaLogitBias",
    "PyLlamaLogitBias",
    "LlamaSamplerChainParams",
    "PyLlamaSamplerChainParams",
    "LlamaChatMessage",
    "PyLlamaChatMessage",
    "LlamaSamplerData",
    "PyLlamaSamplerData",
    "LlamaSamplerI",
    "PyLlamaSamplerI",
    "LlamaSampler",
    "PyLlamaSampler",
    "LlamaPerfContextData",
    "PyLlamaPerfContextData",
    "LlamaPerfSamplerData",
    "PyLlamaPerfSamplerData",
    "LlamaOptParams",
    "PyLlamaOptParams",
    "LlamaContextPointer",
    "LlamaSamplerSeqConfigPointer",
    "LlamaVocabPointer",
    "LlamaModelPointer",
    "LlamaModelQuantizeParamsPointer",
    "LlamaSamplerPointer",
    "LlamaPosPointer",
    "LlamaModelImatrixDataPointer",
    "LlamaLogitBiasPointer",
    "LlamaModelKvOverridePointer",
    "LlamaSamplerIPointer",
    "LlamaModelTensorBuftOverridePointer",
    "LlamaChatMessagePointer",
    "LlamaTokenPointer",
    "LlamaModelTensorOverridePointer",
    "LlamaSeqIdPointer",
    "LlamaTokenDataPointer",
    "LlamaAdapterLoraPointer",
    "LlamaTokenDataArrayPointer",
    "c_llama_flash_attn_type_name",
    "llama_flash_attn_type_name",
    "c_llama_model_default_params",
    "llama_model_default_params",
    "c_llama_context_default_params",
    "llama_context_default_params",
    "c_llama_sampler_chain_default_params",
    "llama_sampler_chain_default_params",
    "c_llama_model_quantize_default_params",
    "llama_model_quantize_default_params",
    "c_llama_backend_init",
    "llama_backend_init",
    "c_llama_backend_free",
    "llama_backend_free",
    "c_llama_numa_init",
    "llama_numa_init",
    "c_llama_attach_threadpool",
    "llama_attach_threadpool",
    "c_llama_detach_threadpool",
    "llama_detach_threadpool",
    "c_llama_model_init_from_user",
    "llama_model_init_from_user",
    "c_llama_load_model_from_file",
    "llama_load_model_from_file",
    "c_llama_model_load_from_file",
    "llama_model_load_from_file",
    "c_llama_model_load_from_file_ptr",
    "llama_model_load_from_file_ptr",
    "c_llama_model_load_from_splits",
    "llama_model_load_from_splits",
    "c_llama_model_save_to_file",
    "llama_model_save_to_file",
    "c_llama_free_model",
    "llama_free_model",
    "c_llama_model_free",
    "llama_model_free",
    "c_llama_init_from_model",
    "llama_init_from_model",
    "c_llama_new_context_with_model",
    "llama_new_context_with_model",
    "c_llama_free",
    "llama_free",
    "c_llama_time_us",
    "llama_time_us",
    "c_llama_max_devices",
    "llama_max_devices",
    "c_llama_max_parallel_sequences",
    "llama_max_parallel_sequences",
    "c_llama_max_tensor_buft_overrides",
    "llama_max_tensor_buft_overrides",
    "c_llama_supports_mmap",
    "llama_supports_mmap",
    "c_llama_supports_mlock",
    "llama_supports_mlock",
    "c_llama_supports_gpu_offload",
    "llama_supports_gpu_offload",
    "c_llama_supports_rpc",
    "llama_supports_rpc",
    "c_llama_n_ctx",
    "llama_n_ctx",
    "c_llama_n_ctx_seq",
    "llama_n_ctx_seq",
    "c_llama_n_batch",
    "llama_n_batch",
    "c_llama_n_ubatch",
    "llama_n_ubatch",
    "c_llama_n_seq_max",
    "llama_n_seq_max",
    "c_llama_n_rs_seq",
    "llama_n_rs_seq",
    "c_llama_n_ctx_train",
    "llama_n_ctx_train",
    "c_llama_n_embd",
    "llama_n_embd",
    "c_llama_n_layer",
    "llama_n_layer",
    "c_llama_n_head",
    "llama_n_head",
    "c_llama_n_vocab",
    "llama_n_vocab",
    "c_llama_get_model",
    "llama_get_model",
    "c_llama_get_memory",
    "llama_get_memory",
    "c_llama_pooling_type",
    "llama_pooling_type",
    "c_llama_model_get_vocab",
    "llama_model_get_vocab",
    "c_llama_model_rope_type",
    "llama_model_rope_type",
    "c_llama_model_n_ctx_train",
    "llama_model_n_ctx_train",
    "c_llama_model_n_embd",
    "llama_model_n_embd",
    "c_llama_model_n_embd_inp",
    "llama_model_n_embd_inp",
    "c_llama_model_n_embd_out",
    "llama_model_n_embd_out",
    "c_llama_model_n_layer",
    "llama_model_n_layer",
    "c_llama_model_n_head",
    "llama_model_n_head",
    "c_llama_model_n_head_kv",
    "llama_model_n_head_kv",
    "c_llama_model_n_swa",
    "llama_model_n_swa",
    "c_llama_model_rope_freq_scale_train",
    "llama_model_rope_freq_scale_train",
    "c_llama_model_n_cls_out",
    "llama_model_n_cls_out",
    "c_llama_model_cls_label",
    "llama_model_cls_label",
    "c_llama_vocab_type",
    "llama_vocab_type",
    "c_llama_vocab_n_tokens",
    "llama_vocab_n_tokens",
    "c_llama_model_meta_val_str",
    "llama_model_meta_val_str",
    "c_llama_model_meta_count",
    "llama_model_meta_count",
    "c_llama_model_meta_key_str",
    "llama_model_meta_key_str",
    "c_llama_model_meta_key_by_index",
    "llama_model_meta_key_by_index",
    "c_llama_model_meta_val_str_by_index",
    "llama_model_meta_val_str_by_index",
    "c_llama_model_desc",
    "llama_model_desc",
    "c_llama_model_size",
    "llama_model_size",
    "c_llama_model_chat_template",
    "llama_model_chat_template",
    "c_llama_model_n_params",
    "llama_model_n_params",
    "c_llama_model_has_encoder",
    "llama_model_has_encoder",
    "c_llama_model_has_decoder",
    "llama_model_has_decoder",
    "c_llama_model_decoder_start_token",
    "llama_model_decoder_start_token",
    "c_llama_model_is_recurrent",
    "llama_model_is_recurrent",
    "c_llama_model_is_hybrid",
    "llama_model_is_hybrid",
    "c_llama_model_is_diffusion",
    "llama_model_is_diffusion",
    "c_llama_model_quantize",
    "llama_model_quantize",
    "c_llama_adapter_lora_init",
    "llama_adapter_lora_init",
    "c_llama_adapter_meta_val_str",
    "llama_adapter_meta_val_str",
    "c_llama_adapter_meta_count",
    "llama_adapter_meta_count",
    "c_llama_adapter_meta_key_by_index",
    "llama_adapter_meta_key_by_index",
    "c_llama_adapter_meta_val_str_by_index",
    "llama_adapter_meta_val_str_by_index",
    "c_llama_adapter_lora_free",
    "llama_adapter_lora_free",
    "c_llama_adapter_get_alora_n_invocation_tokens",
    "llama_adapter_get_alora_n_invocation_tokens",
    "c_llama_adapter_get_alora_invocation_tokens",
    "llama_adapter_get_alora_invocation_tokens",
    "c_llama_set_adapters_lora",
    "llama_set_adapters_lora",
    "c_llama_set_adapter_cvec",
    "llama_set_adapter_cvec",
    "c_llama_memory_clear",
    "llama_memory_clear",
    "c_llama_memory_seq_rm",
    "llama_memory_seq_rm",
    "c_llama_memory_seq_cp",
    "llama_memory_seq_cp",
    "c_llama_memory_seq_keep",
    "llama_memory_seq_keep",
    "c_llama_memory_seq_add",
    "llama_memory_seq_add",
    "c_llama_memory_seq_div",
    "llama_memory_seq_div",
    "c_llama_memory_seq_pos_min",
    "llama_memory_seq_pos_min",
    "c_llama_memory_seq_pos_max",
    "llama_memory_seq_pos_max",
    "c_llama_memory_can_shift",
    "llama_memory_can_shift",
    "c_llama_state_get_size",
    "llama_state_get_size",
    "c_llama_get_state_size",
    "llama_get_state_size",
    "c_llama_state_get_data",
    "llama_state_get_data",
    "c_llama_copy_state_data",
    "llama_copy_state_data",
    "c_llama_state_set_data",
    "llama_state_set_data",
    "c_llama_set_state_data",
    "llama_set_state_data",
    "c_llama_state_load_file",
    "llama_state_load_file",
    "c_llama_load_session_file",
    "llama_load_session_file",
    "c_llama_state_save_file",
    "llama_state_save_file",
    "c_llama_save_session_file",
    "llama_save_session_file",
    "c_llama_state_seq_get_size",
    "llama_state_seq_get_size",
    "c_llama_state_seq_get_data",
    "llama_state_seq_get_data",
    "c_llama_state_seq_set_data",
    "llama_state_seq_set_data",
    "c_llama_state_seq_save_file",
    "llama_state_seq_save_file",
    "c_llama_state_seq_load_file",
    "llama_state_seq_load_file",
    "c_llama_state_seq_get_size_ext",
    "llama_state_seq_get_size_ext",
    "c_llama_state_seq_get_data_ext",
    "llama_state_seq_get_data_ext",
    "c_llama_state_seq_set_data_ext",
    "llama_state_seq_set_data_ext",
    "c_llama_batch_get_one",
    "llama_batch_get_one",
    "c_llama_batch_init",
    "llama_batch_init",
    "c_llama_batch_free",
    "llama_batch_free",
    "c_llama_encode",
    "llama_encode",
    "c_llama_decode",
    "llama_decode",
    "c_llama_set_n_threads",
    "llama_set_n_threads",
    "c_llama_n_threads",
    "llama_n_threads",
    "c_llama_n_threads_batch",
    "llama_n_threads_batch",
    "c_llama_set_embeddings",
    "llama_set_embeddings",
    "c_llama_set_causal_attn",
    "llama_set_causal_attn",
    "c_llama_set_warmup",
    "llama_set_warmup",
    "c_llama_set_abort_callback",
    "llama_set_abort_callback",
    "c_llama_synchronize",
    "llama_synchronize",
    "c_llama_get_logits",
    "llama_get_logits",
    "c_llama_get_logits_ith",
    "llama_get_logits_ith",
    "c_llama_get_embeddings",
    "llama_get_embeddings",
    "c_llama_get_embeddings_ith",
    "llama_get_embeddings_ith",
    "c_llama_get_embeddings_seq",
    "llama_get_embeddings_seq",
    "c_llama_get_sampled_token_ith",
    "llama_get_sampled_token_ith",
    "c_llama_get_sampled_probs_ith",
    "llama_get_sampled_probs_ith",
    "c_llama_get_sampled_probs_count_ith",
    "llama_get_sampled_probs_count_ith",
    "c_llama_get_sampled_logits_ith",
    "llama_get_sampled_logits_ith",
    "c_llama_get_sampled_logits_count_ith",
    "llama_get_sampled_logits_count_ith",
    "c_llama_get_sampled_candidates_ith",
    "llama_get_sampled_candidates_ith",
    "c_llama_get_sampled_candidates_count_ith",
    "llama_get_sampled_candidates_count_ith",
    "c_llama_vocab_get_text",
    "llama_vocab_get_text",
    "c_llama_vocab_get_score",
    "llama_vocab_get_score",
    "c_llama_vocab_get_attr",
    "llama_vocab_get_attr",
    "c_llama_vocab_is_eog",
    "llama_vocab_is_eog",
    "c_llama_vocab_is_control",
    "llama_vocab_is_control",
    "c_llama_vocab_bos",
    "llama_vocab_bos",
    "c_llama_vocab_eos",
    "llama_vocab_eos",
    "c_llama_vocab_eot",
    "llama_vocab_eot",
    "c_llama_vocab_sep",
    "llama_vocab_sep",
    "c_llama_vocab_nl",
    "llama_vocab_nl",
    "c_llama_vocab_pad",
    "llama_vocab_pad",
    "c_llama_vocab_mask",
    "llama_vocab_mask",
    "c_llama_vocab_get_add_bos",
    "llama_vocab_get_add_bos",
    "c_llama_vocab_get_add_eos",
    "llama_vocab_get_add_eos",
    "c_llama_vocab_get_add_sep",
    "llama_vocab_get_add_sep",
    "c_llama_vocab_fim_pre",
    "llama_vocab_fim_pre",
    "c_llama_vocab_fim_suf",
    "llama_vocab_fim_suf",
    "c_llama_vocab_fim_mid",
    "llama_vocab_fim_mid",
    "c_llama_vocab_fim_pad",
    "llama_vocab_fim_pad",
    "c_llama_vocab_fim_rep",
    "llama_vocab_fim_rep",
    "c_llama_vocab_fim_sep",
    "llama_vocab_fim_sep",
    "c_llama_token_get_text",
    "llama_token_get_text",
    "c_llama_token_get_score",
    "llama_token_get_score",
    "c_llama_token_get_attr",
    "llama_token_get_attr",
    "c_llama_token_is_eog",
    "llama_token_is_eog",
    "c_llama_token_is_control",
    "llama_token_is_control",
    "c_llama_token_bos",
    "llama_token_bos",
    "c_llama_token_eos",
    "llama_token_eos",
    "c_llama_token_eot",
    "llama_token_eot",
    "c_llama_token_cls",
    "llama_token_cls",
    "c_llama_token_sep",
    "llama_token_sep",
    "c_llama_token_nl",
    "llama_token_nl",
    "c_llama_token_pad",
    "llama_token_pad",
    "c_llama_add_bos_token",
    "llama_add_bos_token",
    "c_llama_add_eos_token",
    "llama_add_eos_token",
    "c_llama_token_fim_pre",
    "llama_token_fim_pre",
    "c_llama_token_fim_suf",
    "llama_token_fim_suf",
    "c_llama_token_fim_mid",
    "llama_token_fim_mid",
    "c_llama_token_fim_pad",
    "llama_token_fim_pad",
    "c_llama_token_fim_rep",
    "llama_token_fim_rep",
    "c_llama_token_fim_sep",
    "llama_token_fim_sep",
    "c_llama_vocab_cls",
    "llama_vocab_cls",
    "c_llama_tokenize",
    "llama_tokenize",
    "c_llama_token_to_piece",
    "llama_token_to_piece",
    "c_llama_detokenize",
    "llama_detokenize",
    "c_llama_chat_apply_template",
    "llama_chat_apply_template",
    "c_llama_chat_builtin_templates",
    "llama_chat_builtin_templates",
    "c_llama_set_sampler",
    "llama_set_sampler",
    "c_llama_sampler_init",
    "llama_sampler_init",
    "c_llama_sampler_name",
    "llama_sampler_name",
    "c_llama_sampler_accept",
    "llama_sampler_accept",
    "c_llama_sampler_apply",
    "llama_sampler_apply",
    "c_llama_sampler_reset",
    "llama_sampler_reset",
    "c_llama_sampler_clone",
    "llama_sampler_clone",
    "c_llama_sampler_free",
    "llama_sampler_free",
    "c_llama_sampler_chain_init",
    "llama_sampler_chain_init",
    "c_llama_sampler_chain_add",
    "llama_sampler_chain_add",
    "c_llama_sampler_chain_get",
    "llama_sampler_chain_get",
    "c_llama_sampler_chain_n",
    "llama_sampler_chain_n",
    "c_llama_sampler_chain_remove",
    "llama_sampler_chain_remove",
    "c_llama_sampler_init_greedy",
    "llama_sampler_init_greedy",
    "c_llama_sampler_init_dist",
    "llama_sampler_init_dist",
    "c_llama_sampler_init_top_k",
    "llama_sampler_init_top_k",
    "c_llama_sampler_init_top_p",
    "llama_sampler_init_top_p",
    "c_llama_sampler_init_min_p",
    "llama_sampler_init_min_p",
    "c_llama_sampler_init_typical",
    "llama_sampler_init_typical",
    "c_llama_sampler_init_temp",
    "llama_sampler_init_temp",
    "c_llama_sampler_init_temp_ext",
    "llama_sampler_init_temp_ext",
    "c_llama_sampler_init_xtc",
    "llama_sampler_init_xtc",
    "c_llama_sampler_init_top_n_sigma",
    "llama_sampler_init_top_n_sigma",
    "c_llama_sampler_init_mirostat",
    "llama_sampler_init_mirostat",
    "c_llama_sampler_init_mirostat_v2",
    "llama_sampler_init_mirostat_v2",
    "c_llama_sampler_init_grammar",
    "llama_sampler_init_grammar",
    "c_llama_sampler_init_grammar_lazy",
    "llama_sampler_init_grammar_lazy",
    "c_llama_sampler_init_grammar_lazy_patterns",
    "llama_sampler_init_grammar_lazy_patterns",
    "c_llama_sampler_init_penalties",
    "llama_sampler_init_penalties",
    "c_llama_sampler_init_dry",
    "llama_sampler_init_dry",
    "c_llama_sampler_init_adaptive_p",
    "llama_sampler_init_adaptive_p",
    "c_llama_sampler_init_logit_bias",
    "llama_sampler_init_logit_bias",
    "c_llama_sampler_init_infill",
    "llama_sampler_init_infill",
    "c_llama_sampler_get_seed",
    "llama_sampler_get_seed",
    "c_llama_sampler_sample",
    "llama_sampler_sample",
    "c_llama_split_path",
    "llama_split_path",
    "c_llama_split_prefix",
    "llama_split_prefix",
    "c_llama_print_system_info",
    "llama_print_system_info",
    "c_llama_log_get",
    "llama_log_get",
    "c_llama_log_set",
    "llama_log_set",
    "c_llama_perf_context",
    "llama_perf_context",
    "c_llama_perf_context_print",
    "llama_perf_context_print",
    "c_llama_perf_context_reset",
    "llama_perf_context_reset",
    "c_llama_perf_sampler",
    "llama_perf_sampler",
    "c_llama_perf_sampler_print",
    "llama_perf_sampler_print",
    "c_llama_perf_sampler_reset",
    "llama_perf_sampler_reset",
    "c_llama_opt_param_filter_all",
    "llama_opt_param_filter_all",
    "c_llama_opt_init",
    "llama_opt_init",
    "c_llama_opt_epoch",
    "llama_opt_epoch",
]

llama = ctypes.CDLL(LLAMA_LIB)


class GgmlBackendBuffer(ctypes.Structure):
    pass


class GgufContext(ctypes.Structure):
    pass


class LlamaAdapterLora(ctypes.Structure):
    pass


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


class GgmlTensor(ctypes.Structure):
    @property
    def py(self) -> 'PyGgmlTensor':
        return PyGgmlTensor(
            type=self.type,
            buffer=self.buffer,
            ne=self.ne,
            nb=self.nb,
            op=self.op,
            op_params=self.op_params,
            flags=self.flags,
            src=self.src,
            view_src=self.view_src,
            view_offs=self.view_offs,
            data=self.data,
            name=self.name,
            extra=self.extra,
            padding=self.padding,
        )

    @py.setter
    def py(self, value: 'PyGgmlTensor'):
        setattr(self, "type", value.c.type)
        setattr(self, "buffer", value.c.buffer)
        setattr(self, "ne", value.c.ne)
        setattr(self, "nb", value.c.nb)
        setattr(self, "op", value.c.op)
        setattr(self, "op_params", value.c.op_params)
        setattr(self, "flags", value.c.flags)
        setattr(self, "src", value.c.src)
        setattr(self, "view_src", value.c.view_src)
        setattr(self, "view_offs", value.c.view_offs)
        setattr(self, "data", value.c.data)
        setattr(self, "name", value.c.name)
        setattr(self, "extra", value.c.extra)
        setattr(self, "padding", value.c.padding)


class LlamaTokenData(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaTokenData':
        return PyLlamaTokenData(
            id=self.id,
            logit=self.logit,
            p=self.p,
        )

    @py.setter
    def py(self, value: 'PyLlamaTokenData'):
        setattr(self, "id", value.c.id)
        setattr(self, "logit", value.c.logit)
        setattr(self, "p", value.c.p)


class LlamaTokenDataArray(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaTokenDataArray':
        return PyLlamaTokenDataArray(
            data=self.data,
            size=self.size,
            selected=self.selected,
            sorted=self.sorted,
        )

    @py.setter
    def py(self, value: 'PyLlamaTokenDataArray'):
        setattr(self, "data", value.c.data)
        setattr(self, "size", value.c.size)
        setattr(self, "selected", value.c.selected)
        setattr(self, "sorted", value.c.sorted)


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


class LlamaModelTensorOverride(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaModelTensorOverride':
        return PyLlamaModelTensorOverride(
            pattern=self.pattern,
            type=self.type,
        )

    @py.setter
    def py(self, value: 'PyLlamaModelTensorOverride'):
        setattr(self, "pattern", value.c.pattern)
        setattr(self, "type", value.c.type)


class LlamaModelImatrixData(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaModelImatrixData':
        return PyLlamaModelImatrixData(
            name=self.name,
            data=self.data,
            size=self.size,
        )

    @py.setter
    def py(self, value: 'PyLlamaModelImatrixData'):
        setattr(self, "name", value.c.name)
        setattr(self, "data", value.c.data)
        setattr(self, "size", value.c.size)


class LlamaModelQuantizeParams(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaModelQuantizeParams':
        return PyLlamaModelQuantizeParams(
            nthread=self.nthread,
            ftype=self.ftype,
            output_tensor_type=self.output_tensor_type,
            token_embedding_type=self.token_embedding_type,
            allow_requantize=self.allow_requantize,
            quantize_output_tensor=self.quantize_output_tensor,
            only_copy=self.only_copy,
            pure=self.pure,
            keep_split=self.keep_split,
            dry_run=self.dry_run,
            imatrix=self.imatrix,
            kv_overrides=self.kv_overrides,
            tt_overrides=self.tt_overrides,
            prune_layers=self.prune_layers,
        )

    @py.setter
    def py(self, value: 'PyLlamaModelQuantizeParams'):
        setattr(self, "nthread", value.c.nthread)
        setattr(self, "ftype", value.c.ftype)
        setattr(self, "output_tensor_type", value.c.output_tensor_type)
        setattr(self, "token_embedding_type", value.c.token_embedding_type)
        setattr(self, "allow_requantize", value.c.allow_requantize)
        setattr(self, "quantize_output_tensor", value.c.quantize_output_tensor)
        setattr(self, "only_copy", value.c.only_copy)
        setattr(self, "pure", value.c.pure)
        setattr(self, "keep_split", value.c.keep_split)
        setattr(self, "dry_run", value.c.dry_run)
        setattr(self, "imatrix", value.c.imatrix)
        setattr(self, "kv_overrides", value.c.kv_overrides)
        setattr(self, "tt_overrides", value.c.tt_overrides)
        setattr(self, "prune_layers", value.c.prune_layers)


class LlamaLogitBias(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaLogitBias':
        return PyLlamaLogitBias(
            token=self.token,
            bias=self.bias,
        )

    @py.setter
    def py(self, value: 'PyLlamaLogitBias'):
        setattr(self, "token", value.c.token)
        setattr(self, "bias", value.c.bias)


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


class LlamaSamplerData(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaSamplerData':
        return PyLlamaSamplerData(
            logits=self.logits,
            probs=self.probs,
            sampled=self.sampled,
            candidates=self.candidates,
        )

    @py.setter
    def py(self, value: 'PyLlamaSamplerData'):
        setattr(self, "logits", value.c.logits)
        setattr(self, "probs", value.c.probs)
        setattr(self, "sampled", value.c.sampled)
        setattr(self, "candidates", value.c.candidates)


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


class LlamaPerfContextData(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaPerfContextData':
        return PyLlamaPerfContextData(
            t_start_ms=self.t_start_ms,
            t_load_ms=self.t_load_ms,
            t_p_eval_ms=self.t_p_eval_ms,
            t_eval_ms=self.t_eval_ms,
            n_p_eval=self.n_p_eval,
            n_eval=self.n_eval,
            n_reused=self.n_reused,
        )

    @py.setter
    def py(self, value: 'PyLlamaPerfContextData'):
        setattr(self, "t_start_ms", value.c.t_start_ms)
        setattr(self, "t_load_ms", value.c.t_load_ms)
        setattr(self, "t_p_eval_ms", value.c.t_p_eval_ms)
        setattr(self, "t_eval_ms", value.c.t_eval_ms)
        setattr(self, "n_p_eval", value.c.n_p_eval)
        setattr(self, "n_eval", value.c.n_eval)
        setattr(self, "n_reused", value.c.n_reused)


class LlamaPerfSamplerData(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaPerfSamplerData':
        return PyLlamaPerfSamplerData(
            t_sample_ms=self.t_sample_ms,
            n_sample=self.n_sample,
        )

    @py.setter
    def py(self, value: 'PyLlamaPerfSamplerData'):
        setattr(self, "t_sample_ms", value.c.t_sample_ms)
        setattr(self, "n_sample", value.c.n_sample)


class LlamaOptParams(ctypes.Structure):
    @property
    def py(self) -> 'PyLlamaOptParams':
        return PyLlamaOptParams(
            n_ctx_train=self.n_ctx_train,
            param_filter=self.param_filter,
            param_filter_ud=self.param_filter_ud,
            get_opt_pars=self.get_opt_pars,
            get_opt_pars_ud=self.get_opt_pars_ud,
            optimizer_type=self.optimizer_type,
        )

    @py.setter
    def py(self, value: 'PyLlamaOptParams'):
        setattr(self, "n_ctx_train", value.c.n_ctx_train)
        setattr(self, "param_filter", value.c.param_filter)
        setattr(self, "param_filter_ud", value.c.param_filter_ud)
        setattr(self, "get_opt_pars", value.c.get_opt_pars)
        setattr(self, "get_opt_pars_ud", value.c.get_opt_pars_ud)
        setattr(self, "optimizer_type", value.c.optimizer_type)


LlamaAdapterLoraPointer = ctypes.c_void_p
LlamaChatMessagePointer = ctypes.POINTER(LlamaChatMessage)
LlamaContextPointer = ctypes.c_void_p
LlamaLogitBiasPointer = ctypes.POINTER(LlamaLogitBias)
LlamaModelImatrixDataPointer = ctypes.POINTER(LlamaModelImatrixData)
LlamaModelKvOverridePointer = ctypes.POINTER(LlamaModelKvOverride)
LlamaModelPointer = ctypes.c_void_p
LlamaModelQuantizeParamsPointer = ctypes.POINTER(LlamaModelQuantizeParams)
LlamaModelTensorBuftOverridePointer = ctypes.POINTER(LlamaModelTensorBuftOverride)
LlamaModelTensorOverridePointer = ctypes.POINTER(LlamaModelTensorOverride)
LlamaPosPointer = ctypes.c_void_p
LlamaSamplerIPointer = ctypes.POINTER(LlamaSamplerI)
LlamaSamplerPointer = ctypes.POINTER(LlamaSampler)
LlamaSamplerSeqConfigPointer = ctypes.POINTER(LlamaSamplerSeqConfig)
LlamaSeqIdPointer = ctypes.c_void_p
LlamaTokenDataArrayPointer = ctypes.POINTER(LlamaTokenDataArray)
LlamaTokenDataPointer = ctypes.POINTER(LlamaTokenData)
LlamaTokenPointer = ctypes.c_void_p
LlamaVocabPointer = ctypes.c_void_p

GgmlTensor._fields_ = [
    ("type", ctypes.c_int32),
    ("buffer", ctypes.POINTER(GgmlBackendBuffer)),
    ("ne", (ctypes.c_int64 * 4)),
    ("nb", (ctypes.c_int * 4)),
    ("op", ctypes.c_int32),
    ("op_params", (ctypes.c_int32 * 16)),
    ("flags", ctypes.c_int32),
    ("src", (ctypes.POINTER(GgmlTensor) * 10)),
    ("view_src", ctypes.POINTER(GgmlTensor)),
    ("view_offs", ctypes.c_int),
    ("data", ctypes.c_void_p),
    ("name", (ctypes.c_char * 64)),
    ("extra", ctypes.c_void_p),
    ("padding", (ctypes.c_char * 8)),
]

LlamaTokenData._fields_ = [
    ("id", ctypes.c_void_p),
    ("logit", ctypes.c_float),
    ("p", ctypes.c_float),
]

LlamaTokenDataArray._fields_ = [
    ("data", LlamaTokenDataPointer),
    ("size", ctypes.c_size_t),
    ("selected", ctypes.c_int64),
    ("sorted", ctypes.c_bool),
]

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

LlamaModelTensorOverride._fields_ = [
    ("pattern", ctypes.c_char_p),
    ("type", ctypes.c_int32),
]

LlamaModelImatrixData._fields_ = [
    ("name", ctypes.c_char_p),
    ("data", ctypes.POINTER(ctypes.c_float)),
    ("size", ctypes.c_size_t),
]

LlamaModelQuantizeParams._fields_ = [
    ("nthread", ctypes.c_int32),
    ("ftype", ctypes.c_int32),
    ("output_tensor_type", ctypes.c_int32),
    ("token_embedding_type", ctypes.c_int32),
    ("allow_requantize", ctypes.c_bool),
    ("quantize_output_tensor", ctypes.c_bool),
    ("only_copy", ctypes.c_bool),
    ("pure", ctypes.c_bool),
    ("keep_split", ctypes.c_bool),
    ("dry_run", ctypes.c_bool),
    ("imatrix", LlamaModelImatrixDataPointer),
    ("kv_overrides", LlamaModelKvOverridePointer),
    ("tt_overrides", LlamaModelTensorOverridePointer),
    ("prune_layers", ctypes.POINTER(ctypes.c_int32)),
]

LlamaLogitBias._fields_ = [
    ("token", ctypes.c_void_p),
    ("bias", ctypes.c_float),
]

LlamaSamplerChainParams._fields_ = [
    ("no_perf", ctypes.c_bool),
]

LlamaChatMessage._fields_ = [
    ("role", ctypes.c_char_p),
    ("content", ctypes.c_char_p),
]

LlamaSamplerData._fields_ = [
    ("logits", ctypes.POINTER(GgmlTensor)),
    ("probs", ctypes.POINTER(GgmlTensor)),
    ("sampled", ctypes.POINTER(GgmlTensor)),
    ("candidates", ctypes.POINTER(GgmlTensor)),
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

LlamaPerfContextData._fields_ = [
    ("t_start_ms", ctypes.c_double),
    ("t_load_ms", ctypes.c_double),
    ("t_p_eval_ms", ctypes.c_double),
    ("t_eval_ms", ctypes.c_double),
    ("n_p_eval", ctypes.c_int32),
    ("n_eval", ctypes.c_int32),
    ("n_reused", ctypes.c_int32),
]

LlamaPerfSamplerData._fields_ = [
    ("t_sample_ms", ctypes.c_double),
    ("n_sample", ctypes.c_int32),
]

LlamaOptParams._fields_ = [
    ("n_ctx_train", ctypes.c_uint32),
    ("param_filter", ctypes.c_void_p),
    ("param_filter_ud", ctypes.c_void_p),
    ("get_opt_pars", ctypes.c_void_p),
    ("get_opt_pars_ud", ctypes.c_void_p),
    ("optimizer_type", ctypes.c_int32),
]

llama.llama_flash_attn_type_name.argtypes = [ctypes.c_int32]
llama.llama_flash_attn_type_name.restype = ctypes.c_char_p

llama.llama_model_default_params.argtypes = []
llama.llama_model_default_params.restype = LlamaModelParams

llama.llama_context_default_params.argtypes = []
llama.llama_context_default_params.restype = LlamaContextParams

llama.llama_sampler_chain_default_params.argtypes = []
llama.llama_sampler_chain_default_params.restype = LlamaSamplerChainParams

llama.llama_model_quantize_default_params.argtypes = []
llama.llama_model_quantize_default_params.restype = LlamaModelQuantizeParams

llama.llama_backend_init.argtypes = []
llama.llama_backend_init.restype = None

llama.llama_backend_free.argtypes = []
llama.llama_backend_free.restype = None

llama.llama_numa_init.argtypes = [ctypes.c_int32]
llama.llama_numa_init.restype = None

llama.llama_attach_threadpool.argtypes = [LlamaContextPointer, ctypes.c_void_p, ctypes.c_void_p]
llama.llama_attach_threadpool.restype = None

llama.llama_detach_threadpool.argtypes = [LlamaContextPointer]
llama.llama_detach_threadpool.restype = None

llama.llama_model_init_from_user.argtypes = [ctypes.POINTER(GgufContext), ctypes.c_void_p, ctypes.c_void_p,
                                             LlamaModelParams]
llama.llama_model_init_from_user.restype = LlamaModelPointer

llama.llama_load_model_from_file.argtypes = [ctypes.c_char_p, LlamaModelParams]
llama.llama_load_model_from_file.restype = LlamaModelPointer

llama.llama_model_load_from_file.argtypes = [ctypes.c_char_p, LlamaModelParams]
llama.llama_model_load_from_file.restype = LlamaModelPointer

llama.llama_model_load_from_file_ptr.argtypes = [ctypes.POINTER(ctypes.c_void_p), LlamaModelParams]
llama.llama_model_load_from_file_ptr.restype = LlamaModelPointer

llama.llama_model_load_from_splits.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.c_size_t, LlamaModelParams]
llama.llama_model_load_from_splits.restype = LlamaModelPointer

llama.llama_model_save_to_file.argtypes = [LlamaModelPointer, ctypes.c_char_p]
llama.llama_model_save_to_file.restype = None

llama.llama_free_model.argtypes = [LlamaModelPointer]
llama.llama_free_model.restype = None

llama.llama_model_free.argtypes = [LlamaModelPointer]
llama.llama_model_free.restype = None

llama.llama_init_from_model.argtypes = [LlamaModelPointer, LlamaContextParams]
llama.llama_init_from_model.restype = LlamaContextPointer

llama.llama_new_context_with_model.argtypes = [LlamaModelPointer, LlamaContextParams]
llama.llama_new_context_with_model.restype = LlamaContextPointer

llama.llama_free.argtypes = [LlamaContextPointer]
llama.llama_free.restype = None

llama.llama_time_us.argtypes = []
llama.llama_time_us.restype = ctypes.c_int64

llama.llama_max_devices.argtypes = []
llama.llama_max_devices.restype = ctypes.c_int

llama.llama_max_parallel_sequences.argtypes = []
llama.llama_max_parallel_sequences.restype = ctypes.c_int

llama.llama_max_tensor_buft_overrides.argtypes = []
llama.llama_max_tensor_buft_overrides.restype = ctypes.c_int

llama.llama_supports_mmap.argtypes = []
llama.llama_supports_mmap.restype = ctypes.c_int

llama.llama_supports_mlock.argtypes = []
llama.llama_supports_mlock.restype = ctypes.c_int

llama.llama_supports_gpu_offload.argtypes = []
llama.llama_supports_gpu_offload.restype = ctypes.c_int

llama.llama_supports_rpc.argtypes = []
llama.llama_supports_rpc.restype = ctypes.c_int

llama.llama_n_ctx.argtypes = [LlamaContextPointer]
llama.llama_n_ctx.restype = ctypes.c_uint32

llama.llama_n_ctx_seq.argtypes = [LlamaContextPointer]
llama.llama_n_ctx_seq.restype = ctypes.c_uint32

llama.llama_n_batch.argtypes = [LlamaContextPointer]
llama.llama_n_batch.restype = ctypes.c_uint32

llama.llama_n_ubatch.argtypes = [LlamaContextPointer]
llama.llama_n_ubatch.restype = ctypes.c_uint32

llama.llama_n_seq_max.argtypes = [LlamaContextPointer]
llama.llama_n_seq_max.restype = ctypes.c_uint32

llama.llama_n_rs_seq.argtypes = [LlamaContextPointer]
llama.llama_n_rs_seq.restype = ctypes.c_uint32

llama.llama_n_ctx_train.argtypes = [LlamaModelPointer]
llama.llama_n_ctx_train.restype = ctypes.c_int32

llama.llama_n_embd.argtypes = [LlamaModelPointer]
llama.llama_n_embd.restype = ctypes.c_int32

llama.llama_n_layer.argtypes = [LlamaModelPointer]
llama.llama_n_layer.restype = ctypes.c_int32

llama.llama_n_head.argtypes = [LlamaModelPointer]
llama.llama_n_head.restype = ctypes.c_int32

llama.llama_n_vocab.argtypes = [LlamaVocabPointer]
llama.llama_n_vocab.restype = ctypes.c_int32

llama.llama_get_model.argtypes = [LlamaContextPointer]
llama.llama_get_model.restype = LlamaModelPointer

llama.llama_get_memory.argtypes = [LlamaContextPointer]
llama.llama_get_memory.restype = ctypes.c_void_p

llama.llama_pooling_type.argtypes = [LlamaContextPointer]
llama.llama_pooling_type.restype = ctypes.c_int32

llama.llama_model_get_vocab.argtypes = [LlamaModelPointer]
llama.llama_model_get_vocab.restype = LlamaVocabPointer

llama.llama_model_rope_type.argtypes = [LlamaModelPointer]
llama.llama_model_rope_type.restype = ctypes.c_int32

llama.llama_model_n_ctx_train.argtypes = [LlamaModelPointer]
llama.llama_model_n_ctx_train.restype = ctypes.c_int32

llama.llama_model_n_embd.argtypes = [LlamaModelPointer]
llama.llama_model_n_embd.restype = ctypes.c_int32

llama.llama_model_n_embd_inp.argtypes = [LlamaModelPointer]
llama.llama_model_n_embd_inp.restype = ctypes.c_int32

llama.llama_model_n_embd_out.argtypes = [LlamaModelPointer]
llama.llama_model_n_embd_out.restype = ctypes.c_int32

llama.llama_model_n_layer.argtypes = [LlamaModelPointer]
llama.llama_model_n_layer.restype = ctypes.c_int32

llama.llama_model_n_head.argtypes = [LlamaModelPointer]
llama.llama_model_n_head.restype = ctypes.c_int32

llama.llama_model_n_head_kv.argtypes = [LlamaModelPointer]
llama.llama_model_n_head_kv.restype = ctypes.c_int32

llama.llama_model_n_swa.argtypes = [LlamaModelPointer]
llama.llama_model_n_swa.restype = ctypes.c_int32

llama.llama_model_rope_freq_scale_train.argtypes = [LlamaModelPointer]
llama.llama_model_rope_freq_scale_train.restype = ctypes.c_float

llama.llama_model_n_cls_out.argtypes = [LlamaModelPointer]
llama.llama_model_n_cls_out.restype = ctypes.c_uint32

llama.llama_model_cls_label.argtypes = [LlamaModelPointer, ctypes.c_uint32]
llama.llama_model_cls_label.restype = ctypes.c_char_p

llama.llama_vocab_type.argtypes = [LlamaVocabPointer]
llama.llama_vocab_type.restype = ctypes.c_int32

llama.llama_vocab_n_tokens.argtypes = [LlamaVocabPointer]
llama.llama_vocab_n_tokens.restype = ctypes.c_int32

llama.llama_model_meta_val_str.argtypes = [LlamaModelPointer, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
llama.llama_model_meta_val_str.restype = ctypes.c_int32

llama.llama_model_meta_count.argtypes = [LlamaModelPointer]
llama.llama_model_meta_count.restype = ctypes.c_int32

llama.llama_model_meta_key_str.argtypes = [ctypes.c_int32]
llama.llama_model_meta_key_str.restype = ctypes.c_char_p

llama.llama_model_meta_key_by_index.argtypes = [LlamaModelPointer, ctypes.c_int32, ctypes.c_char_p, ctypes.c_size_t]
llama.llama_model_meta_key_by_index.restype = ctypes.c_int32

llama.llama_model_meta_val_str_by_index.argtypes = [LlamaModelPointer, ctypes.c_int32, ctypes.c_char_p, ctypes.c_size_t]
llama.llama_model_meta_val_str_by_index.restype = ctypes.c_int32

llama.llama_model_desc.argtypes = [LlamaModelPointer, ctypes.c_char_p, ctypes.c_size_t]
llama.llama_model_desc.restype = ctypes.c_int32

llama.llama_model_size.argtypes = [LlamaModelPointer]
llama.llama_model_size.restype = ctypes.c_uint64

llama.llama_model_chat_template.argtypes = [LlamaModelPointer, ctypes.c_char_p]
llama.llama_model_chat_template.restype = ctypes.c_char_p

llama.llama_model_n_params.argtypes = [LlamaModelPointer]
llama.llama_model_n_params.restype = ctypes.c_uint64

llama.llama_model_has_encoder.argtypes = [LlamaModelPointer]
llama.llama_model_has_encoder.restype = ctypes.c_int

llama.llama_model_has_decoder.argtypes = [LlamaModelPointer]
llama.llama_model_has_decoder.restype = ctypes.c_int

llama.llama_model_decoder_start_token.argtypes = [LlamaModelPointer]
llama.llama_model_decoder_start_token.restype = ctypes.c_void_p

llama.llama_model_is_recurrent.argtypes = [LlamaModelPointer]
llama.llama_model_is_recurrent.restype = ctypes.c_int

llama.llama_model_is_hybrid.argtypes = [LlamaModelPointer]
llama.llama_model_is_hybrid.restype = ctypes.c_int

llama.llama_model_is_diffusion.argtypes = [LlamaModelPointer]
llama.llama_model_is_diffusion.restype = ctypes.c_int

llama.llama_model_quantize.argtypes = [ctypes.c_char_p, ctypes.c_char_p, LlamaModelQuantizeParamsPointer]
llama.llama_model_quantize.restype = ctypes.c_uint32

llama.llama_adapter_lora_init.argtypes = [LlamaModelPointer, ctypes.c_char_p]
llama.llama_adapter_lora_init.restype = LlamaAdapterLoraPointer

llama.llama_adapter_meta_val_str.argtypes = [LlamaAdapterLoraPointer, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
llama.llama_adapter_meta_val_str.restype = ctypes.c_int32

llama.llama_adapter_meta_count.argtypes = [LlamaAdapterLoraPointer]
llama.llama_adapter_meta_count.restype = ctypes.c_int32

llama.llama_adapter_meta_key_by_index.argtypes = [LlamaAdapterLoraPointer, ctypes.c_int32, ctypes.c_char_p,
                                                  ctypes.c_size_t]
llama.llama_adapter_meta_key_by_index.restype = ctypes.c_int32

llama.llama_adapter_meta_val_str_by_index.argtypes = [LlamaAdapterLoraPointer, ctypes.c_int32, ctypes.c_char_p,
                                                      ctypes.c_size_t]
llama.llama_adapter_meta_val_str_by_index.restype = ctypes.c_int32

llama.llama_adapter_lora_free.argtypes = [LlamaAdapterLoraPointer]
llama.llama_adapter_lora_free.restype = None

llama.llama_adapter_get_alora_n_invocation_tokens.argtypes = [LlamaAdapterLoraPointer]
llama.llama_adapter_get_alora_n_invocation_tokens.restype = ctypes.c_uint64

llama.llama_adapter_get_alora_invocation_tokens.argtypes = [LlamaAdapterLoraPointer]
llama.llama_adapter_get_alora_invocation_tokens.restype = LlamaTokenPointer

llama.llama_set_adapters_lora.argtypes = [LlamaContextPointer, ctypes.POINTER(LlamaAdapterLoraPointer), ctypes.c_size_t,
                                          ctypes.POINTER(ctypes.c_float)]
llama.llama_set_adapters_lora.restype = ctypes.c_int32

llama.llama_set_adapter_cvec.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_float), ctypes.c_size_t,
                                         ctypes.c_int32, ctypes.c_int32, ctypes.c_int32]
llama.llama_set_adapter_cvec.restype = ctypes.c_int32

llama.llama_memory_clear.argtypes = [ctypes.c_void_p, ctypes.c_bool]
llama.llama_memory_clear.restype = None

llama.llama_memory_seq_rm.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
llama.llama_memory_seq_rm.restype = ctypes.c_int

llama.llama_memory_seq_cp.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                                      ctypes.c_void_p]
llama.llama_memory_seq_cp.restype = None

llama.llama_memory_seq_keep.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
llama.llama_memory_seq_keep.restype = None

llama.llama_memory_seq_add.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                                       ctypes.c_void_p]
llama.llama_memory_seq_add.restype = None

llama.llama_memory_seq_div.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
llama.llama_memory_seq_div.restype = None

llama.llama_memory_seq_pos_min.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
llama.llama_memory_seq_pos_min.restype = ctypes.c_void_p

llama.llama_memory_seq_pos_max.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
llama.llama_memory_seq_pos_max.restype = ctypes.c_void_p

llama.llama_memory_can_shift.argtypes = [ctypes.c_void_p]
llama.llama_memory_can_shift.restype = ctypes.c_int

llama.llama_state_get_size.argtypes = [LlamaContextPointer]
llama.llama_state_get_size.restype = ctypes.c_int

llama.llama_get_state_size.argtypes = [LlamaContextPointer]
llama.llama_get_state_size.restype = ctypes.c_int

llama.llama_state_get_data.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t]
llama.llama_state_get_data.restype = ctypes.c_int

llama.llama_copy_state_data.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8)]
llama.llama_copy_state_data.restype = ctypes.c_int

llama.llama_state_set_data.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t]
llama.llama_state_set_data.restype = ctypes.c_int

llama.llama_set_state_data.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8)]
llama.llama_set_state_data.restype = ctypes.c_int

llama.llama_state_load_file.argtypes = [LlamaContextPointer, ctypes.c_char_p, LlamaTokenPointer, ctypes.c_size_t,
                                        ctypes.POINTER(ctypes.c_size_t)]
llama.llama_state_load_file.restype = ctypes.c_int

llama.llama_load_session_file.argtypes = [LlamaContextPointer, ctypes.c_char_p, LlamaTokenPointer, ctypes.c_size_t,
                                          ctypes.POINTER(ctypes.c_size_t)]
llama.llama_load_session_file.restype = ctypes.c_int

llama.llama_state_save_file.argtypes = [LlamaContextPointer, ctypes.c_char_p, LlamaTokenPointer, ctypes.c_size_t]
llama.llama_state_save_file.restype = ctypes.c_int

llama.llama_save_session_file.argtypes = [LlamaContextPointer, ctypes.c_char_p, LlamaTokenPointer, ctypes.c_size_t]
llama.llama_save_session_file.restype = ctypes.c_int

llama.llama_state_seq_get_size.argtypes = [LlamaContextPointer, ctypes.c_void_p]
llama.llama_state_seq_get_size.restype = ctypes.c_int

llama.llama_state_seq_get_data.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t,
                                           ctypes.c_void_p]
llama.llama_state_seq_get_data.restype = ctypes.c_int

llama.llama_state_seq_set_data.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t,
                                           ctypes.c_void_p]
llama.llama_state_seq_set_data.restype = ctypes.c_int

llama.llama_state_seq_save_file.argtypes = [LlamaContextPointer, ctypes.c_char_p, ctypes.c_void_p, LlamaTokenPointer,
                                            ctypes.c_size_t]
llama.llama_state_seq_save_file.restype = ctypes.c_int

llama.llama_state_seq_load_file.argtypes = [LlamaContextPointer, ctypes.c_char_p, ctypes.c_void_p, LlamaTokenPointer,
                                            ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
llama.llama_state_seq_load_file.restype = ctypes.c_int

llama.llama_state_seq_get_size_ext.argtypes = [LlamaContextPointer, ctypes.c_void_p, ctypes.c_void_p]
llama.llama_state_seq_get_size_ext.restype = ctypes.c_int

llama.llama_state_seq_get_data_ext.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t,
                                               ctypes.c_void_p, ctypes.c_void_p]
llama.llama_state_seq_get_data_ext.restype = ctypes.c_int

llama.llama_state_seq_set_data_ext.argtypes = [LlamaContextPointer, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t,
                                               ctypes.c_void_p, ctypes.c_void_p]
llama.llama_state_seq_set_data_ext.restype = ctypes.c_int

llama.llama_batch_get_one.argtypes = [LlamaTokenPointer, ctypes.c_int32]
llama.llama_batch_get_one.restype = LlamaBatch

llama.llama_batch_init.argtypes = [ctypes.c_int32, ctypes.c_int32, ctypes.c_int32]
llama.llama_batch_init.restype = LlamaBatch

llama.llama_batch_free.argtypes = [LlamaBatch]
llama.llama_batch_free.restype = None

llama.llama_encode.argtypes = [LlamaContextPointer, LlamaBatch]
llama.llama_encode.restype = ctypes.c_int32

llama.llama_decode.argtypes = [LlamaContextPointer, LlamaBatch]
llama.llama_decode.restype = ctypes.c_int32

llama.llama_set_n_threads.argtypes = [LlamaContextPointer, ctypes.c_int32, ctypes.c_int32]
llama.llama_set_n_threads.restype = None

llama.llama_n_threads.argtypes = [LlamaContextPointer]
llama.llama_n_threads.restype = ctypes.c_int32

llama.llama_n_threads_batch.argtypes = [LlamaContextPointer]
llama.llama_n_threads_batch.restype = ctypes.c_int32

llama.llama_set_embeddings.argtypes = [LlamaContextPointer, ctypes.c_bool]
llama.llama_set_embeddings.restype = None

llama.llama_set_causal_attn.argtypes = [LlamaContextPointer, ctypes.c_bool]
llama.llama_set_causal_attn.restype = None

llama.llama_set_warmup.argtypes = [LlamaContextPointer, ctypes.c_bool]
llama.llama_set_warmup.restype = None

llama.llama_set_abort_callback.argtypes = [LlamaContextPointer, ctypes.c_int, ctypes.c_void_p]
llama.llama_set_abort_callback.restype = None

llama.llama_synchronize.argtypes = [LlamaContextPointer]
llama.llama_synchronize.restype = None

llama.llama_get_logits.argtypes = [LlamaContextPointer]
llama.llama_get_logits.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_logits_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_logits_ith.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_embeddings.argtypes = [LlamaContextPointer]
llama.llama_get_embeddings.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_embeddings_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_embeddings_ith.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_embeddings_seq.argtypes = [LlamaContextPointer, ctypes.c_void_p]
llama.llama_get_embeddings_seq.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_sampled_token_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_token_ith.restype = ctypes.c_void_p

llama.llama_get_sampled_probs_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_probs_ith.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_sampled_probs_count_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_probs_count_ith.restype = ctypes.c_uint32

llama.llama_get_sampled_logits_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_logits_ith.restype = ctypes.POINTER(ctypes.c_float)

llama.llama_get_sampled_logits_count_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_logits_count_ith.restype = ctypes.c_uint32

llama.llama_get_sampled_candidates_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_candidates_ith.restype = LlamaTokenPointer

llama.llama_get_sampled_candidates_count_ith.argtypes = [LlamaContextPointer, ctypes.c_int32]
llama.llama_get_sampled_candidates_count_ith.restype = ctypes.c_uint32

llama.llama_vocab_get_text.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_vocab_get_text.restype = ctypes.c_char_p

llama.llama_vocab_get_score.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_vocab_get_score.restype = ctypes.c_float

llama.llama_vocab_get_attr.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_vocab_get_attr.restype = ctypes.c_int32

llama.llama_vocab_is_eog.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_vocab_is_eog.restype = ctypes.c_int

llama.llama_vocab_is_control.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_vocab_is_control.restype = ctypes.c_int

llama.llama_vocab_bos.argtypes = [LlamaVocabPointer]
llama.llama_vocab_bos.restype = ctypes.c_void_p

llama.llama_vocab_eos.argtypes = [LlamaVocabPointer]
llama.llama_vocab_eos.restype = ctypes.c_void_p

llama.llama_vocab_eot.argtypes = [LlamaVocabPointer]
llama.llama_vocab_eot.restype = ctypes.c_void_p

llama.llama_vocab_sep.argtypes = [LlamaVocabPointer]
llama.llama_vocab_sep.restype = ctypes.c_void_p

llama.llama_vocab_nl.argtypes = [LlamaVocabPointer]
llama.llama_vocab_nl.restype = ctypes.c_void_p

llama.llama_vocab_pad.argtypes = [LlamaVocabPointer]
llama.llama_vocab_pad.restype = ctypes.c_void_p

llama.llama_vocab_mask.argtypes = [LlamaVocabPointer]
llama.llama_vocab_mask.restype = ctypes.c_void_p

llama.llama_vocab_get_add_bos.argtypes = [LlamaVocabPointer]
llama.llama_vocab_get_add_bos.restype = ctypes.c_int

llama.llama_vocab_get_add_eos.argtypes = [LlamaVocabPointer]
llama.llama_vocab_get_add_eos.restype = ctypes.c_int

llama.llama_vocab_get_add_sep.argtypes = [LlamaVocabPointer]
llama.llama_vocab_get_add_sep.restype = ctypes.c_int

llama.llama_vocab_fim_pre.argtypes = [LlamaVocabPointer]
llama.llama_vocab_fim_pre.restype = ctypes.c_void_p

llama.llama_vocab_fim_suf.argtypes = [LlamaVocabPointer]
llama.llama_vocab_fim_suf.restype = ctypes.c_void_p

llama.llama_vocab_fim_mid.argtypes = [LlamaVocabPointer]
llama.llama_vocab_fim_mid.restype = ctypes.c_void_p

llama.llama_vocab_fim_pad.argtypes = [LlamaVocabPointer]
llama.llama_vocab_fim_pad.restype = ctypes.c_void_p

llama.llama_vocab_fim_rep.argtypes = [LlamaVocabPointer]
llama.llama_vocab_fim_rep.restype = ctypes.c_void_p

llama.llama_vocab_fim_sep.argtypes = [LlamaVocabPointer]
llama.llama_vocab_fim_sep.restype = ctypes.c_void_p

llama.llama_token_get_text.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_token_get_text.restype = ctypes.c_char_p

llama.llama_token_get_score.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_token_get_score.restype = ctypes.c_float

llama.llama_token_get_attr.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_token_get_attr.restype = ctypes.c_int32

llama.llama_token_is_eog.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_token_is_eog.restype = ctypes.c_int

llama.llama_token_is_control.argtypes = [LlamaVocabPointer, ctypes.c_void_p]
llama.llama_token_is_control.restype = ctypes.c_int

llama.llama_token_bos.argtypes = [LlamaVocabPointer]
llama.llama_token_bos.restype = ctypes.c_void_p

llama.llama_token_eos.argtypes = [LlamaVocabPointer]
llama.llama_token_eos.restype = ctypes.c_void_p

llama.llama_token_eot.argtypes = [LlamaVocabPointer]
llama.llama_token_eot.restype = ctypes.c_void_p

llama.llama_token_cls.argtypes = [LlamaVocabPointer]
llama.llama_token_cls.restype = ctypes.c_void_p

llama.llama_token_sep.argtypes = [LlamaVocabPointer]
llama.llama_token_sep.restype = ctypes.c_void_p

llama.llama_token_nl.argtypes = [LlamaVocabPointer]
llama.llama_token_nl.restype = ctypes.c_void_p

llama.llama_token_pad.argtypes = [LlamaVocabPointer]
llama.llama_token_pad.restype = ctypes.c_void_p

llama.llama_add_bos_token.argtypes = [LlamaVocabPointer]
llama.llama_add_bos_token.restype = ctypes.c_int

llama.llama_add_eos_token.argtypes = [LlamaVocabPointer]
llama.llama_add_eos_token.restype = ctypes.c_int

llama.llama_token_fim_pre.argtypes = [LlamaVocabPointer]
llama.llama_token_fim_pre.restype = ctypes.c_void_p

llama.llama_token_fim_suf.argtypes = [LlamaVocabPointer]
llama.llama_token_fim_suf.restype = ctypes.c_void_p

llama.llama_token_fim_mid.argtypes = [LlamaVocabPointer]
llama.llama_token_fim_mid.restype = ctypes.c_void_p

llama.llama_token_fim_pad.argtypes = [LlamaVocabPointer]
llama.llama_token_fim_pad.restype = ctypes.c_void_p

llama.llama_token_fim_rep.argtypes = [LlamaVocabPointer]
llama.llama_token_fim_rep.restype = ctypes.c_void_p

llama.llama_token_fim_sep.argtypes = [LlamaVocabPointer]
llama.llama_token_fim_sep.restype = ctypes.c_void_p

llama.llama_vocab_cls.argtypes = [LlamaVocabPointer]
llama.llama_vocab_cls.restype = ctypes.c_void_p

llama.llama_tokenize.argtypes = [LlamaVocabPointer, ctypes.c_char_p, ctypes.c_int32, LlamaTokenPointer, ctypes.c_int32,
                                 ctypes.c_bool, ctypes.c_bool]
llama.llama_tokenize.restype = ctypes.c_int32

llama.llama_token_to_piece.argtypes = [LlamaVocabPointer, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int32,
                                       ctypes.c_int32, ctypes.c_bool]
llama.llama_token_to_piece.restype = ctypes.c_int32

llama.llama_detokenize.argtypes = [LlamaVocabPointer, LlamaTokenPointer, ctypes.c_int32, ctypes.c_char_p,
                                   ctypes.c_int32, ctypes.c_bool, ctypes.c_bool]
llama.llama_detokenize.restype = ctypes.c_int32

llama.llama_chat_apply_template.argtypes = [ctypes.c_char_p, LlamaChatMessagePointer, ctypes.c_size_t, ctypes.c_bool,
                                            ctypes.c_char_p, ctypes.c_int32]
llama.llama_chat_apply_template.restype = ctypes.c_int32

llama.llama_chat_builtin_templates.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.c_size_t]
llama.llama_chat_builtin_templates.restype = ctypes.c_int32

llama.llama_set_sampler.argtypes = [LlamaContextPointer, ctypes.c_void_p, LlamaSamplerPointer]
llama.llama_set_sampler.restype = ctypes.c_int

llama.llama_sampler_init.argtypes = [LlamaSamplerIPointer, ctypes.c_void_p]
llama.llama_sampler_init.restype = LlamaSamplerPointer

llama.llama_sampler_name.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_name.restype = ctypes.c_char_p

llama.llama_sampler_accept.argtypes = [LlamaSamplerPointer, ctypes.c_void_p]
llama.llama_sampler_accept.restype = None

llama.llama_sampler_apply.argtypes = [LlamaSamplerPointer, LlamaTokenDataArrayPointer]
llama.llama_sampler_apply.restype = None

llama.llama_sampler_reset.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_reset.restype = None

llama.llama_sampler_clone.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_clone.restype = LlamaSamplerPointer

llama.llama_sampler_free.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_free.restype = None

llama.llama_sampler_chain_init.argtypes = [LlamaSamplerChainParams]
llama.llama_sampler_chain_init.restype = LlamaSamplerPointer

llama.llama_sampler_chain_add.argtypes = [LlamaSamplerPointer, LlamaSamplerPointer]
llama.llama_sampler_chain_add.restype = None

llama.llama_sampler_chain_get.argtypes = [LlamaSamplerPointer, ctypes.c_int32]
llama.llama_sampler_chain_get.restype = LlamaSamplerPointer

llama.llama_sampler_chain_n.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_chain_n.restype = ctypes.c_int

llama.llama_sampler_chain_remove.argtypes = [LlamaSamplerPointer, ctypes.c_int32]
llama.llama_sampler_chain_remove.restype = LlamaSamplerPointer

llama.llama_sampler_init_greedy.argtypes = []
llama.llama_sampler_init_greedy.restype = LlamaSamplerPointer

llama.llama_sampler_init_dist.argtypes = [ctypes.c_uint32]
llama.llama_sampler_init_dist.restype = LlamaSamplerPointer

llama.llama_sampler_init_top_k.argtypes = [ctypes.c_int32]
llama.llama_sampler_init_top_k.restype = LlamaSamplerPointer

llama.llama_sampler_init_top_p.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_top_p.restype = LlamaSamplerPointer

llama.llama_sampler_init_min_p.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_min_p.restype = LlamaSamplerPointer

llama.llama_sampler_init_typical.argtypes = [ctypes.c_float, ctypes.c_size_t]
llama.llama_sampler_init_typical.restype = LlamaSamplerPointer

llama.llama_sampler_init_temp.argtypes = [ctypes.c_float]
llama.llama_sampler_init_temp.restype = LlamaSamplerPointer

llama.llama_sampler_init_temp_ext.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float]
llama.llama_sampler_init_temp_ext.restype = LlamaSamplerPointer

llama.llama_sampler_init_xtc.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_size_t, ctypes.c_uint32]
llama.llama_sampler_init_xtc.restype = LlamaSamplerPointer

llama.llama_sampler_init_top_n_sigma.argtypes = [ctypes.c_float]
llama.llama_sampler_init_top_n_sigma.restype = LlamaSamplerPointer

llama.llama_sampler_init_mirostat.argtypes = [ctypes.c_int32, ctypes.c_uint32, ctypes.c_float, ctypes.c_float,
                                              ctypes.c_int32]
llama.llama_sampler_init_mirostat.restype = LlamaSamplerPointer

llama.llama_sampler_init_mirostat_v2.argtypes = [ctypes.c_uint32, ctypes.c_float, ctypes.c_float]
llama.llama_sampler_init_mirostat_v2.restype = LlamaSamplerPointer

llama.llama_sampler_init_grammar.argtypes = [LlamaVocabPointer, ctypes.c_char_p, ctypes.c_char_p]
llama.llama_sampler_init_grammar.restype = LlamaSamplerPointer

llama.llama_sampler_init_grammar_lazy.argtypes = [LlamaVocabPointer, ctypes.c_char_p, ctypes.c_char_p,
                                                  ctypes.POINTER(ctypes.c_char_p), ctypes.c_size_t, LlamaTokenPointer,
                                                  ctypes.c_size_t]
llama.llama_sampler_init_grammar_lazy.restype = LlamaSamplerPointer

llama.llama_sampler_init_grammar_lazy_patterns.argtypes = [LlamaVocabPointer, ctypes.c_char_p, ctypes.c_char_p,
                                                           ctypes.POINTER(ctypes.c_char_p), ctypes.c_size_t,
                                                           LlamaTokenPointer, ctypes.c_size_t]
llama.llama_sampler_init_grammar_lazy_patterns.restype = LlamaSamplerPointer

llama.llama_sampler_init_penalties.argtypes = [ctypes.c_int32, ctypes.c_float, ctypes.c_float, ctypes.c_float]
llama.llama_sampler_init_penalties.restype = LlamaSamplerPointer

llama.llama_sampler_init_dry.argtypes = [LlamaVocabPointer, ctypes.c_int32, ctypes.c_float, ctypes.c_float,
                                         ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char_p),
                                         ctypes.c_size_t]
llama.llama_sampler_init_dry.restype = LlamaSamplerPointer

llama.llama_sampler_init_adaptive_p.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_uint32]
llama.llama_sampler_init_adaptive_p.restype = LlamaSamplerPointer

llama.llama_sampler_init_logit_bias.argtypes = [ctypes.c_int32, ctypes.c_int32, LlamaLogitBiasPointer]
llama.llama_sampler_init_logit_bias.restype = LlamaSamplerPointer

llama.llama_sampler_init_infill.argtypes = [LlamaVocabPointer]
llama.llama_sampler_init_infill.restype = LlamaSamplerPointer

llama.llama_sampler_get_seed.argtypes = [LlamaSamplerPointer]
llama.llama_sampler_get_seed.restype = ctypes.c_uint32

llama.llama_sampler_sample.argtypes = [LlamaSamplerPointer, LlamaContextPointer, ctypes.c_int32]
llama.llama_sampler_sample.restype = ctypes.c_void_p

llama.llama_split_path.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_int32, ctypes.c_int32]
llama.llama_split_path.restype = ctypes.c_int32

llama.llama_split_prefix.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_int32, ctypes.c_int32]
llama.llama_split_prefix.restype = ctypes.c_int32

llama.llama_print_system_info.argtypes = []
llama.llama_print_system_info.restype = ctypes.c_char_p

llama.llama_log_get.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))]
llama.llama_log_get.restype = None

llama.llama_log_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
llama.llama_log_set.restype = None

llama.llama_perf_context.argtypes = [LlamaContextPointer]
llama.llama_perf_context.restype = LlamaPerfContextData

llama.llama_perf_context_print.argtypes = [LlamaContextPointer]
llama.llama_perf_context_print.restype = None

llama.llama_perf_context_reset.argtypes = [LlamaContextPointer]
llama.llama_perf_context_reset.restype = None

llama.llama_perf_sampler.argtypes = [LlamaSamplerPointer]
llama.llama_perf_sampler.restype = LlamaPerfSamplerData

llama.llama_perf_sampler_print.argtypes = [LlamaSamplerPointer]
llama.llama_perf_sampler_print.restype = None

llama.llama_perf_sampler_reset.argtypes = [LlamaSamplerPointer]
llama.llama_perf_sampler_reset.restype = None

llama.llama_opt_param_filter_all.argtypes = [ctypes.POINTER(GgmlTensor), ctypes.c_void_p]
llama.llama_opt_param_filter_all.restype = ctypes.c_int

llama.llama_opt_init.argtypes = [LlamaContextPointer, LlamaModelPointer, LlamaOptParams]
llama.llama_opt_init.restype = None

llama.llama_opt_epoch.argtypes = [LlamaContextPointer, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                                  ctypes.c_int64, ctypes.c_void_p, ctypes.c_void_p]
llama.llama_opt_epoch.restype = None


class PyGgmlTensor:
    def __init__(self, type=None, buffer=None, ne=None, nb=None, op=None, op_params=None, flags=None, src=None,
                 view_src=None, view_offs=None, data=None, name=None, extra=None, padding=None):
        self.type = type
        self.buffer = buffer
        self.ne = ne
        self.nb = nb
        self.op = op
        self.op_params = op_params
        self.flags = flags
        self.src = src
        self.view_src = view_src
        self.view_offs = view_offs
        self.data = data
        self.name = name
        self.extra = extra
        self.padding = padding

    @property
    def c(self) -> 'GgmlTensor':
        c_obj = GgmlTensor()
        if self.type is not None:
            c_obj.type = self.type
        if self.buffer is not None:
            c_obj.buffer = self.buffer
        if self.ne is not None:
            c_obj.ne = self.ne
        if self.nb is not None:
            c_obj.nb = self.nb
        if self.op is not None:
            c_obj.op = self.op
        if self.op_params is not None:
            c_obj.op_params = self.op_params
        if self.flags is not None:
            c_obj.flags = self.flags
        if self.src is not None:
            c_obj.src = self.src
        if self.view_src is not None:
            c_obj.view_src = self.view_src
        if self.view_offs is not None:
            c_obj.view_offs = self.view_offs
        if self.data is not None:
            c_obj.data = self.data
        if self.name is not None:
            c_obj.name = self.name
        if self.extra is not None:
            c_obj.extra = self.extra
        if self.padding is not None:
            c_obj.padding = self.padding
        return c_obj

    @c.setter
    def c(self, value: 'GgmlTensor'):
        py_obj = value.py
        self.type = py_obj.type
        self.buffer = py_obj.buffer
        self.ne = py_obj.ne
        self.nb = py_obj.nb
        self.op = py_obj.op
        self.op_params = py_obj.op_params
        self.flags = py_obj.flags
        self.src = py_obj.src
        self.view_src = py_obj.view_src
        self.view_offs = py_obj.view_offs
        self.data = py_obj.data
        self.name = py_obj.name
        self.extra = py_obj.extra
        self.padding = py_obj.padding


class PyLlamaTokenData:
    def __init__(self, id=None, logit=None, p=None):
        self.id = id
        self.logit = logit
        self.p = p

    @property
    def c(self) -> 'LlamaTokenData':
        c_obj = LlamaTokenData()
        if self.id is not None:
            c_obj.id = self.id
        if self.logit is not None:
            c_obj.logit = self.logit
        if self.p is not None:
            c_obj.p = self.p
        return c_obj

    @c.setter
    def c(self, value: 'LlamaTokenData'):
        py_obj = value.py
        self.id = py_obj.id
        self.logit = py_obj.logit
        self.p = py_obj.p


class PyLlamaTokenDataArray:
    def __init__(self, data=None, size=None, selected=None, sorted=None):
        self.data = data
        self.size = size
        self.selected = selected
        self.sorted = sorted

    @property
    def c(self) -> 'LlamaTokenDataArray':
        c_obj = LlamaTokenDataArray()
        if self.data is not None:
            c_obj.data = self.data
        if self.size is not None:
            c_obj.size = self.size
        if self.selected is not None:
            c_obj.selected = self.selected
        if self.sorted is not None:
            c_obj.sorted = self.sorted
        return c_obj

    @c.setter
    def c(self, value: 'LlamaTokenDataArray'):
        py_obj = value.py
        self.data = py_obj.data
        self.size = py_obj.size
        self.selected = py_obj.selected
        self.sorted = py_obj.sorted


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


class PyLlamaModelTensorOverride:
    def __init__(self, pattern=None, type=None):
        self.pattern = pattern
        self.type = type

    @property
    def c(self) -> 'LlamaModelTensorOverride':
        c_obj = LlamaModelTensorOverride()
        if self.pattern is not None:
            c_obj.pattern = self.pattern
        if self.type is not None:
            c_obj.type = self.type
        return c_obj

    @c.setter
    def c(self, value: 'LlamaModelTensorOverride'):
        py_obj = value.py
        self.pattern = py_obj.pattern
        self.type = py_obj.type


class PyLlamaModelImatrixData:
    def __init__(self, name=None, data=None, size=None):
        self.name = name
        self.data = data
        self.size = size

    @property
    def c(self) -> 'LlamaModelImatrixData':
        c_obj = LlamaModelImatrixData()
        if self.name is not None:
            c_obj.name = self.name
        if self.data is not None:
            c_obj.data = self.data
        if self.size is not None:
            c_obj.size = self.size
        return c_obj

    @c.setter
    def c(self, value: 'LlamaModelImatrixData'):
        py_obj = value.py
        self.name = py_obj.name
        self.data = py_obj.data
        self.size = py_obj.size


class PyLlamaModelQuantizeParams:
    def __init__(self, nthread=None, ftype=None, output_tensor_type=None, token_embedding_type=None,
                 allow_requantize=None, quantize_output_tensor=None, only_copy=None, pure=None, keep_split=None,
                 dry_run=None, imatrix=None, kv_overrides=None, tt_overrides=None, prune_layers=None):
        self.nthread = nthread
        self.ftype = ftype
        self.output_tensor_type = output_tensor_type
        self.token_embedding_type = token_embedding_type
        self.allow_requantize = allow_requantize
        self.quantize_output_tensor = quantize_output_tensor
        self.only_copy = only_copy
        self.pure = pure
        self.keep_split = keep_split
        self.dry_run = dry_run
        self.imatrix = imatrix
        self.kv_overrides = kv_overrides
        self.tt_overrides = tt_overrides
        self.prune_layers = prune_layers

    @property
    def c(self) -> 'LlamaModelQuantizeParams':
        c_obj = LlamaModelQuantizeParams()
        if self.nthread is not None:
            c_obj.nthread = self.nthread
        if self.ftype is not None:
            c_obj.ftype = self.ftype
        if self.output_tensor_type is not None:
            c_obj.output_tensor_type = self.output_tensor_type
        if self.token_embedding_type is not None:
            c_obj.token_embedding_type = self.token_embedding_type
        if self.allow_requantize is not None:
            c_obj.allow_requantize = self.allow_requantize
        if self.quantize_output_tensor is not None:
            c_obj.quantize_output_tensor = self.quantize_output_tensor
        if self.only_copy is not None:
            c_obj.only_copy = self.only_copy
        if self.pure is not None:
            c_obj.pure = self.pure
        if self.keep_split is not None:
            c_obj.keep_split = self.keep_split
        if self.dry_run is not None:
            c_obj.dry_run = self.dry_run
        if self.imatrix is not None:
            c_obj.imatrix = self.imatrix
        if self.kv_overrides is not None:
            c_obj.kv_overrides = self.kv_overrides
        if self.tt_overrides is not None:
            c_obj.tt_overrides = self.tt_overrides
        if self.prune_layers is not None:
            c_obj.prune_layers = self.prune_layers
        return c_obj

    @c.setter
    def c(self, value: 'LlamaModelQuantizeParams'):
        py_obj = value.py
        self.nthread = py_obj.nthread
        self.ftype = py_obj.ftype
        self.output_tensor_type = py_obj.output_tensor_type
        self.token_embedding_type = py_obj.token_embedding_type
        self.allow_requantize = py_obj.allow_requantize
        self.quantize_output_tensor = py_obj.quantize_output_tensor
        self.only_copy = py_obj.only_copy
        self.pure = py_obj.pure
        self.keep_split = py_obj.keep_split
        self.dry_run = py_obj.dry_run
        self.imatrix = py_obj.imatrix
        self.kv_overrides = py_obj.kv_overrides
        self.tt_overrides = py_obj.tt_overrides
        self.prune_layers = py_obj.prune_layers


class PyLlamaLogitBias:
    def __init__(self, token=None, bias=None):
        self.token = token
        self.bias = bias

    @property
    def c(self) -> 'LlamaLogitBias':
        c_obj = LlamaLogitBias()
        if self.token is not None:
            c_obj.token = self.token
        if self.bias is not None:
            c_obj.bias = self.bias
        return c_obj

    @c.setter
    def c(self, value: 'LlamaLogitBias'):
        py_obj = value.py
        self.token = py_obj.token
        self.bias = py_obj.bias


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


class PyLlamaSamplerData:
    def __init__(self, logits=None, probs=None, sampled=None, candidates=None):
        self.logits = logits
        self.probs = probs
        self.sampled = sampled
        self.candidates = candidates

    @property
    def c(self) -> 'LlamaSamplerData':
        c_obj = LlamaSamplerData()
        if self.logits is not None:
            c_obj.logits = self.logits
        if self.probs is not None:
            c_obj.probs = self.probs
        if self.sampled is not None:
            c_obj.sampled = self.sampled
        if self.candidates is not None:
            c_obj.candidates = self.candidates
        return c_obj

    @c.setter
    def c(self, value: 'LlamaSamplerData'):
        py_obj = value.py
        self.logits = py_obj.logits
        self.probs = py_obj.probs
        self.sampled = py_obj.sampled
        self.candidates = py_obj.candidates


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


class PyLlamaPerfContextData:
    def __init__(self, t_start_ms=None, t_load_ms=None, t_p_eval_ms=None, t_eval_ms=None, n_p_eval=None, n_eval=None,
                 n_reused=None):
        self.t_start_ms = t_start_ms
        self.t_load_ms = t_load_ms
        self.t_p_eval_ms = t_p_eval_ms
        self.t_eval_ms = t_eval_ms
        self.n_p_eval = n_p_eval
        self.n_eval = n_eval
        self.n_reused = n_reused

    @property
    def c(self) -> 'LlamaPerfContextData':
        c_obj = LlamaPerfContextData()
        if self.t_start_ms is not None:
            c_obj.t_start_ms = self.t_start_ms
        if self.t_load_ms is not None:
            c_obj.t_load_ms = self.t_load_ms
        if self.t_p_eval_ms is not None:
            c_obj.t_p_eval_ms = self.t_p_eval_ms
        if self.t_eval_ms is not None:
            c_obj.t_eval_ms = self.t_eval_ms
        if self.n_p_eval is not None:
            c_obj.n_p_eval = self.n_p_eval
        if self.n_eval is not None:
            c_obj.n_eval = self.n_eval
        if self.n_reused is not None:
            c_obj.n_reused = self.n_reused
        return c_obj

    @c.setter
    def c(self, value: 'LlamaPerfContextData'):
        py_obj = value.py
        self.t_start_ms = py_obj.t_start_ms
        self.t_load_ms = py_obj.t_load_ms
        self.t_p_eval_ms = py_obj.t_p_eval_ms
        self.t_eval_ms = py_obj.t_eval_ms
        self.n_p_eval = py_obj.n_p_eval
        self.n_eval = py_obj.n_eval
        self.n_reused = py_obj.n_reused


class PyLlamaPerfSamplerData:
    def __init__(self, t_sample_ms=None, n_sample=None):
        self.t_sample_ms = t_sample_ms
        self.n_sample = n_sample

    @property
    def c(self) -> 'LlamaPerfSamplerData':
        c_obj = LlamaPerfSamplerData()
        if self.t_sample_ms is not None:
            c_obj.t_sample_ms = self.t_sample_ms
        if self.n_sample is not None:
            c_obj.n_sample = self.n_sample
        return c_obj

    @c.setter
    def c(self, value: 'LlamaPerfSamplerData'):
        py_obj = value.py
        self.t_sample_ms = py_obj.t_sample_ms
        self.n_sample = py_obj.n_sample


class PyLlamaOptParams:
    def __init__(self, n_ctx_train=None, param_filter=None, param_filter_ud=None, get_opt_pars=None,
                 get_opt_pars_ud=None, optimizer_type=None):
        self.n_ctx_train = n_ctx_train
        self.param_filter = param_filter
        self.param_filter_ud = param_filter_ud
        self.get_opt_pars = get_opt_pars
        self.get_opt_pars_ud = get_opt_pars_ud
        self.optimizer_type = optimizer_type

    @property
    def c(self) -> 'LlamaOptParams':
        c_obj = LlamaOptParams()
        if self.n_ctx_train is not None:
            c_obj.n_ctx_train = self.n_ctx_train
        if self.param_filter is not None:
            c_obj.param_filter = self.param_filter
        if self.param_filter_ud is not None:
            c_obj.param_filter_ud = self.param_filter_ud
        if self.get_opt_pars is not None:
            c_obj.get_opt_pars = self.get_opt_pars
        if self.get_opt_pars_ud is not None:
            c_obj.get_opt_pars_ud = self.get_opt_pars_ud
        if self.optimizer_type is not None:
            c_obj.optimizer_type = self.optimizer_type
        return c_obj

    @c.setter
    def c(self, value: 'LlamaOptParams'):
        py_obj = value.py
        self.n_ctx_train = py_obj.n_ctx_train
        self.param_filter = py_obj.param_filter
        self.param_filter_ud = py_obj.param_filter_ud
        self.get_opt_pars = py_obj.get_opt_pars
        self.get_opt_pars_ud = py_obj.get_opt_pars_ud
        self.optimizer_type = py_obj.optimizer_type


def c_llama_flash_attn_type_name(flash_attn_type: int) -> bytes:
    return llama.llama_flash_attn_type_name(flash_attn_type)


def llama_flash_attn_type_name(flash_attn_type: int) -> bytes:
    return c_llama_flash_attn_type_name(flash_attn_type)


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


def c_llama_model_quantize_default_params() -> 'LlamaModelQuantizeParams':
    return llama.llama_model_quantize_default_params()


def llama_model_quantize_default_params() -> 'PyLlamaModelQuantizeParams':
    return c_llama_model_quantize_default_params().py


def c_llama_backend_init():
    return llama.llama_backend_init()


def llama_backend_init():
    return c_llama_backend_init()


def c_llama_backend_free():
    return llama.llama_backend_free()


def llama_backend_free():
    return c_llama_backend_free()


def c_llama_numa_init(numa: int):
    return llama.llama_numa_init(numa)


def llama_numa_init(numa: int):
    return c_llama_numa_init(numa)


def c_llama_attach_threadpool(ctx: 'LlamaContextPointer', threadpool, threadpool_batch):
    return llama.llama_attach_threadpool(ctx, threadpool, threadpool_batch)


def llama_attach_threadpool(ctx: 'LlamaContextPointer', threadpool, threadpool_batch):
    return c_llama_attach_threadpool(ctx, threadpool, threadpool_batch)


def c_llama_detach_threadpool(ctx: 'LlamaContextPointer'):
    return llama.llama_detach_threadpool(ctx)


def llama_detach_threadpool(ctx: 'LlamaContextPointer'):
    return c_llama_detach_threadpool(ctx)


def c_llama_model_init_from_user(metadata, set_tensor_data, set_tensor_data_ud,
                                 params: 'LlamaModelParams') -> 'LlamaModelPointer':
    return llama.llama_model_init_from_user(metadata, set_tensor_data, set_tensor_data_ud, params)


def llama_model_init_from_user(metadata, set_tensor_data, set_tensor_data_ud,
                               params: 'PyLlamaModelParams') -> 'LlamaModelPointer':
    return c_llama_model_init_from_user(metadata, set_tensor_data, set_tensor_data_ud, params.c)


def c_llama_load_model_from_file(path_model: bytes, params: 'LlamaModelParams') -> 'LlamaModelPointer':
    return llama.llama_load_model_from_file(path_model, params)


def llama_load_model_from_file(path_model: bytes, params: 'PyLlamaModelParams') -> 'LlamaModelPointer':
    return c_llama_load_model_from_file(path_model, params.c)


def c_llama_model_load_from_file(path_model: bytes, params: 'LlamaModelParams') -> 'LlamaModelPointer':
    return llama.llama_model_load_from_file(path_model, params)


def llama_model_load_from_file(path_model: bytes, params: 'PyLlamaModelParams') -> 'LlamaModelPointer':
    return c_llama_model_load_from_file(path_model, params.c)


def c_llama_model_load_from_file_ptr(file, params: 'LlamaModelParams') -> 'LlamaModelPointer':
    return llama.llama_model_load_from_file_ptr(file, params)


def llama_model_load_from_file_ptr(file, params: 'PyLlamaModelParams') -> 'LlamaModelPointer':
    return c_llama_model_load_from_file_ptr(file, params.c)


def c_llama_model_load_from_splits(paths, n_paths: int, params: 'LlamaModelParams') -> 'LlamaModelPointer':
    return llama.llama_model_load_from_splits(paths, n_paths, params)


def llama_model_load_from_splits(paths, n_paths: int, params: 'PyLlamaModelParams') -> 'LlamaModelPointer':
    return c_llama_model_load_from_splits(paths, n_paths, params.c)


def c_llama_model_save_to_file(model: 'LlamaModelPointer', path_model: bytes):
    return llama.llama_model_save_to_file(model, path_model)


def llama_model_save_to_file(model: 'LlamaModelPointer', path_model: bytes):
    return c_llama_model_save_to_file(model, path_model)


def c_llama_free_model(model: 'LlamaModelPointer'):
    return llama.llama_free_model(model)


def llama_free_model(model: 'LlamaModelPointer'):
    return c_llama_free_model(model)


def c_llama_model_free(model: 'LlamaModelPointer'):
    return llama.llama_model_free(model)


def llama_model_free(model: 'LlamaModelPointer'):
    return c_llama_model_free(model)


def c_llama_init_from_model(model: 'LlamaModelPointer', params: 'LlamaContextParams') -> 'LlamaContextPointer':
    return llama.llama_init_from_model(model, params)


def llama_init_from_model(model: 'LlamaModelPointer', params: 'PyLlamaContextParams') -> 'LlamaContextPointer':
    return c_llama_init_from_model(model, params.c)


def c_llama_new_context_with_model(model: 'LlamaModelPointer', params: 'LlamaContextParams') -> 'LlamaContextPointer':
    return llama.llama_new_context_with_model(model, params)


def llama_new_context_with_model(model: 'LlamaModelPointer', params: 'PyLlamaContextParams') -> 'LlamaContextPointer':
    return c_llama_new_context_with_model(model, params.c)


def c_llama_free(ctx: 'LlamaContextPointer'):
    return llama.llama_free(ctx)


def llama_free(ctx: 'LlamaContextPointer'):
    return c_llama_free(ctx)


def c_llama_time_us() -> int:
    return llama.llama_time_us()


def llama_time_us() -> int:
    return c_llama_time_us()


def c_llama_max_devices() -> int:
    return llama.llama_max_devices()


def llama_max_devices() -> int:
    return c_llama_max_devices()


def c_llama_max_parallel_sequences() -> int:
    return llama.llama_max_parallel_sequences()


def llama_max_parallel_sequences() -> int:
    return c_llama_max_parallel_sequences()


def c_llama_max_tensor_buft_overrides() -> int:
    return llama.llama_max_tensor_buft_overrides()


def llama_max_tensor_buft_overrides() -> int:
    return c_llama_max_tensor_buft_overrides()


def c_llama_supports_mmap() -> int:
    return llama.llama_supports_mmap()


def llama_supports_mmap() -> int:
    return c_llama_supports_mmap()


def c_llama_supports_mlock() -> int:
    return llama.llama_supports_mlock()


def llama_supports_mlock() -> int:
    return c_llama_supports_mlock()


def c_llama_supports_gpu_offload() -> int:
    return llama.llama_supports_gpu_offload()


def llama_supports_gpu_offload() -> int:
    return c_llama_supports_gpu_offload()


def c_llama_supports_rpc() -> int:
    return llama.llama_supports_rpc()


def llama_supports_rpc() -> int:
    return c_llama_supports_rpc()


def c_llama_n_ctx(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_ctx(ctx)


def llama_n_ctx(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_ctx(ctx)


def c_llama_n_ctx_seq(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_ctx_seq(ctx)


def llama_n_ctx_seq(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_ctx_seq(ctx)


def c_llama_n_batch(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_batch(ctx)


def llama_n_batch(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_batch(ctx)


def c_llama_n_ubatch(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_ubatch(ctx)


def llama_n_ubatch(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_ubatch(ctx)


def c_llama_n_seq_max(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_seq_max(ctx)


def llama_n_seq_max(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_seq_max(ctx)


def c_llama_n_rs_seq(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_rs_seq(ctx)


def llama_n_rs_seq(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_rs_seq(ctx)


def c_llama_n_ctx_train(model: 'LlamaModelPointer') -> int:
    return llama.llama_n_ctx_train(model)


def llama_n_ctx_train(model: 'LlamaModelPointer') -> int:
    return c_llama_n_ctx_train(model)


def c_llama_n_embd(model: 'LlamaModelPointer') -> int:
    return llama.llama_n_embd(model)


def llama_n_embd(model: 'LlamaModelPointer') -> int:
    return c_llama_n_embd(model)


def c_llama_n_layer(model: 'LlamaModelPointer') -> int:
    return llama.llama_n_layer(model)


def llama_n_layer(model: 'LlamaModelPointer') -> int:
    return c_llama_n_layer(model)


def c_llama_n_head(model: 'LlamaModelPointer') -> int:
    return llama.llama_n_head(model)


def llama_n_head(model: 'LlamaModelPointer') -> int:
    return c_llama_n_head(model)


def c_llama_n_vocab(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_n_vocab(vocab)


def llama_n_vocab(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_n_vocab(vocab)


def c_llama_get_model(ctx: 'LlamaContextPointer') -> 'LlamaModelPointer':
    return llama.llama_get_model(ctx)


def llama_get_model(ctx: 'LlamaContextPointer') -> 'LlamaModelPointer':
    return c_llama_get_model(ctx)


def c_llama_get_memory(ctx: 'LlamaContextPointer') -> Any:
    return llama.llama_get_memory(ctx)


def llama_get_memory(ctx: 'LlamaContextPointer') -> Any:
    return c_llama_get_memory(ctx)


def c_llama_pooling_type(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_pooling_type(ctx)


def llama_pooling_type(ctx: 'LlamaContextPointer') -> int:
    return c_llama_pooling_type(ctx)


def c_llama_model_get_vocab(model: 'LlamaModelPointer') -> 'LlamaVocabPointer':
    return llama.llama_model_get_vocab(model)


def llama_model_get_vocab(model: 'LlamaModelPointer') -> 'LlamaVocabPointer':
    return c_llama_model_get_vocab(model)


def c_llama_model_rope_type(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_rope_type(model)


def llama_model_rope_type(model: 'LlamaModelPointer') -> int:
    return c_llama_model_rope_type(model)


def c_llama_model_n_ctx_train(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_ctx_train(model)


def llama_model_n_ctx_train(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_ctx_train(model)


def c_llama_model_n_embd(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_embd(model)


def llama_model_n_embd(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_embd(model)


def c_llama_model_n_embd_inp(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_embd_inp(model)


def llama_model_n_embd_inp(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_embd_inp(model)


def c_llama_model_n_embd_out(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_embd_out(model)


def llama_model_n_embd_out(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_embd_out(model)


def c_llama_model_n_layer(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_layer(model)


def llama_model_n_layer(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_layer(model)


def c_llama_model_n_head(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_head(model)


def llama_model_n_head(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_head(model)


def c_llama_model_n_head_kv(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_head_kv(model)


def llama_model_n_head_kv(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_head_kv(model)


def c_llama_model_n_swa(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_swa(model)


def llama_model_n_swa(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_swa(model)


def c_llama_model_rope_freq_scale_train(model: 'LlamaModelPointer') -> float:
    return llama.llama_model_rope_freq_scale_train(model)


def llama_model_rope_freq_scale_train(model: 'LlamaModelPointer') -> float:
    return c_llama_model_rope_freq_scale_train(model)


def c_llama_model_n_cls_out(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_cls_out(model)


def llama_model_n_cls_out(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_cls_out(model)


def c_llama_model_cls_label(model: 'LlamaModelPointer', i: int) -> bytes:
    return llama.llama_model_cls_label(model, i)


def llama_model_cls_label(model: 'LlamaModelPointer', i: int) -> bytes:
    return c_llama_model_cls_label(model, i)


def c_llama_vocab_type(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_vocab_type(vocab)


def llama_vocab_type(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_vocab_type(vocab)


def c_llama_vocab_n_tokens(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_vocab_n_tokens(vocab)


def llama_vocab_n_tokens(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_vocab_n_tokens(vocab)


def c_llama_model_meta_val_str(model: 'LlamaModelPointer', key: bytes, buf: bytes, buf_size: int) -> int:
    return llama.llama_model_meta_val_str(model, key, buf, buf_size)


def llama_model_meta_val_str(model: 'LlamaModelPointer', key: bytes, buf: bytes, buf_size: int) -> int:
    return c_llama_model_meta_val_str(model, key, buf, buf_size)


def c_llama_model_meta_count(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_meta_count(model)


def llama_model_meta_count(model: 'LlamaModelPointer') -> int:
    return c_llama_model_meta_count(model)


def c_llama_model_meta_key_str(key: int) -> bytes:
    return llama.llama_model_meta_key_str(key)


def llama_model_meta_key_str(key: int) -> bytes:
    return c_llama_model_meta_key_str(key)


def c_llama_model_meta_key_by_index(model: 'LlamaModelPointer', i: int, buf: bytes, buf_size: int) -> int:
    return llama.llama_model_meta_key_by_index(model, i, buf, buf_size)


def llama_model_meta_key_by_index(model: 'LlamaModelPointer', i: int, buf: bytes, buf_size: int) -> int:
    return c_llama_model_meta_key_by_index(model, i, buf, buf_size)


def c_llama_model_meta_val_str_by_index(model: 'LlamaModelPointer', i: int, buf: bytes, buf_size: int) -> int:
    return llama.llama_model_meta_val_str_by_index(model, i, buf, buf_size)


def llama_model_meta_val_str_by_index(model: 'LlamaModelPointer', i: int, buf: bytes, buf_size: int) -> int:
    return c_llama_model_meta_val_str_by_index(model, i, buf, buf_size)


def c_llama_model_desc(model: 'LlamaModelPointer', buf: bytes, buf_size: int) -> int:
    return llama.llama_model_desc(model, buf, buf_size)


def llama_model_desc(model: 'LlamaModelPointer', buf: bytes, buf_size: int) -> int:
    return c_llama_model_desc(model, buf, buf_size)


def c_llama_model_size(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_size(model)


def llama_model_size(model: 'LlamaModelPointer') -> int:
    return c_llama_model_size(model)


def c_llama_model_chat_template(model: 'LlamaModelPointer', name: bytes) -> bytes:
    return llama.llama_model_chat_template(model, name)


def llama_model_chat_template(model: 'LlamaModelPointer', name: bytes) -> bytes:
    return c_llama_model_chat_template(model, name)


def c_llama_model_n_params(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_n_params(model)


def llama_model_n_params(model: 'LlamaModelPointer') -> int:
    return c_llama_model_n_params(model)


def c_llama_model_has_encoder(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_has_encoder(model)


def llama_model_has_encoder(model: 'LlamaModelPointer') -> int:
    return c_llama_model_has_encoder(model)


def c_llama_model_has_decoder(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_has_decoder(model)


def llama_model_has_decoder(model: 'LlamaModelPointer') -> int:
    return c_llama_model_has_decoder(model)


def c_llama_model_decoder_start_token(model: 'LlamaModelPointer') -> Any:
    return llama.llama_model_decoder_start_token(model)


def llama_model_decoder_start_token(model: 'LlamaModelPointer') -> Any:
    return c_llama_model_decoder_start_token(model)


def c_llama_model_is_recurrent(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_is_recurrent(model)


def llama_model_is_recurrent(model: 'LlamaModelPointer') -> int:
    return c_llama_model_is_recurrent(model)


def c_llama_model_is_hybrid(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_is_hybrid(model)


def llama_model_is_hybrid(model: 'LlamaModelPointer') -> int:
    return c_llama_model_is_hybrid(model)


def c_llama_model_is_diffusion(model: 'LlamaModelPointer') -> int:
    return llama.llama_model_is_diffusion(model)


def llama_model_is_diffusion(model: 'LlamaModelPointer') -> int:
    return c_llama_model_is_diffusion(model)


def c_llama_model_quantize(fname_inp: bytes, fname_out: bytes, params: 'LlamaModelQuantizeParamsPointer') -> int:
    return llama.llama_model_quantize(fname_inp, fname_out, params)


def llama_model_quantize(fname_inp: bytes, fname_out: bytes, params: 'LlamaModelQuantizeParamsPointer') -> int:
    return c_llama_model_quantize(fname_inp, fname_out, params)


def c_llama_adapter_lora_init(model: 'LlamaModelPointer', path_lora: bytes) -> 'LlamaAdapterLoraPointer':
    return llama.llama_adapter_lora_init(model, path_lora)


def llama_adapter_lora_init(model: 'LlamaModelPointer', path_lora: bytes) -> 'LlamaAdapterLoraPointer':
    return c_llama_adapter_lora_init(model, path_lora)


def c_llama_adapter_meta_val_str(adapter: 'LlamaAdapterLoraPointer', key: bytes, buf: bytes, buf_size: int) -> int:
    return llama.llama_adapter_meta_val_str(adapter, key, buf, buf_size)


def llama_adapter_meta_val_str(adapter: 'LlamaAdapterLoraPointer', key: bytes, buf: bytes, buf_size: int) -> int:
    return c_llama_adapter_meta_val_str(adapter, key, buf, buf_size)


def c_llama_adapter_meta_count(adapter: 'LlamaAdapterLoraPointer') -> int:
    return llama.llama_adapter_meta_count(adapter)


def llama_adapter_meta_count(adapter: 'LlamaAdapterLoraPointer') -> int:
    return c_llama_adapter_meta_count(adapter)


def c_llama_adapter_meta_key_by_index(adapter: 'LlamaAdapterLoraPointer', i: int, buf: bytes, buf_size: int) -> int:
    return llama.llama_adapter_meta_key_by_index(adapter, i, buf, buf_size)


def llama_adapter_meta_key_by_index(adapter: 'LlamaAdapterLoraPointer', i: int, buf: bytes, buf_size: int) -> int:
    return c_llama_adapter_meta_key_by_index(adapter, i, buf, buf_size)


def c_llama_adapter_meta_val_str_by_index(adapter: 'LlamaAdapterLoraPointer', i: int, buf: bytes, buf_size: int) -> int:
    return llama.llama_adapter_meta_val_str_by_index(adapter, i, buf, buf_size)


def llama_adapter_meta_val_str_by_index(adapter: 'LlamaAdapterLoraPointer', i: int, buf: bytes, buf_size: int) -> int:
    return c_llama_adapter_meta_val_str_by_index(adapter, i, buf, buf_size)


def c_llama_adapter_lora_free(adapter: 'LlamaAdapterLoraPointer'):
    return llama.llama_adapter_lora_free(adapter)


def llama_adapter_lora_free(adapter: 'LlamaAdapterLoraPointer'):
    return c_llama_adapter_lora_free(adapter)


def c_llama_adapter_get_alora_n_invocation_tokens(adapter: 'LlamaAdapterLoraPointer') -> int:
    return llama.llama_adapter_get_alora_n_invocation_tokens(adapter)


def llama_adapter_get_alora_n_invocation_tokens(adapter: 'LlamaAdapterLoraPointer') -> int:
    return c_llama_adapter_get_alora_n_invocation_tokens(adapter)


def c_llama_adapter_get_alora_invocation_tokens(adapter: 'LlamaAdapterLoraPointer') -> 'LlamaTokenPointer':
    return llama.llama_adapter_get_alora_invocation_tokens(adapter)


def llama_adapter_get_alora_invocation_tokens(adapter: 'LlamaAdapterLoraPointer') -> 'LlamaTokenPointer':
    return c_llama_adapter_get_alora_invocation_tokens(adapter)


def c_llama_set_adapters_lora(ctx: 'LlamaContextPointer', adapters, n_adapters: int, scales) -> int:
    return llama.llama_set_adapters_lora(ctx, adapters, n_adapters, scales)


def llama_set_adapters_lora(ctx: 'LlamaContextPointer', adapters, n_adapters: int, scales) -> int:
    return c_llama_set_adapters_lora(ctx, adapters, n_adapters, scales)


def c_llama_set_adapter_cvec(ctx: 'LlamaContextPointer', data, len_: int, n_embd: int, il_start: int,
                             il_end: int) -> int:
    return llama.llama_set_adapter_cvec(ctx, data, len_, n_embd, il_start, il_end)


def llama_set_adapter_cvec(ctx: 'LlamaContextPointer', data, len_: int, n_embd: int, il_start: int, il_end: int) -> int:
    return c_llama_set_adapter_cvec(ctx, data, len_, n_embd, il_start, il_end)


def c_llama_memory_clear(mem, data: bool):
    return llama.llama_memory_clear(mem, data)


def llama_memory_clear(mem, data: bool):
    return c_llama_memory_clear(mem, data)


def c_llama_memory_seq_rm(mem, seq_id, p0, p1) -> int:
    return llama.llama_memory_seq_rm(mem, seq_id, p0, p1)


def llama_memory_seq_rm(mem, seq_id, p0, p1) -> int:
    return c_llama_memory_seq_rm(mem, seq_id, p0, p1)


def c_llama_memory_seq_cp(mem, seq_id_src, seq_id_dst, p0, p1):
    return llama.llama_memory_seq_cp(mem, seq_id_src, seq_id_dst, p0, p1)


def llama_memory_seq_cp(mem, seq_id_src, seq_id_dst, p0, p1):
    return c_llama_memory_seq_cp(mem, seq_id_src, seq_id_dst, p0, p1)


def c_llama_memory_seq_keep(mem, seq_id):
    return llama.llama_memory_seq_keep(mem, seq_id)


def llama_memory_seq_keep(mem, seq_id):
    return c_llama_memory_seq_keep(mem, seq_id)


def c_llama_memory_seq_add(mem, seq_id, p0, p1, delta):
    return llama.llama_memory_seq_add(mem, seq_id, p0, p1, delta)


def llama_memory_seq_add(mem, seq_id, p0, p1, delta):
    return c_llama_memory_seq_add(mem, seq_id, p0, p1, delta)


def c_llama_memory_seq_div(mem, seq_id, p0, p1, d: int):
    return llama.llama_memory_seq_div(mem, seq_id, p0, p1, d)


def llama_memory_seq_div(mem, seq_id, p0, p1, d: int):
    return c_llama_memory_seq_div(mem, seq_id, p0, p1, d)


def c_llama_memory_seq_pos_min(mem, seq_id) -> Any:
    return llama.llama_memory_seq_pos_min(mem, seq_id)


def llama_memory_seq_pos_min(mem, seq_id) -> Any:
    return c_llama_memory_seq_pos_min(mem, seq_id)


def c_llama_memory_seq_pos_max(mem, seq_id) -> Any:
    return llama.llama_memory_seq_pos_max(mem, seq_id)


def llama_memory_seq_pos_max(mem, seq_id) -> Any:
    return c_llama_memory_seq_pos_max(mem, seq_id)


def c_llama_memory_can_shift(mem) -> int:
    return llama.llama_memory_can_shift(mem)


def llama_memory_can_shift(mem) -> int:
    return c_llama_memory_can_shift(mem)


def c_llama_state_get_size(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_state_get_size(ctx)


def llama_state_get_size(ctx: 'LlamaContextPointer') -> int:
    return c_llama_state_get_size(ctx)


def c_llama_get_state_size(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_get_state_size(ctx)


def llama_get_state_size(ctx: 'LlamaContextPointer') -> int:
    return c_llama_get_state_size(ctx)


def c_llama_state_get_data(ctx: 'LlamaContextPointer', dst, size: int) -> int:
    return llama.llama_state_get_data(ctx, dst, size)


def llama_state_get_data(ctx: 'LlamaContextPointer', dst, size: int) -> int:
    return c_llama_state_get_data(ctx, dst, size)


def c_llama_copy_state_data(ctx: 'LlamaContextPointer', dst) -> int:
    return llama.llama_copy_state_data(ctx, dst)


def llama_copy_state_data(ctx: 'LlamaContextPointer', dst) -> int:
    return c_llama_copy_state_data(ctx, dst)


def c_llama_state_set_data(ctx: 'LlamaContextPointer', src, size: int) -> int:
    return llama.llama_state_set_data(ctx, src, size)


def llama_state_set_data(ctx: 'LlamaContextPointer', src, size: int) -> int:
    return c_llama_state_set_data(ctx, src, size)


def c_llama_set_state_data(ctx: 'LlamaContextPointer', src) -> int:
    return llama.llama_set_state_data(ctx, src)


def llama_set_state_data(ctx: 'LlamaContextPointer', src) -> int:
    return c_llama_set_state_data(ctx, src)


def c_llama_state_load_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens_out: 'LlamaTokenPointer',
                            n_token_capacity: int, n_token_count_out) -> int:
    return llama.llama_state_load_file(ctx, path_session, tokens_out, n_token_capacity, n_token_count_out)


def llama_state_load_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens_out: 'LlamaTokenPointer',
                          n_token_capacity: int, n_token_count_out) -> int:
    return c_llama_state_load_file(ctx, path_session, tokens_out, n_token_capacity, n_token_count_out)


def c_llama_load_session_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens_out: 'LlamaTokenPointer',
                              n_token_capacity: int, n_token_count_out) -> int:
    return llama.llama_load_session_file(ctx, path_session, tokens_out, n_token_capacity, n_token_count_out)


def llama_load_session_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens_out: 'LlamaTokenPointer',
                            n_token_capacity: int, n_token_count_out) -> int:
    return c_llama_load_session_file(ctx, path_session, tokens_out, n_token_capacity, n_token_count_out)


def c_llama_state_save_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens: 'LlamaTokenPointer',
                            n_token_count: int) -> int:
    return llama.llama_state_save_file(ctx, path_session, tokens, n_token_count)


def llama_state_save_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens: 'LlamaTokenPointer',
                          n_token_count: int) -> int:
    return c_llama_state_save_file(ctx, path_session, tokens, n_token_count)


def c_llama_save_session_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens: 'LlamaTokenPointer',
                              n_token_count: int) -> int:
    return llama.llama_save_session_file(ctx, path_session, tokens, n_token_count)


def llama_save_session_file(ctx: 'LlamaContextPointer', path_session: bytes, tokens: 'LlamaTokenPointer',
                            n_token_count: int) -> int:
    return c_llama_save_session_file(ctx, path_session, tokens, n_token_count)


def c_llama_state_seq_get_size(ctx: 'LlamaContextPointer', seq_id) -> int:
    return llama.llama_state_seq_get_size(ctx, seq_id)


def llama_state_seq_get_size(ctx: 'LlamaContextPointer', seq_id) -> int:
    return c_llama_state_seq_get_size(ctx, seq_id)


def c_llama_state_seq_get_data(ctx: 'LlamaContextPointer', dst, size: int, seq_id) -> int:
    return llama.llama_state_seq_get_data(ctx, dst, size, seq_id)


def llama_state_seq_get_data(ctx: 'LlamaContextPointer', dst, size: int, seq_id) -> int:
    return c_llama_state_seq_get_data(ctx, dst, size, seq_id)


def c_llama_state_seq_set_data(ctx: 'LlamaContextPointer', src, size: int, dest_seq_id) -> int:
    return llama.llama_state_seq_set_data(ctx, src, size, dest_seq_id)


def llama_state_seq_set_data(ctx: 'LlamaContextPointer', src, size: int, dest_seq_id) -> int:
    return c_llama_state_seq_set_data(ctx, src, size, dest_seq_id)


def c_llama_state_seq_save_file(ctx: 'LlamaContextPointer', filepath: bytes, seq_id, tokens: 'LlamaTokenPointer',
                                n_token_count: int) -> int:
    return llama.llama_state_seq_save_file(ctx, filepath, seq_id, tokens, n_token_count)


def llama_state_seq_save_file(ctx: 'LlamaContextPointer', filepath: bytes, seq_id, tokens: 'LlamaTokenPointer',
                              n_token_count: int) -> int:
    return c_llama_state_seq_save_file(ctx, filepath, seq_id, tokens, n_token_count)


def c_llama_state_seq_load_file(ctx: 'LlamaContextPointer', filepath: bytes, dest_seq_id,
                                tokens_out: 'LlamaTokenPointer', n_token_capacity: int, n_token_count_out) -> int:
    return llama.llama_state_seq_load_file(ctx, filepath, dest_seq_id, tokens_out, n_token_capacity, n_token_count_out)


def llama_state_seq_load_file(ctx: 'LlamaContextPointer', filepath: bytes, dest_seq_id, tokens_out: 'LlamaTokenPointer',
                              n_token_capacity: int, n_token_count_out) -> int:
    return c_llama_state_seq_load_file(ctx, filepath, dest_seq_id, tokens_out, n_token_capacity, n_token_count_out)


def c_llama_state_seq_get_size_ext(ctx: 'LlamaContextPointer', seq_id, flags) -> int:
    return llama.llama_state_seq_get_size_ext(ctx, seq_id, flags)


def llama_state_seq_get_size_ext(ctx: 'LlamaContextPointer', seq_id, flags) -> int:
    return c_llama_state_seq_get_size_ext(ctx, seq_id, flags)


def c_llama_state_seq_get_data_ext(ctx: 'LlamaContextPointer', dst, size: int, seq_id, flags) -> int:
    return llama.llama_state_seq_get_data_ext(ctx, dst, size, seq_id, flags)


def llama_state_seq_get_data_ext(ctx: 'LlamaContextPointer', dst, size: int, seq_id, flags) -> int:
    return c_llama_state_seq_get_data_ext(ctx, dst, size, seq_id, flags)


def c_llama_state_seq_set_data_ext(ctx: 'LlamaContextPointer', src, size: int, dest_seq_id, flags) -> int:
    return llama.llama_state_seq_set_data_ext(ctx, src, size, dest_seq_id, flags)


def llama_state_seq_set_data_ext(ctx: 'LlamaContextPointer', src, size: int, dest_seq_id, flags) -> int:
    return c_llama_state_seq_set_data_ext(ctx, src, size, dest_seq_id, flags)


def c_llama_batch_get_one(tokens: 'LlamaTokenPointer', n_tokens: int) -> 'LlamaBatch':
    return llama.llama_batch_get_one(tokens, n_tokens)


def llama_batch_get_one(tokens: 'LlamaTokenPointer', n_tokens: int) -> 'PyLlamaBatch':
    return c_llama_batch_get_one(tokens, n_tokens).py


def c_llama_batch_init(n_tokens: int, embd: int, n_seq_max: int) -> 'LlamaBatch':
    return llama.llama_batch_init(n_tokens, embd, n_seq_max)


def llama_batch_init(n_tokens: int, embd: int, n_seq_max: int) -> 'PyLlamaBatch':
    return c_llama_batch_init(n_tokens, embd, n_seq_max).py


def c_llama_batch_free(batch: 'LlamaBatch'):
    return llama.llama_batch_free(batch)


def llama_batch_free(batch: 'PyLlamaBatch'):
    return c_llama_batch_free(batch.c)


def c_llama_encode(ctx: 'LlamaContextPointer', batch: 'LlamaBatch') -> int:
    return llama.llama_encode(ctx, batch)


def llama_encode(ctx: 'LlamaContextPointer', batch: 'PyLlamaBatch') -> int:
    return c_llama_encode(ctx, batch.c)


def c_llama_decode(ctx: 'LlamaContextPointer', batch: 'LlamaBatch') -> int:
    return llama.llama_decode(ctx, batch)


def llama_decode(ctx: 'LlamaContextPointer', batch: 'PyLlamaBatch') -> int:
    return c_llama_decode(ctx, batch.c)


def c_llama_set_n_threads(ctx: 'LlamaContextPointer', n_threads: int, n_threads_batch: int):
    return llama.llama_set_n_threads(ctx, n_threads, n_threads_batch)


def llama_set_n_threads(ctx: 'LlamaContextPointer', n_threads: int, n_threads_batch: int):
    return c_llama_set_n_threads(ctx, n_threads, n_threads_batch)


def c_llama_n_threads(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_threads(ctx)


def llama_n_threads(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_threads(ctx)


def c_llama_n_threads_batch(ctx: 'LlamaContextPointer') -> int:
    return llama.llama_n_threads_batch(ctx)


def llama_n_threads_batch(ctx: 'LlamaContextPointer') -> int:
    return c_llama_n_threads_batch(ctx)


def c_llama_set_embeddings(ctx: 'LlamaContextPointer', embeddings: bool):
    return llama.llama_set_embeddings(ctx, embeddings)


def llama_set_embeddings(ctx: 'LlamaContextPointer', embeddings: bool):
    return c_llama_set_embeddings(ctx, embeddings)


def c_llama_set_causal_attn(ctx: 'LlamaContextPointer', causal_attn: bool):
    return llama.llama_set_causal_attn(ctx, causal_attn)


def llama_set_causal_attn(ctx: 'LlamaContextPointer', causal_attn: bool):
    return c_llama_set_causal_attn(ctx, causal_attn)


def c_llama_set_warmup(ctx: 'LlamaContextPointer', warmup: bool):
    return llama.llama_set_warmup(ctx, warmup)


def llama_set_warmup(ctx: 'LlamaContextPointer', warmup: bool):
    return c_llama_set_warmup(ctx, warmup)


def c_llama_set_abort_callback(ctx: 'LlamaContextPointer', abort_callback: int, abort_callback_data):
    return llama.llama_set_abort_callback(ctx, abort_callback, abort_callback_data)


def llama_set_abort_callback(ctx: 'LlamaContextPointer', abort_callback: int, abort_callback_data):
    return c_llama_set_abort_callback(ctx, abort_callback, abort_callback_data)


def c_llama_synchronize(ctx: 'LlamaContextPointer'):
    return llama.llama_synchronize(ctx)


def llama_synchronize(ctx: 'LlamaContextPointer'):
    return c_llama_synchronize(ctx)


def c_llama_get_logits(ctx: 'LlamaContextPointer') -> Any:
    return llama.llama_get_logits(ctx)


def llama_get_logits(ctx: 'LlamaContextPointer') -> Any:
    return c_llama_get_logits(ctx)


def c_llama_get_logits_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return llama.llama_get_logits_ith(ctx, i)


def llama_get_logits_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return c_llama_get_logits_ith(ctx, i)


def c_llama_get_embeddings(ctx: 'LlamaContextPointer') -> Any:
    return llama.llama_get_embeddings(ctx)


def llama_get_embeddings(ctx: 'LlamaContextPointer') -> Any:
    return c_llama_get_embeddings(ctx)


def c_llama_get_embeddings_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return llama.llama_get_embeddings_ith(ctx, i)


def llama_get_embeddings_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return c_llama_get_embeddings_ith(ctx, i)


def c_llama_get_embeddings_seq(ctx: 'LlamaContextPointer', seq_id) -> Any:
    return llama.llama_get_embeddings_seq(ctx, seq_id)


def llama_get_embeddings_seq(ctx: 'LlamaContextPointer', seq_id) -> Any:
    return c_llama_get_embeddings_seq(ctx, seq_id)


def c_llama_get_sampled_token_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return llama.llama_get_sampled_token_ith(ctx, i)


def llama_get_sampled_token_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return c_llama_get_sampled_token_ith(ctx, i)


def c_llama_get_sampled_probs_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return llama.llama_get_sampled_probs_ith(ctx, i)


def llama_get_sampled_probs_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return c_llama_get_sampled_probs_ith(ctx, i)


def c_llama_get_sampled_probs_count_ith(ctx: 'LlamaContextPointer', i: int) -> int:
    return llama.llama_get_sampled_probs_count_ith(ctx, i)


def llama_get_sampled_probs_count_ith(ctx: 'LlamaContextPointer', i: int) -> int:
    return c_llama_get_sampled_probs_count_ith(ctx, i)


def c_llama_get_sampled_logits_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return llama.llama_get_sampled_logits_ith(ctx, i)


def llama_get_sampled_logits_ith(ctx: 'LlamaContextPointer', i: int) -> Any:
    return c_llama_get_sampled_logits_ith(ctx, i)


def c_llama_get_sampled_logits_count_ith(ctx: 'LlamaContextPointer', i: int) -> int:
    return llama.llama_get_sampled_logits_count_ith(ctx, i)


def llama_get_sampled_logits_count_ith(ctx: 'LlamaContextPointer', i: int) -> int:
    return c_llama_get_sampled_logits_count_ith(ctx, i)


def c_llama_get_sampled_candidates_ith(ctx: 'LlamaContextPointer', i: int) -> 'LlamaTokenPointer':
    return llama.llama_get_sampled_candidates_ith(ctx, i)


def llama_get_sampled_candidates_ith(ctx: 'LlamaContextPointer', i: int) -> 'LlamaTokenPointer':
    return c_llama_get_sampled_candidates_ith(ctx, i)


def c_llama_get_sampled_candidates_count_ith(ctx: 'LlamaContextPointer', i: int) -> int:
    return llama.llama_get_sampled_candidates_count_ith(ctx, i)


def llama_get_sampled_candidates_count_ith(ctx: 'LlamaContextPointer', i: int) -> int:
    return c_llama_get_sampled_candidates_count_ith(ctx, i)


def c_llama_vocab_get_text(vocab: 'LlamaVocabPointer', token) -> bytes:
    return llama.llama_vocab_get_text(vocab, token)


def llama_vocab_get_text(vocab: 'LlamaVocabPointer', token) -> bytes:
    return c_llama_vocab_get_text(vocab, token)


def c_llama_vocab_get_score(vocab: 'LlamaVocabPointer', token) -> float:
    return llama.llama_vocab_get_score(vocab, token)


def llama_vocab_get_score(vocab: 'LlamaVocabPointer', token) -> float:
    return c_llama_vocab_get_score(vocab, token)


def c_llama_vocab_get_attr(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_vocab_get_attr(vocab, token)


def llama_vocab_get_attr(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_vocab_get_attr(vocab, token)


def c_llama_vocab_is_eog(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_vocab_is_eog(vocab, token)


def llama_vocab_is_eog(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_vocab_is_eog(vocab, token)


def c_llama_vocab_is_control(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_vocab_is_control(vocab, token)


def llama_vocab_is_control(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_vocab_is_control(vocab, token)


def c_llama_vocab_bos(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_bos(vocab)


def llama_vocab_bos(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_bos(vocab)


def c_llama_vocab_eos(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_eos(vocab)


def llama_vocab_eos(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_eos(vocab)


def c_llama_vocab_eot(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_eot(vocab)


def llama_vocab_eot(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_eot(vocab)


def c_llama_vocab_sep(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_sep(vocab)


def llama_vocab_sep(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_sep(vocab)


def c_llama_vocab_nl(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_nl(vocab)


def llama_vocab_nl(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_nl(vocab)


def c_llama_vocab_pad(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_pad(vocab)


def llama_vocab_pad(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_pad(vocab)


def c_llama_vocab_mask(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_mask(vocab)


def llama_vocab_mask(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_mask(vocab)


def c_llama_vocab_get_add_bos(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_vocab_get_add_bos(vocab)


def llama_vocab_get_add_bos(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_vocab_get_add_bos(vocab)


def c_llama_vocab_get_add_eos(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_vocab_get_add_eos(vocab)


def llama_vocab_get_add_eos(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_vocab_get_add_eos(vocab)


def c_llama_vocab_get_add_sep(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_vocab_get_add_sep(vocab)


def llama_vocab_get_add_sep(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_vocab_get_add_sep(vocab)


def c_llama_vocab_fim_pre(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_fim_pre(vocab)


def llama_vocab_fim_pre(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_fim_pre(vocab)


def c_llama_vocab_fim_suf(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_fim_suf(vocab)


def llama_vocab_fim_suf(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_fim_suf(vocab)


def c_llama_vocab_fim_mid(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_fim_mid(vocab)


def llama_vocab_fim_mid(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_fim_mid(vocab)


def c_llama_vocab_fim_pad(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_fim_pad(vocab)


def llama_vocab_fim_pad(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_fim_pad(vocab)


def c_llama_vocab_fim_rep(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_fim_rep(vocab)


def llama_vocab_fim_rep(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_fim_rep(vocab)


def c_llama_vocab_fim_sep(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_fim_sep(vocab)


def llama_vocab_fim_sep(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_fim_sep(vocab)


def c_llama_token_get_text(vocab: 'LlamaVocabPointer', token) -> bytes:
    return llama.llama_token_get_text(vocab, token)


def llama_token_get_text(vocab: 'LlamaVocabPointer', token) -> bytes:
    return c_llama_token_get_text(vocab, token)


def c_llama_token_get_score(vocab: 'LlamaVocabPointer', token) -> float:
    return llama.llama_token_get_score(vocab, token)


def llama_token_get_score(vocab: 'LlamaVocabPointer', token) -> float:
    return c_llama_token_get_score(vocab, token)


def c_llama_token_get_attr(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_token_get_attr(vocab, token)


def llama_token_get_attr(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_token_get_attr(vocab, token)


def c_llama_token_is_eog(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_token_is_eog(vocab, token)


def llama_token_is_eog(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_token_is_eog(vocab, token)


def c_llama_token_is_control(vocab: 'LlamaVocabPointer', token) -> int:
    return llama.llama_token_is_control(vocab, token)


def llama_token_is_control(vocab: 'LlamaVocabPointer', token) -> int:
    return c_llama_token_is_control(vocab, token)


def c_llama_token_bos(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_bos(vocab)


def llama_token_bos(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_bos(vocab)


def c_llama_token_eos(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_eos(vocab)


def llama_token_eos(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_eos(vocab)


def c_llama_token_eot(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_eot(vocab)


def llama_token_eot(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_eot(vocab)


def c_llama_token_cls(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_cls(vocab)


def llama_token_cls(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_cls(vocab)


def c_llama_token_sep(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_sep(vocab)


def llama_token_sep(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_sep(vocab)


def c_llama_token_nl(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_nl(vocab)


def llama_token_nl(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_nl(vocab)


def c_llama_token_pad(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_pad(vocab)


def llama_token_pad(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_pad(vocab)


def c_llama_add_bos_token(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_add_bos_token(vocab)


def llama_add_bos_token(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_add_bos_token(vocab)


def c_llama_add_eos_token(vocab: 'LlamaVocabPointer') -> int:
    return llama.llama_add_eos_token(vocab)


def llama_add_eos_token(vocab: 'LlamaVocabPointer') -> int:
    return c_llama_add_eos_token(vocab)


def c_llama_token_fim_pre(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_fim_pre(vocab)


def llama_token_fim_pre(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_fim_pre(vocab)


def c_llama_token_fim_suf(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_fim_suf(vocab)


def llama_token_fim_suf(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_fim_suf(vocab)


def c_llama_token_fim_mid(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_fim_mid(vocab)


def llama_token_fim_mid(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_fim_mid(vocab)


def c_llama_token_fim_pad(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_fim_pad(vocab)


def llama_token_fim_pad(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_fim_pad(vocab)


def c_llama_token_fim_rep(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_fim_rep(vocab)


def llama_token_fim_rep(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_fim_rep(vocab)


def c_llama_token_fim_sep(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_token_fim_sep(vocab)


def llama_token_fim_sep(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_token_fim_sep(vocab)


def c_llama_vocab_cls(vocab: 'LlamaVocabPointer') -> Any:
    return llama.llama_vocab_cls(vocab)


def llama_vocab_cls(vocab: 'LlamaVocabPointer') -> Any:
    return c_llama_vocab_cls(vocab)


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


def c_llama_detokenize(vocab: 'LlamaVocabPointer', tokens: 'LlamaTokenPointer', n_tokens: int, text: bytes,
                       text_len_max: int, remove_special: bool, unparse_special: bool) -> int:
    return llama.llama_detokenize(vocab, tokens, n_tokens, text, text_len_max, remove_special, unparse_special)


def llama_detokenize(vocab: 'LlamaVocabPointer', tokens: 'LlamaTokenPointer', n_tokens: int, text: bytes,
                     text_len_max: int, remove_special: bool, unparse_special: bool) -> int:
    return c_llama_detokenize(vocab, tokens, n_tokens, text, text_len_max, remove_special, unparse_special)


def c_llama_chat_apply_template(tmpl: bytes, chat: 'LlamaChatMessagePointer', n_msg: int, add_ass: bool, buf: bytes,
                                length: int) -> int:
    return llama.llama_chat_apply_template(tmpl, chat, n_msg, add_ass, buf, length)


def llama_chat_apply_template(tmpl: bytes, chat: 'LlamaChatMessagePointer', n_msg: int, add_ass: bool, buf: bytes,
                              length: int) -> int:
    return c_llama_chat_apply_template(tmpl, chat, n_msg, add_ass, buf, length)


def c_llama_chat_builtin_templates(output, len_: int) -> int:
    return llama.llama_chat_builtin_templates(output, len_)


def llama_chat_builtin_templates(output, len_: int) -> int:
    return c_llama_chat_builtin_templates(output, len_)


def c_llama_set_sampler(ctx: 'LlamaContextPointer', seq_id, smpl: 'LlamaSamplerPointer') -> int:
    return llama.llama_set_sampler(ctx, seq_id, smpl)


def llama_set_sampler(ctx: 'LlamaContextPointer', seq_id, smpl: 'LlamaSamplerPointer') -> int:
    return c_llama_set_sampler(ctx, seq_id, smpl)


def c_llama_sampler_init(iface: 'LlamaSamplerIPointer', ctx) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init(iface, ctx)


def llama_sampler_init(iface: 'LlamaSamplerIPointer', ctx) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init(iface, ctx)


def c_llama_sampler_name(smpl: 'LlamaSamplerPointer') -> bytes:
    return llama.llama_sampler_name(smpl)


def llama_sampler_name(smpl: 'LlamaSamplerPointer') -> bytes:
    return c_llama_sampler_name(smpl)


def c_llama_sampler_accept(smpl: 'LlamaSamplerPointer', token):
    return llama.llama_sampler_accept(smpl, token)


def llama_sampler_accept(smpl: 'LlamaSamplerPointer', token):
    return c_llama_sampler_accept(smpl, token)


def c_llama_sampler_apply(smpl: 'LlamaSamplerPointer', cur_p: 'LlamaTokenDataArrayPointer'):
    return llama.llama_sampler_apply(smpl, cur_p)


def llama_sampler_apply(smpl: 'LlamaSamplerPointer', cur_p: 'LlamaTokenDataArrayPointer'):
    return c_llama_sampler_apply(smpl, cur_p)


def c_llama_sampler_reset(smpl: 'LlamaSamplerPointer'):
    return llama.llama_sampler_reset(smpl)


def llama_sampler_reset(smpl: 'LlamaSamplerPointer'):
    return c_llama_sampler_reset(smpl)


def c_llama_sampler_clone(smpl: 'LlamaSamplerPointer') -> 'LlamaSamplerPointer':
    return llama.llama_sampler_clone(smpl)


def llama_sampler_clone(smpl: 'LlamaSamplerPointer') -> 'LlamaSamplerPointer':
    return c_llama_sampler_clone(smpl)


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


def c_llama_sampler_chain_get(chain: 'LlamaSamplerPointer', i: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_chain_get(chain, i)


def llama_sampler_chain_get(chain: 'LlamaSamplerPointer', i: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_chain_get(chain, i)


def c_llama_sampler_chain_n(chain: 'LlamaSamplerPointer') -> int:
    return llama.llama_sampler_chain_n(chain)


def llama_sampler_chain_n(chain: 'LlamaSamplerPointer') -> int:
    return c_llama_sampler_chain_n(chain)


def c_llama_sampler_chain_remove(chain: 'LlamaSamplerPointer', i: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_chain_remove(chain, i)


def llama_sampler_chain_remove(chain: 'LlamaSamplerPointer', i: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_chain_remove(chain, i)


def c_llama_sampler_init_greedy() -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_greedy()


def llama_sampler_init_greedy() -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_greedy()


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


def c_llama_sampler_init_typical(p: float, min_keep: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_typical(p, min_keep)


def llama_sampler_init_typical(p: float, min_keep: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_typical(p, min_keep)


def c_llama_sampler_init_temp(t: float) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_temp(t)


def llama_sampler_init_temp(t: float) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_temp(t)


def c_llama_sampler_init_temp_ext(t: float, delta: float, exponent: float) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_temp_ext(t, delta, exponent)


def llama_sampler_init_temp_ext(t: float, delta: float, exponent: float) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_temp_ext(t, delta, exponent)


def c_llama_sampler_init_xtc(p: float, t: float, min_keep: int, seed: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_xtc(p, t, min_keep, seed)


def llama_sampler_init_xtc(p: float, t: float, min_keep: int, seed: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_xtc(p, t, min_keep, seed)


def c_llama_sampler_init_top_n_sigma(n: float) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_top_n_sigma(n)


def llama_sampler_init_top_n_sigma(n: float) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_top_n_sigma(n)


def c_llama_sampler_init_mirostat(n_vocab: int, seed: int, tau: float, eta: float, m: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_mirostat(n_vocab, seed, tau, eta, m)


def llama_sampler_init_mirostat(n_vocab: int, seed: int, tau: float, eta: float, m: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_mirostat(n_vocab, seed, tau, eta, m)


def c_llama_sampler_init_mirostat_v2(seed: int, tau: float, eta: float) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_mirostat_v2(seed, tau, eta)


def llama_sampler_init_mirostat_v2(seed: int, tau: float, eta: float) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_mirostat_v2(seed, tau, eta)


def c_llama_sampler_init_grammar(vocab: 'LlamaVocabPointer', grammar_str: bytes,
                                 grammar_root: bytes) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_grammar(vocab, grammar_str, grammar_root)


def llama_sampler_init_grammar(vocab: 'LlamaVocabPointer', grammar_str: bytes,
                               grammar_root: bytes) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_grammar(vocab, grammar_str, grammar_root)


def c_llama_sampler_init_grammar_lazy(vocab: 'LlamaVocabPointer', grammar_str: bytes, grammar_root: bytes,
                                      trigger_words, num_trigger_words: int, trigger_tokens: 'LlamaTokenPointer',
                                      num_trigger_tokens: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_grammar_lazy(vocab, grammar_str, grammar_root, trigger_words, num_trigger_words,
                                                 trigger_tokens, num_trigger_tokens)


def llama_sampler_init_grammar_lazy(vocab: 'LlamaVocabPointer', grammar_str: bytes, grammar_root: bytes, trigger_words,
                                    num_trigger_words: int, trigger_tokens: 'LlamaTokenPointer',
                                    num_trigger_tokens: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_grammar_lazy(vocab, grammar_str, grammar_root, trigger_words, num_trigger_words,
                                             trigger_tokens, num_trigger_tokens)


def c_llama_sampler_init_grammar_lazy_patterns(vocab: 'LlamaVocabPointer', grammar_str: bytes, grammar_root: bytes,
                                               trigger_patterns, num_trigger_patterns: int,
                                               trigger_tokens: 'LlamaTokenPointer',
                                               num_trigger_tokens: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_grammar_lazy_patterns(vocab, grammar_str, grammar_root, trigger_patterns,
                                                          num_trigger_patterns, trigger_tokens, num_trigger_tokens)


def llama_sampler_init_grammar_lazy_patterns(vocab: 'LlamaVocabPointer', grammar_str: bytes, grammar_root: bytes,
                                             trigger_patterns, num_trigger_patterns: int,
                                             trigger_tokens: 'LlamaTokenPointer',
                                             num_trigger_tokens: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_grammar_lazy_patterns(vocab, grammar_str, grammar_root, trigger_patterns,
                                                      num_trigger_patterns, trigger_tokens, num_trigger_tokens)


def c_llama_sampler_init_penalties(penalty_last_n: int, penalty_repeat: float, penalty_freq: float,
                                   penalty_present: float) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_penalties(penalty_last_n, penalty_repeat, penalty_freq, penalty_present)


def llama_sampler_init_penalties(penalty_last_n: int, penalty_repeat: float, penalty_freq: float,
                                 penalty_present: float) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_penalties(penalty_last_n, penalty_repeat, penalty_freq, penalty_present)


def c_llama_sampler_init_dry(vocab: 'LlamaVocabPointer', n_ctx_train: int, dry_multiplier: float, dry_base: float,
                             dry_allowed_length: int, dry_penalty_last_n: int, seq_breakers,
                             num_breakers: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_dry(vocab, n_ctx_train, dry_multiplier, dry_base, dry_allowed_length,
                                        dry_penalty_last_n, seq_breakers, num_breakers)


def llama_sampler_init_dry(vocab: 'LlamaVocabPointer', n_ctx_train: int, dry_multiplier: float, dry_base: float,
                           dry_allowed_length: int, dry_penalty_last_n: int, seq_breakers,
                           num_breakers: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_dry(vocab, n_ctx_train, dry_multiplier, dry_base, dry_allowed_length,
                                    dry_penalty_last_n, seq_breakers, num_breakers)


def c_llama_sampler_init_adaptive_p(target: float, decay: float, seed: int) -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_adaptive_p(target, decay, seed)


def llama_sampler_init_adaptive_p(target: float, decay: float, seed: int) -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_adaptive_p(target, decay, seed)


def c_llama_sampler_init_logit_bias(n_vocab: int, n_logit_bias: int,
                                    logit_bias: 'LlamaLogitBiasPointer') -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_logit_bias(n_vocab, n_logit_bias, logit_bias)


def llama_sampler_init_logit_bias(n_vocab: int, n_logit_bias: int,
                                  logit_bias: 'LlamaLogitBiasPointer') -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_logit_bias(n_vocab, n_logit_bias, logit_bias)


def c_llama_sampler_init_infill(vocab: 'LlamaVocabPointer') -> 'LlamaSamplerPointer':
    return llama.llama_sampler_init_infill(vocab)


def llama_sampler_init_infill(vocab: 'LlamaVocabPointer') -> 'LlamaSamplerPointer':
    return c_llama_sampler_init_infill(vocab)


def c_llama_sampler_get_seed(smpl: 'LlamaSamplerPointer') -> int:
    return llama.llama_sampler_get_seed(smpl)


def llama_sampler_get_seed(smpl: 'LlamaSamplerPointer') -> int:
    return c_llama_sampler_get_seed(smpl)


def c_llama_sampler_sample(smpl: 'LlamaSamplerPointer', ctx: 'LlamaContextPointer', idx: int) -> Any:
    return llama.llama_sampler_sample(smpl, ctx, idx)


def llama_sampler_sample(smpl: 'LlamaSamplerPointer', ctx: 'LlamaContextPointer', idx: int) -> Any:
    return c_llama_sampler_sample(smpl, ctx, idx)


def c_llama_split_path(split_path: bytes, maxlen: int, path_prefix: bytes, split_no: int, split_count: int) -> int:
    return llama.llama_split_path(split_path, maxlen, path_prefix, split_no, split_count)


def llama_split_path(split_path: bytes, maxlen: int, path_prefix: bytes, split_no: int, split_count: int) -> int:
    return c_llama_split_path(split_path, maxlen, path_prefix, split_no, split_count)


def c_llama_split_prefix(split_prefix: bytes, maxlen: int, split_path: bytes, split_no: int, split_count: int) -> int:
    return llama.llama_split_prefix(split_prefix, maxlen, split_path, split_no, split_count)


def llama_split_prefix(split_prefix: bytes, maxlen: int, split_path: bytes, split_no: int, split_count: int) -> int:
    return c_llama_split_prefix(split_prefix, maxlen, split_path, split_no, split_count)


def c_llama_print_system_info() -> bytes:
    return llama.llama_print_system_info()


def llama_print_system_info() -> bytes:
    return c_llama_print_system_info()


def c_llama_log_get(log_callback, user_data):
    return llama.llama_log_get(log_callback, user_data)


def llama_log_get(log_callback, user_data):
    return c_llama_log_get(log_callback, user_data)


def c_llama_log_set(log_callback, user_data):
    return llama.llama_log_set(log_callback, user_data)


def llama_log_set(log_callback, user_data):
    return c_llama_log_set(log_callback, user_data)


def c_llama_perf_context(ctx: 'LlamaContextPointer') -> 'LlamaPerfContextData':
    return llama.llama_perf_context(ctx)


def llama_perf_context(ctx: 'LlamaContextPointer') -> 'PyLlamaPerfContextData':
    return c_llama_perf_context(ctx).py


def c_llama_perf_context_print(ctx: 'LlamaContextPointer'):
    return llama.llama_perf_context_print(ctx)


def llama_perf_context_print(ctx: 'LlamaContextPointer'):
    return c_llama_perf_context_print(ctx)


def c_llama_perf_context_reset(ctx: 'LlamaContextPointer'):
    return llama.llama_perf_context_reset(ctx)


def llama_perf_context_reset(ctx: 'LlamaContextPointer'):
    return c_llama_perf_context_reset(ctx)


def c_llama_perf_sampler(chain: 'LlamaSamplerPointer') -> 'LlamaPerfSamplerData':
    return llama.llama_perf_sampler(chain)


def llama_perf_sampler(chain: 'LlamaSamplerPointer') -> 'PyLlamaPerfSamplerData':
    return c_llama_perf_sampler(chain).py


def c_llama_perf_sampler_print(chain: 'LlamaSamplerPointer'):
    return llama.llama_perf_sampler_print(chain)


def llama_perf_sampler_print(chain: 'LlamaSamplerPointer'):
    return c_llama_perf_sampler_print(chain)


def c_llama_perf_sampler_reset(chain: 'LlamaSamplerPointer'):
    return llama.llama_perf_sampler_reset(chain)


def llama_perf_sampler_reset(chain: 'LlamaSamplerPointer'):
    return c_llama_perf_sampler_reset(chain)


def c_llama_opt_param_filter_all(tensor, userdata) -> int:
    return llama.llama_opt_param_filter_all(tensor, userdata)


def llama_opt_param_filter_all(tensor, userdata) -> int:
    return c_llama_opt_param_filter_all(tensor, userdata)


def c_llama_opt_init(lctx: 'LlamaContextPointer', model: 'LlamaModelPointer', lopt_params: 'LlamaOptParams'):
    return llama.llama_opt_init(lctx, model, lopt_params)


def llama_opt_init(lctx: 'LlamaContextPointer', model: 'LlamaModelPointer', lopt_params: 'PyLlamaOptParams'):
    return c_llama_opt_init(lctx, model, lopt_params.c)


def c_llama_opt_epoch(lctx: 'LlamaContextPointer', dataset, result_train, result_eval, idata_split: int, callback_train,
                      callback_eval):
    return llama.llama_opt_epoch(lctx, dataset, result_train, result_eval, idata_split, callback_train, callback_eval)


def llama_opt_epoch(lctx: 'LlamaContextPointer', dataset, result_train, result_eval, idata_split: int, callback_train,
                    callback_eval):
    return c_llama_opt_epoch(lctx, dataset, result_train, result_eval, idata_split, callback_train, callback_eval)
