from bianca.bootstrap import *
from bianca.llama_router import *

__all__ = ["ModelProfileRegistry"]

MODEL_PROFILE = PROJECT_DIR / "model_profile.json"


class ModelProfileRegistry(dict[str, ModelProfile]):
    def __init__(self):
        dict.__init__(self)
        self.reload()

    def reload(self):
        reg = {}
        dat = json.loads(MODEL_PROFILE.read_text())

        def _get_config(profile_name: str) -> ModelProfile:
            if profile_name in reg:
                return reg[profile_name]

            profile = dat[profile_name]
            profile_model = profile["model"]
            profile_kwargs = {
                "model_kwargs": profile.get("model_params", {}),
                "context_kwargs": profile.get("context_params", {}),
                "sampler_chain_kwargs": profile.get("sampler_chain_params", {}),
                "sampler_kwargs": profile.get("sampler_params", {}),
                "system_prompt": profile.get("system_prompt"),
                "fallback": _get_config(profile["fallback"]) if profile.get("fallback") else None
            }

            if profile_model in dat:
                reg[profile_name] = _get_config(profile_model).fork(**profile_kwargs)
            else:
                reg[profile_name] = ModelProfile(str(PROJECT_DIR / profile_model), **profile_kwargs)

            return reg[profile_name]

        for it in dat:
            _get_config(it)

        dict.__init__(self, reg)
