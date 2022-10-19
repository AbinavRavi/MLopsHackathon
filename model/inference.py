import pickle
from train import clean_text

def inference(tweet: str):
    preprocessed_text = clean_text(tweet)
    load_model = pickle.load("model.pkl")
    prediction = load_model.predict(preprocessed_text)
    return prediction