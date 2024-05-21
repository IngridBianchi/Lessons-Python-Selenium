from pydantic import BaseModel


class Address(BaseModel):
    currentAddress: str

    class Config:
        orm_mode = True