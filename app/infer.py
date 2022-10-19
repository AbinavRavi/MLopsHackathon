from pydantic import BaseModel
from fastapi import FastAPI, status

app = FastAPI()

class ModelInput(BaseModel):
    tweet: str

class ModelOutput(BaseModel):
    person: str

@app.get('/', status_code=status.HTTP_200_OK)
def run_inference(req: ModelInput):
    pass

if __name__ == "__main__":
    run_inference()
