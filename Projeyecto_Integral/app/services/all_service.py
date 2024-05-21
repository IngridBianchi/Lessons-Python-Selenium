from fastapi import FastAPI, HTTPException
from typing import List
from models import Address, Person

app = FastAPI()

# Mock data
address_db = [{"currentAddress": "Celestino Marco 1609"}]
person_db = [{
    "firstName": "Alejandro",
    "lastName": "Arrua",
    "userEmail": "vp.arrua@gmail.com",
    "gender": "Male",
    "userNumber": "034315441034",
    "dateOfBirthInput": "09 July 1994",
    "subjects": ["English","Maths","Physics","Chemistry","Accounting","Arts"],
    "hobbies": ["Sports","Music"],
    "state": "NCR",
    "city": "Delhi"
}]

@app.get("/addresses/", response_model=List[Address])
async def get_addresses():
    return address_db

@app.post("/addresses/", response_model=Address)
async def create_address(address: Address):
    address_db.append(address)
    return address

@app.get("/persons/", response_model=List[Person])
async def get_persons():
    return person_db

@app.post("/persons/", response_model=Person)
async def create_person(person: Person):
    person_db.append(person)
    return person