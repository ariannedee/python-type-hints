""" Type hinting example for Hugging Face transformers
pip install torch
pip install transformers <- types included
"""
from transformers import (
    PreTrainedModel,
    PreTrainedTokenizer,
    AutoModel,
    AutoTokenizer
)
import torch

def load_model(name: str) -> tuple[PreTrainedModel, PreTrainedTokenizer]:
    model = AutoModel.from_pretrained(name)
    tokenizer = AutoTokenizer.from_pretrained(name)
    return model, tokenizer

def get_embeddings(
    text: str,
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizer
) -> torch.Tensor:
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :]