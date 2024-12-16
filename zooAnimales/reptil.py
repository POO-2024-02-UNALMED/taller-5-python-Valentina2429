from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_escamas=None, largo_cola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)


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

    def setLargoCola(self, largo_cola):
        self.largo_cola = largo_cola

    def getLargoCola(self):
        return self.largo_cola

    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return iguana

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return serpiente
