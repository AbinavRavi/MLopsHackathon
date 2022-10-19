
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from model.inference import inference

app = FastAPI()

class InferRequest(BaseModel):
    tweet: str


@app.post('/infer', status_code=status.HTTP_200_OK)
def run_inference(infer_request: InferRequest):
    text = infer_request.tweet
    prediction = inference(text)
    if prediction == 0:
        pred = "elon"
    else:
        pred = "kanye"
    response = {
        "tweet" : text,
        "prediction" : pred
    }
    return response
