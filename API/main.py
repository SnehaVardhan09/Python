from fastapi import FastAPI

app = FastAPI()

@app.get("/")  #endpoint
def home():
    return {"Data": "Testing, World!"}   

