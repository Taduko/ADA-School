class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self,cantidad):
        self.velocidad += cantidad

    def frenar(self,cantidad):
        self.velocidad -= cantidad
    

mi_coche = Coche("Ford", "Focus")


mi_coche.acelerar(50)
print(mi_coche.velocidad)

mi_coche.frenar(20)
print(mi_coche.velocidad)

#https://www.hackerrank.com/domains/algorithms