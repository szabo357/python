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


# order matters 
"""When creating path operations, you can find situations where you have a fixed path.
Like /users/me, let's say that it's to get data about the current user.
And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.
Because path operations are evaluated in order, you need to make sure that the path 
for /users/me is declared before the one for /users/{user_id}:"""

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}