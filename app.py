import pickle
import numpy as np
import yaml
from flask import Flask, request
from pathlib import Path
from typing import Dict, Any

model = None
app = Flask(__name__)


def load_model(config: Dict[str, Any]) -> None:
    global model
    with open(config["model_name"], "rb") as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint() -> None:
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction() -> str:
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
        prediction = model.predict(data)  # runs globally loaded model on the data
    return str(prediction[0])


if __name__ == '__main__':
    config = yaml.load(Path("config.yml").read_text(), Loader=yaml.SafeLoader)
    load_model(config)
    app.run(host='0.0.0.0', port=5000)
