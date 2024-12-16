from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_piel=None, venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado

    @classmethod
    def getListado(cls):
        return cls.listado

    def setColorPiel(self, color_piel):
        self.color_piel = color_piel

    def getColorPiel(self):
        return self.color_piel

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso

    def isVenenoso(self):
        return self.venenoso

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crearRana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra

