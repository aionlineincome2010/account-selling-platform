from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Account Selling Platform API is running successfully!"}
