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
        
        2. se calculara la diferencia de poder de ambos equipos cada tiempo
        
        3. se calculara los goles de cada equipo segun el tiempo actual y su diferencia de poder

        4. si hay gol entonces un jugador de la seleccion que anoto recibira un gol a su conteo y otro jugador sera dado una asistencia a su conteo

        5. por cada tiempo sera posible que la plantilla sufra penalizacion por faltas con tarjetas adquiridas durante la simulacion

        6. en caso de empate se realizara otra simulacion con tiempo extra(1 tiempo)  |  el proceso repite el punto 2 en adelante hasta terminar el tiempo extra

        """




        # Variables
        finalizar = False
        tiempo_tarnscurrido = 1
        tiempo_partido = 2
        titulares_1 = self.equipo_1.titulares
        titulares_2 = self.equipo_2.titulares
        fuerza_equipo_1 = self.equipo_1.fuerza_equipo
        fuerza_equipo_2 = self.equipo_2.fuerza_equipo
        gol_obtenido_1 = 0
        gol_obtenido_2 = 0
        cambio_titulares = []





        # paso 1
        while tiempo_tarnscurrido <= tiempo_partido:
            
            
            # paso 2
            diferencia = fuerza_equipo_1 - fuerza_equipo_2





            # paso 3
            if diferencia > 15 and diferencia < 30:
                if fuerza_equipo_1 > fuerza_equipo_2:
                    gol_obtenido_1 += random.randint(1, 3)
                    gol_obtenido_2 += random.randint(0, 2)
                else:
                    gol_obtenido_2 += random.randint(1, 3)
                    gol_obtenido_1 += random.randint(0, 2)

            elif diferencia >= 30:
                if fuerza_equipo_1 > fuerza_equipo_2:
                    gol_obtenido_1 += random.randint(2, 5)
                    gol_obtenido_2 += random.randint(0, 3)
                else:
                    gol_obtenido_2 += random.randint(2, 5)
                    gol_obtenido_1 += random.randint(0 , 3)
            
            else:
                gol_obtenido_1 += random.randint(0, 4)
                gol_obtenido_2 += random.randint(0, 4)







            # paso 4
            if gol_obtenido_1 > 0:

                for gol in range(gol_obtenido_1):

                    goleador = titulares_1[random.randint(0, len(titulares_1) - 1)]
                    goleador.registrar_estadistica(1, 0, 0, 0)

                    asistencia = True
                    while asistencia:

                        asistidor = titulares_1[random.randint(0, len(titulares_1) - 1)]
                        if asistidor.nombre != goleador.nombre and asistidor.apellido != goleador.apellido:

                            asistidor.registrar_estadistica(0, 1, 0, 0)
                            asistencia = False
                    
            if gol_obtenido_2 > 0:

                for gol in range(gol_obtenido_2):

                    goleador = titulares_1[random.randint(0, len(titulares_2) - 1)]
                    goleador.registrar_estadistica(1, 0, 0, 0)

                    asistencia = True
                    while asistencia:

                        asistidor = titulares_1[random.randint(0, len(titulares_2) - 1)]
                        if asistidor.nombre != goleador.nombre and asistidor.apellido != goleador.apellido:

                            asistidor.registrar_estadistica(0, 1, 0, 0)
                            asistencia = False
            

            self.goles_1 += gol_obtenido_1
            self.goles_2 += gol_obtenido_2
            gol_obtenido_1 = 0
            gol_obtenido_2 = 0

    




            # paso 5
            for equipo in range(1, 3):
                
                if equipo == 1:
                    titulares = titulares_1
                    fuerza_equipo = fuerza_equipo_1
                    equipo_asosciado = self.equipo_1
                
                else:
                    titulares = titulares_2
                    fuerza_equipo = fuerza_equipo_2
                    equipo_asosciado = self.equipo_2



                tarjeta = random.randint(1, 100)

                if tarjeta <= 10 and tarjeta > 3:

                    jugador = titulares[random.randint(0, len(titulares) - 1)]
                    jugador.tarjeta_obtenida += 1
                    jugador.registrar_estadistica(0, 0, 1, 0)
                    equipo_asosciado.registrar_resultados(0, 0, 1, 0)

                    if jugador.tarjeta_obtenida % 2 == 0:
                        jugador.registrar_estadistica(0, 0, 0, 1)
                        equipo_asosciado.registrar_resultado(0, 0, 0, 1)

                        if jugador.calidad <= 60:
                            fuerza_equipo -= 5
                        elif jugador.calidad > 60 and jugador.calidad <= 78:
                            fuerza_equipo -= 10
                        elif jugador.calidad > 78 and jugador.calidad <= 95:
                            fuerza_equipo -= 15
                        else:
                            fuerza_equipo -= 18


                        for traspaso in titulares:

                            if traspaso.nombre != jugador.nombre and traspaso.apellido != jugador.apellido:
                                cambio_titulares.append(traspaso)
                        

                        if equipo == 1:
                            titulares_1 = cambio_titulares
                            fuerza_equipo_1 = fuerza_equipo
                        else:
                            titulares_2 = cambio_titulares
                            fuerza_equipo_2 = fuerza_equipo

                        cambio_titulares = []
                        jugador.tarjeta_obtenida = 0
                
                else:
                    if tarjeta <= 3:

                        jugador = titulares[random.randint(0, len(titulares) - 1)]

                        jugador.registrar_estadistica(0, 0, 0, 1)
                        equipo_asosciado.registrar_resultado(0, 0, 0, 1)

                        if jugador.calidad <= 60:
                            fuerza_equipo -= 5
                        elif jugador.calidad > 60 and jugador.calidad <= 78:
                            fuerza_equipo -= 10
                        elif jugador.calidad > 78 and jugador.calidad <= 95:
                            fuerza_equipo -= 15
                        else:
                            fuerza_equipo -= 18


                        for traspaso in titulares:

                            if traspaso.nombre != jugador.nombre and traspaso.apellido != jugador.apellido:
                                cambio_titulares.append(traspaso)
                        

                        if equipo == 1:
                            titulares_1 = cambio_titulares
                            fuerza_equipo_1 = fuerza_equipo
                        else:
                            titulares_2 = cambio_titulares
                            fuerza_equipo_2 = fuerza_equipo

                        cambio_titulares = []
                        jugador.tarjeta_obtenida = 0
        



            # paso 6
            if tiempo_tarnscurrido == 2:
                if self.fase != "Grupos":
                    if self.goles_1 == self.goles_2 and not finalizar:
                        tiempo_partido += 1
                        finalizar = True
            
            else:
                tiempo_tarnscurrido += 1
                








                        








        



            
            

