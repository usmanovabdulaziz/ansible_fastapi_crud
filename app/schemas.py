from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str

class ItemResponse(ItemCreate):
    id: int
    class Config:
        from_attributes = True