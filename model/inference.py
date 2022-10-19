from cgi import test
import joblib
import pickle
import numpy as np
from train import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer

def inference(tweet: str):
    preprocessed_text = clean_text(tweet)
    converted_text = np.array(preprocessed_text).reshape(-1)
    load_model = joblib.load("model.joblib")
    tf1 = pickle.load(open("tfidf.pickle", 'rb'))
    test_vec = tf1.transform(converted_text)
    prediction = load_model.predict(test_vec)
    return prediction

if __name__ == "__main__":
    inference("doge to the moon")