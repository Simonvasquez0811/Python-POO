class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Validamos el precio antes de asignarlo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    # Los métodos para acceder y modificar vendrán en la siguiente sección
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido (convención)
        self.__modelo = modelo   # Privado (name mangling)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        # Podemos acceder a _marca (protegido)
        print(f"Marca: {self._marca}")

        # Esto generará un AttributeError
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("No se puede acceder a __modelo desde la subclase")

# ...código existente...

coche = Coche("Toyota", "Corolla", 4)
coche.info()