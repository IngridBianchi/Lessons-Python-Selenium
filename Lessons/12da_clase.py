from marshmallow import Schema, fields, validates ,ValidationError
from abc import ABC, abstractmethod
import jsonschema

# Defino el esquema con Marshmallow
class PublicationSchema(Schema):
    title = fields.Str(required=True)

class AuthorSchema(Schema):
    name = fields.Str(required=True)
    publication = fields.Nested(PublicationSchema, required=True)

# Clase abstracta para la publicacion
class Publication(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display_info(self):
        pass

# Clase Book que implementa la publicacin
class Book(Publication):
    def __init__(self, title, authors):
        super().__init__(title)
        self.authors = authors

    def display_info(self):
        print(f"Title: {self.title}")
        print("Authors:")
        for author in self.authors:
            print(f"- {author['name']}")
        print(f"Publication: {self.title}")

# JSON Schema para validar
json_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "publication": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        },
        "required": ["name", "publication"]
    }
}

# Funcion para cargar y validar el JSON
def load_json(json_data, schema):
    try:
        jsonschema.validate(instance=json_data, schema=schema)
        return json_data
    except jsonschema.exceptions.ValidationError as e:
        print(f"Error de validación JSON: {e}")
        return None

# JSON de ejemplo
json_data = [
    {"name": "John Doe", "publication": {"title": "Python Programming"}},
    {"name": "Jane Smith", "publication": {"title": "Data Science Basics"}}
]

# Creo instancias de los esquemas
author_schema = AuthorSchema()

# Cargo y valido el JSON
data = load_json(json_data, json_schema)

# Imprimo
if data:
    for author_data in data:
        title = author_data["publication"]["title"]
        authors = [author_data]
        book = Book(title, authors)
        book.display_info()
        print()
