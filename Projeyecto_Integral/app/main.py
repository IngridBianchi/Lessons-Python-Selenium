from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la conexión a la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Crea la instancia de la aplicación FastAPI
app = FastAPI()

# Crea el motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea una sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase base para las clases de modelos SQLAlchemy
Base = declarative_base()
