# Def ClaseVehiculo(tipo,color):

# Esta funcion devuelve un objeto instanciado de la clase vehiculo
# la cual debe tener los siguientes atributos :
# Tipo : Un valor dentro de ['auto','camioneta','moto']
# Color : Un valor de tipo de dato string
# Velocidad : Un valor de tipo de dato float, que debe inicializarse en 0
# y debe tener el siguiente metodo:
# Acelerar (): Este metodo recibe un parametro con el valor que debe incrementar
# a la propiedad velocidad y luego retornarla
# Si la propiedad velocidad cobra un valor menor a 0 que en 0
# Si la propiedad velocidad cobra un valor mayor a 100 queda en 100

class Vehiculo:
    velocidad = 0
    def __init__(self, t, c):
        self.tipo = t
        self.color = c
    def Acelerar(numero):
        velocidad = velocidad + numero
        if velocidad < 0:
            velocidad = 0
        elif velocidad > 100:
            velocidad = 100
        return velocidad
    
coche = Vehiculo('auto','negro')
coche.Acelerar(20)
print(coche.velocidad)