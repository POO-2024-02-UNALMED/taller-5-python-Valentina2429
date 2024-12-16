class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []


    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getUbicacion(self):
        return self.ubicacion

    def setZonas(self, zonas):
        self.zonas = zonas

    def getZonas(self):
        return self.zonas

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        total_animales = sum(zona.cantidad_animales() for zona in self.zonas)
        return total_animales
