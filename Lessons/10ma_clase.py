from abc import ABC, abstractmethod

class Publication(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display_info(self):
        pass

class Author(Publication):
    def __init__(self, name, title):
        # uso super para instanciar el constructor de Publicacion
        super().__init__(title)
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Publication: {self.title}")

class Book(Publication):
    def __init__(self, title, authors):
        # uso super para instanciar el constructor de Publicacion
        super().__init__(title)
        self.authors = authors

    def display_info(self):
        print(f"Title: {self.title}")
        print("Authors:")
        for author in self.authors:
            print(f"- {author.name}")
        print(f"Publication: {self.title}")

# Creo una instancia de la clase Publication
publication = Book("Python Programming", [])

# Creo autores y libros utilizando la misma instancia de Publication
author1 = Author("John Doe", publication)
author2 = Author("Jane Smith", publication)

book1 = Book("Python Programming", [author1])
book2 = Book("Data Science Basics", [author1, author2])
book3 = Book("Web Development", [author2])

# Muestro la información de los autores y los libros
print("Información de los autores:")
author1.display_info()
print()
author2.display_info()
print()

print("Información de los libros:")
book1.display_info()
print()
book2.display_info()
print()
book3.display_info()
