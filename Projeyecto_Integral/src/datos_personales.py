
class DatosPersonales:
    def __init__(self, first_name, last_name, email, gender, mobile, date_of_birth, subjects, hobbies, state, city):
        self.firstName = first_name
        self.lastName = last_name
        self.userEmail = email
        self.gender = gender
        self.userNumber = mobile
        self.dateOfBirthInput = date_of_birth
        self.subjects = subjects
        self.hobbies = hobbies
        self.state = state
        self.city = city
    def __str__(self):
        return f"Nombre: {self.firstName}, Apellido: {self.lastName}, Email: {self.userEmail}, Genero: {self.gender}, Mobil: {self.userNumber}, Nacimiento: {self.dateOfBirthInput}, Materias: [{self.subjects}, Hobbies: [{self.hobbies}], Estado: {self.state}, Ciudad: {self.city}"
    def get_fullName(self):
        return self.lastName + " " + self.firstName

