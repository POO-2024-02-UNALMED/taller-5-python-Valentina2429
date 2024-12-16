from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0


    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_escamas=None, cantidad_aletas=0):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado

    @classmethod
    def getListado(cls):
        return cls.listado

    def setColorEscamas(self, color_escamas):
        self.color_escamas = color_escamas

    def getColorEscamas(self):
        return self.color_escamas

    def setCantidadAletas(self, cantidad_aletas):
        self.cantidad_aletas = cantidad_aletas

    def getCantidadAletas(self):
        return self.cantidad_aletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)

    @staticmethod
    def movimiento():
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = cls(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = cls(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return bacalao
