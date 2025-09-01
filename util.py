# util.py
import os
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

# Always resolve paths relative to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_estimated_price(location, sqft, bhk, bath):
    global __data_columns, __model
    if __data_columns is None or __model is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")

    try:
        loc_index = __data_columns.index(location.lower())
    except Exception:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns, __locations, __model

    try:
        # Load columns.json safely
        with open(os.path.join(BASE_DIR, "artifacts", "columns.json"), "r") as f:
            __data_columns = json.load(f)["data_columns"]
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
        print(f"Loaded columns.json with {len(__data_columns)} columns")

        # Load the trained model (lasso)
        if __model is None:
            model_path = os.path.join(
                BASE_DIR, "artifacts", "bangalore_home_prices_lasso_model.pickle"
            )
            with open(model_path, "rb") as f:
                __model = pickle.load(f)
            print("Model loaded successfully")

    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error while loading artifacts: {e}")
        raise

    print("loading saved artifacts...done")


def get_location_names():
    global __locations
    if __locations is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")
    return __locations


def get_data_columns():
    global __data_columns
    if __data_columns is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")
    return __data_columns


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names()[:10])  # show only first 10 locations
    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))
    print(get_estimated_price("Kalhalli", 1000, 2, 2))  # other location
    print(get_estimated_price("Ejipura", 1000, 2, 2))  # other location
