from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, Base, engine
from . import crud, schemas, models

# create tables if not exist (for local test)
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(404, "Item not found")
    return updated

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted["deleted"]:
        raise HTTPException(404, "Item not found")
    return deleted