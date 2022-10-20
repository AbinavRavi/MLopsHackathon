
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from model.inference import inference
import requests
import os

app = FastAPI()

class InferRequest(BaseModel):
    tweet: str


@app.post('/infer')
def run_inference(infer_request: InferRequest):
    text = infer_request.tweet
    print(text)
    prediction = inference(text)
    if prediction == 0:
        pred = "elon"
    else:
        pred = "kanye"
    next_request = {
        "tweet" : text,
        "prediction" : pred
    }
    headers = {"Content-Type":"application/json"}
    response = requests.post(os.getenv("streamlit"), headers=headers, data=next_request)
    return response
