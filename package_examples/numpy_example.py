""" Type hinting example for NumPy
pip install numpy <- types included since 1.20
"""
import numpy as np
from numpy.typing import NDArray

def normalize(arr: NDArray[np.float64]) -> NDArray[np.float64]:
    return (arr - arr.mean()) / arr.std()

data: np.ndarray

# Type aliases for clarity
type Features = NDArray[np.float64]
Labels = NDArray[np.int32]

def train(X: Features, y: Labels) -> dict[str, Features]:
    weights = np.mean(X, axis=0)
    return {"weights": weights}