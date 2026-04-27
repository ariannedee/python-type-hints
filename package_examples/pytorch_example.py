""" Type hinting example for PyTorch
pip install torch <- types included since Python 3.8
"""
from torch import nn, Tensor, optim

# Tensors and models
def forward_pass(x: Tensor, model: nn.Module) -> Tensor:
    return model(x)

def train_step(
    model: nn.Module,
    data: Tensor,
    labels: Tensor,
    optimizer: optim.Optimizer,
    loss_fn: nn.Module
) -> float:
    optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, labels)
    loss.backward()
    optimizer.step()
    return loss.item()