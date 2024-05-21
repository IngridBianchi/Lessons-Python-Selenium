class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

empleado1 = Empleado("Juancito", 3000)
empleado2 = Empleado("Mariano", 2500)
empleado3 = Empleado("Pedrito", 3500)
empleado4 = Empleado("Ana", 4000)

empleados = [empleado1, empleado2, empleado3, empleado4]

umbral_salario = 3000

empleados_con_salario_superior = {empleado.nombre: empleado.salario for empleado in empleados if empleado.salario > umbral_salario}

print(empleados_con_salario_superior)
