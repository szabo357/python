from fastapi import FastAPI

# to run the code uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def root():
    """Root endpoint of out API
    it returns "Hello World!" """
    return {"message": "Hello World!"}

# Declaring Path with parameters or variables

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# Path parameters with Types
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
