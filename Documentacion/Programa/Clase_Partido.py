import Datos
import random


#################################################################################################################################
#################################################################################################################################

# Clase Partido
# Herencia: Ninguna
# ------------------------------


# Clase Partido
class Partido:

    def __init__(self, equipo_1, equipo_2, fecha):
        
        if isinstance(fecha, str):


            self.equipo_1 = equipo_1
            self.equipo_2 = equipo_2
            self.goles_1 = 0
            self.goles_2 = 0
            self.fecha = fecha

            self.fase = "Grupos"
            self.id_partido = None
        

        else:
            return f"Error, La fecha es Invalida"
        
    



    # Objetivo; Mostrar el resultado del Partido 

    #E: no recibe parametros aparte de si mismo

    #S: retorna un f"string" que muestra el resultado el resultado de ambos equipos y los goles obtenidos

    #R: ninguna

    def mostrar_resultado(self):
    # ------------------------------


        print(f"{self.equipo_1.pais.codigo_fifa} {self.goles_1} - {self.goles_2} {self.equipo_2.pais.codigo_fifa}")




 
    # Objetivo; Retonar la seleccion ganadora

    #E: no recibe parametros aparte de si mismo

    #S: retorna el objeto equipo con mas goles obtenidos o None en caso de Empate 

    #R: solo puede retornar Empate si esta en fase de grupos

    def generar_ganador(self):
    # ------------------------------


        if self.goles_1 > self.goles_2:

            print(f"Gano: {self.equipo_1.pais.nombre_pais}")
            return self.equipo_1

        elif self.equipo_1 < self.equipo_2:

            print(f"Gano: {self.equipo_2.pais.nombre_pais}")
            return self.equipo_2

        else:
            if self.fase == "Grupos":

                print(f"Empate")
                return None





    # Objetivo; Simular un partido  

    #E: no recibe parametros aparte de si mismo

    #S: simulara una forma de realizar un partido  |  los resultados obtenidos se guardaran en las seleccion y jugadores correspondientes 

    #R: ninguno

    def simular(self):
    # ------------------------------


        """
        Descripcion ; habran dos tiempos  |  uno extra en caso de empate siempre y cuando no sea en fase de grupos





        1. simular un partido de 90 minutos( 2 tiempos )
        
        2. se calculara de diferencia de poder de ambos equipos cada tiempo
        
        3. se calculara los goles de cada equipo segun el tiempo actual

        4. por cada tiempo sera posible que la plantilla sufra penalizacion por faltas con tarjetas rojas adquiridas durante la simulacion

        5. en caso de empate se realizara otra simulacion con tiempo extra(1 tiempo)  |  el proceso repite el punto 2 en adelante hasta terminar el tiempo extra

        """




        # Variables
        finalizar = False
        tiempo_tarnscurrido = 1

