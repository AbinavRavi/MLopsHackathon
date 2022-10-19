
from fastapi import FastAPI, status
from model.inference import inference

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def run_inference(req: str):
    prediction = inference(req)
    return req, prediction
