import pickle
import os
import numpy as np
from sklearn.ensemble import RandomForestRegressor

MODEL_PATH = "models/ats_model.pkl"


def train_model():

    # Sample training data
    X = np.array([
        [5, 2, 3],
        [8, 3, 4],
        [2, 1, 1],
        [10, 5, 6],
        [7, 2, 5],
        [3, 1, 2]
    ])

    y = np.array([65, 80, 40, 90, 75, 50])

    model = RandomForestRegressor()

    model.fit(X, y)

    os.makedirs("models", exist_ok=True)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)


def load_model():

    if not os.path.exists(MODEL_PATH):
        train_model()

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    return model


def predict_score(skills, experience, projects):

    model = load_model()

    score = model.predict([[skills, experience, projects]])

    return int(score[0])
