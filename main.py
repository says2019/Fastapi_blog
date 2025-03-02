from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hw():
    return "hello world"