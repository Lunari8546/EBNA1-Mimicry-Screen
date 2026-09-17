from functools import cache

import torch
from transformers import EsmModel, EsmTokenizer

MODEL_NAME = "facebook/esm2_t6_8M_UR50D"

@cache
def _load() -> tuple[EsmModel, EsmTokenizer]:
    model = EsmModel.from_pretrained(MODEL_NAME, add_pooling_layer=False)
    tokenizer = EsmTokenizer.from_pretrained(MODEL_NAME)

    return model, tokenizer

@torch.inference_mode()
def embed(sequence: str) -> torch.Tensor:
    model, tokenizer = _load()

    inputs = tokenizer(sequence, return_tensors="pt", return_special_tokens_mask=True)
    is_special = inputs.pop("special_tokens_mask")

    last_hidden_state = model(**inputs).last_hidden_state

    return last_hidden_state[0][is_special[0] == 0]
