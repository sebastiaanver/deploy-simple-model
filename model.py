from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from typing import Dict, Any
from pathlib import Path
import yaml
import pickle

TRAINING = False


def main(config: Dict[str, Any]) -> None:
    # Load data.
    iris_data = load_iris()
    X = iris_data['data']
    y = iris_data['target']

    # Set up model.
    model = ElasticNet(random_state=0)

    # Train model.
    if TRAINING:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)
        model.fit(X_train, y_train)

    else:
        model.fit(X, y)  # If not training; use all available data

    # Store mode object.
    with open(config["model_name"], 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    config = yaml.load(Path("config.yml").read_text(), Loader=yaml.SafeLoader)
    main(config)
