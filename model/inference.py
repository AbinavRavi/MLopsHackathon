import joblib
import pickle
import numpy as np
from train import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer

def inference(tweet: str):
    preprocessed_text = clean_text(tweet)
    tfidf_vectorizer = TfidfVectorizer()
    converted_text = np.array(preprocessed_text).reshape(-1)
    pickle.load(open("tfidf.pickle", 'rb'))
    test_vec = tfidf_vectorizer.transform(converted_text)
    load_model = joblib.load("model.joblib")
    prediction = load_model.predict(test_vec)
    print(prediction)
    return prediction

if __name__ == "__main__":
    inference("doge to the moon")