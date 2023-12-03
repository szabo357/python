from fastapi import FastAPI

# to run the code uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def root():
    """Root endpoint of out API
    it returns "Hello World!" """
    return {"message": "Hello World!"}