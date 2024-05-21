from pydantic import BaseModel
from typing import List
from .adress import Address


class Person(BaseModel):
    firstName: str
    lastName: str
    userEmail: str
    gender: str
    userNumber: str
    dateOfBirthInput: str
    subjects: List[str]
    hobbies: List[str]
    state: str
    city: str
    addresses: List[Address]

    class Config:
        orm_mode = True