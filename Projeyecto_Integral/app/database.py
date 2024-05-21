from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .main import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    currentAddress = Column(String, index=True)

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, index=True)
    lastName = Column(String, index=True)
    userEmail = Column(String, unique=True, index=True)
    gender = Column(String, index=True)
    userNumber = Column(String, index=True)
    dateOfBirthInput = Column(String, index=True)
    state = Column(String, index=True)
    city = Column(String, index=True)

# Luego, aquí puedes agregar más columnas y relaciones según tus necesidades.
