
class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.total_animales += 1


    @classmethod
    def setTotalAnimales(cls, total):
        cls.total_animales = total

    @classmethod
    def getTotalAnimales(cls):
        return cls.total_animales

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getHabitat(self):
        return self.habitat

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def setZona(self, zona):
        self.zona = zona

    def getZona(self):
        return self.zona

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        
        return (
            f"Mamiferos: {len(Mamifero.listado)}\n"
            f"Aves: {len(Ave.listado)}\n"
            f"Reptiles: {len(Reptil.listado)}\n"
            f"Peces: {len(Pez.listado)}\n"
            f"Anfibios: {len(Anfibio.listado)}"
        )

    def toString(self):
        if self.zona != None:
            return (
                f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en "
                f"{self.habitat} y mi genero es {self.genero}, la zona en la que me ubico "
                f"es {self.zona.get_nombre()}, en el {self.zona.get_zoo().get_nombre()}"
            )
        
        else:
            return (
                f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en "
                f"{self.habitat} y mi genero es {self.genero}"
            )
