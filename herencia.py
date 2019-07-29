
class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")


class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ronroneo(self):
        print("Ronroneo")

        



firulais = Perro("FIrulais")
firulais.ladrar()
firulais.comer()
firulais.dormir()
print("")
oni = Gato("Oni")
oni.ronroneo()
oni.comer()
oni.dormir()
