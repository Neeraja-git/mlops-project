from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello i am learning and succesfully doploy this my first achievment while learning  MLOps"}
