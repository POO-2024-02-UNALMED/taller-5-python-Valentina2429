from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0


    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_plumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado

    @classmethod
    def getListado(cls):
        return cls.listado

    def setColorPlumas(self, color_plumas):
        self.color_plumas = color_plumas

    def getColorPlumas(self):
        return self.color_plumas

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return halcon

    @staticmethod
    def crearAguila(nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return aguila
