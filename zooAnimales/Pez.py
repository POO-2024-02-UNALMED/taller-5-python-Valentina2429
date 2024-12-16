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
    def set_listado(cls, listado):
        cls.listado = listado

    @classmethod
    def get_listado(cls):
        return cls.listado

    def set_color_escamas(self, color_escamas):
        self.color_escamas = color_escamas

    def get_color_escamas(self):
        return self.color_escamas

    def set_cantidad_aletas(self, cantidad_aletas):
        self.cantidad_aletas = cantidad_aletas

    def get_cantidad_aletas(self):
        return self.cantidad_aletas

    @classmethod
    def cantidad_peces(cls):
        return len(cls.listado)

    @staticmethod
    def movimiento():
        return "nadar"

    @classmethod
    def crear_salmon(cls, nombre, edad, genero):
        salmon = cls(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return salmon

    @classmethod
    def crear_bacalao(cls, nombre, edad, genero):
        bacalao = cls(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return bacalao
