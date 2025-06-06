#crearemos la clase animal

class Animal:
    def __init__(self, nombre):
        self.nombre=nombre
        
    def comer(self):
        print(f"{self.nombre} Esta comiendo")


class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")


class Gato(Animal):
    def correr(self):
        print(f"{self.nombre} esta corriendo")

    def maullar(self):
        print("esta maullando")


#definir objeto para usar la clase
# miperro=Perro("Neron")
# miperro.ladrar()

# migato=Gato("Gati")
# migato.correr()
# migato.maullar()







# perro=Animal("Juan Orlando")
# venezolano=Animal("YOKIRSON YONAILEN MADURO")
# venezolano.correr()
# perro.correr()
# perro.ladrar()
# perro.comer()