class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []
        

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_ubicacion(self):
        return self.ubicacion

    def set_zonas(self, zonas):
        self.zonas = zonas

    def get_zonas(self):
        return self.zonas

    def agregar_zonas(self, zona):
        self.zonas.append(zona)

    def cantidad_total_animales(self):
        total_animales = sum(zona.cantidad_animales() for zona in self.zonas)
        return total_animales
