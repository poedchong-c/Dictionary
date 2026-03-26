from fastapi import FastAPI
from routes import word, category

app = FastAPI()

# Include routers 
app.include_router(word.router)
app.include_router(category.router)

# GET
@app.get("/")
def read_root():
    return {"message": "GET works"}

# POST
@app.post("/items")
def create_item():
    return {"message": "POST works"}

# PUT
@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": f"PUT works {item_id}"}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"DELETE works {item_id}"}