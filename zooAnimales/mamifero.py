from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0


    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje=False, patas=0):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado

    @classmethod
    def getListado(cls):
        return cls.listado

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def isPelaje(self):
        return self.pelaje

    def setPatas(self, patas):
        self.patas = patas

    def getPatas(self):
        return self.patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = cls(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = cls(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon
