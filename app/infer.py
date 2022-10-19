
from fastapi import FastAPI, status
from model.inference import inference

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def run_inference(req: ModelInput):
    pass

if __name__ == "__main__":
    run_inference()
