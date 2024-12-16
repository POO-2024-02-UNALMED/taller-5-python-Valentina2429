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
    def set_listado(cls, listado):
        cls.listado = listado

    @classmethod
    def get_listado(cls):
        return cls.listado

    def set_pelaje(self, pelaje):
        self.pelaje = pelaje

    def is_pelaje(self):
        return self.pelaje

    def set_patas(self, patas):
        self.patas = patas

    def get_patas(self):
        return self.patas

    @classmethod
    def cantidad_mamiferos(cls):
        return len(cls.listado)

    @classmethod
    def crear_caballo(cls, nombre, edad, genero):
        caballo = cls(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo

    @classmethod
    def crear_leon(cls, nombre, edad, genero):
        leon = cls(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon
