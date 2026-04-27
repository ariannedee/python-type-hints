""" Type hinting example for Pandas
pip install scikit-learn
pip install git+https://github.com/microsoft/python-type-stubs.git  <- Microsoft's maintained stubs
"""
from sklearn.base import BaseEstimator
import numpy as np
from numpy.typing import NDArray

def train_classifier(
    model: BaseEstimator,
    X: NDArray[np.float64],
    y: NDArray[np.int32]
) -> BaseEstimator:
    return model.fit(X, y)

def predict(
    model: BaseEstimator,
    X: NDArray[np.float64]
) -> NDArray[np.int32]:
    return model.predict(X)