class Persona:
    def __init__(self, nombre, edad,caracteristicas):
        self.nombre = nombre
        self.edad = edad
        self.caracteristicas= caracteristicas

# Python internamente hace algo equivalente a:
# Persona.__init__(ana, "Ana García", 28)

# Creamos dos objetos Persona
ana = Persona("Ana García", 28,"Alta,Delgada,Morena")
juan = Persona("Juan López", 35,"Bajo,Compostura media")

# Accedemos a sus atributos
print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35
print(ana.caracteristicas)
print(juan.caracteristicas)