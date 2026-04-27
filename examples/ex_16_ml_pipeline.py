import pandas as pd
import numpy as np
from numpy.typing import NDArray
from typing import TypeAlias

# Clear type aliases make the code self-documenting
Features: TypeAlias = NDArray[np.float64]
Labels: TypeAlias = NDArray[np.int32]
Predictions: TypeAlias = NDArray[np.int32]
Accuracy: TypeAlias = float


def load_data(filepath: str) -> pd.DataFrame:
    """Load the dataset from CSV."""
    return pd.read_csv(filepath)


def prepare_features(df: pd.DataFrame) -> tuple[Features, Labels]:
    """
    Split dataframe into features (X) and labels (y).
    Returns arrays ready for training.
    """
    X = df.drop('target', axis=1).values
    y = df['target'].values
    return X, y


def train_model(X_train: Features, y_train: Labels) -> dict[str, Features]:
    """
    Train a simple model and return learned weights.
    In real life, this would be a scikit-learn model or neural network.
    """
    # Simplified: just store mean of each feature as "model"
    weights = np.mean(X_train, axis=0)
    return {"weights": weights}


def predict(X_test: Features, model: dict[str, Features]) -> Predictions:
    """Make predictions using the trained model."""
    # Simplified prediction logic
    weights = model["weights"]
    predictions = (X_test > weights).astype(np.int32).sum(axis=1)
    return predictions % 2  # Some binary classification


def evaluate(y_true: Labels, y_pred: Predictions) -> Accuracy:
    """Calculate accuracy score."""
    correct = np.sum(y_true == y_pred)
    return float(correct / len(y_true))


# Run the complete pipeline
def run_pipeline(train_path: str, test_path: str) -> Accuracy:
    """Complete ML pipeline from data to evaluation."""
    # Load and prepare training data
    train_df = load_data(train_path)
    X_train, y_train = prepare_features(train_df)

    # Train model
    model = train_model(X_train, y_train)

    # Load and prepare test data
    test_df = load_data(test_path)
    X_test, y_test = prepare_features(test_df)

    # Predict and evaluate
    predictions = predict(X_test, model)
    accuracy = evaluate(y_test, predictions)

    return accuracy


if __name__ == "__main__":
    final_accuracy = run_pipeline("data/train.csv", "data/test.csv")
    print(f"Model accuracy: {final_accuracy:.2%}")