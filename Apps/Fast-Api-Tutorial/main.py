from fastapi import FastAPI

# to run the code uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}