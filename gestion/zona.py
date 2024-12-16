

class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []


    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setZoo(self, zoo):
        self.zoo = zoo

    def getZoo(self):
        return self.zoo

    def setAnimales(self, animales):
        self.animales = animales

    def getAnimales(self):
        return self.animales

    def agregarAnimales(self, nuevo):
        self.animales.append(nuevo)

    def cantidadAnimales(self):
        return len(self.animales)
