# se importa la clase BaseCommand de django.core.management.base para crear un comando personalizado de Django. 
from django.core.management.base import BaseCommand
import time # se importa 
import random
from django.utils import timezone

# se crea la clase AGV, para representar un vehículo guiado automáticamente (AGV) con atributos como id_carro, posicion_actual y direccion.
class AGV:
    # se define el método __init__ que inicializa los atributos id_carro, posicion_actual y direccion de la instancia de AGV.
    def __init__(self, id_carro, posicion_actual, direccion):
        self.id_carro = id_carro
        self.posicion_actual = posicion_actual
        self.direccion = direccion
    # se crea el método avanzar que actualiza la posición del AGV según la dirección y los sensores.
    def avanzar(self):
        # se cre un if para determinar la lista de sensores actual según la dirección del AGV.
        if self.direccion == "ida":
            lista_actual = sensores_ida

        else:
            lista_actual = sensores_vuelta
        # se obtiene el índice de la posición actual del AGV en la lista de sensores correspondiente.
        indice_actual = lista_actual.index(self.posicion_actual)
        # se verifica si el AGV ha llegado al final de la lista de sensores y se actualiza la dirección y la posición en consecuencia.
        if indice_actual < len(lista_actual) - 1:
            self.posicion_actual = lista_actual[indice_actual + 1]
        else:
            self.direccion = "ida" if self.direccion == "vuelta" else "vuelta"

            # se actualiza la posición del AGV al primer sensor de la nueva dirección.
            if self.direccion == "ida":
                self.posicion_actual = sensores_ida[0]
            else:
                self.posicion_actual = sensores_vuelta[0]

         
        

    
# se crean variables listas que contienen los identificadores de los sensores para la ida y la vuelta del recorrido del AGV.
sensores_ida = ["segmento_1", "segmento_2", "segmento_3", "segmento_4", "segmento_5"]
sensores_vuelta = ["segmento_6", "segmento_7", "segmento_8", "segmento_9", "segmento_10"]
# La clase Command hereda de BaseCommand y define el método handle, que se ejecuta cuando se llama al comando. 
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        carro_1 = AGV("Carro_1", "segmento_1", "ida")
        carro_2 = AGV("Carro_2", "segmento_1", "ida")
        carro_3 = AGV("Carro_3", "segmento_1", "ida")
        print("Simulacion iniciada")

