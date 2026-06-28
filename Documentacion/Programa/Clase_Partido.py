import random
import Datos


#################################################################################################################################
#################################################################################################################################

# Clase Partido
# Herencia: Ninguna
# ------------------------------


# Clase Partido
class Partido:

    def __init__(self, equipo_1, equipo_2, fase, id, fecha):
        

        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.goles_1 = 0
        self.goles_2 = 0
        self.penales_1 = 0
        self.penales_2 = 0

        self.fase = fase
        self.id_partido = id
        self.fecha = fecha


    # Objetivo; Mostrar el resultado del Partido 

    #E: no recibe parametros aparte de si mismo

    #S: retorna un f"string" que muestra el resultado de ambos equipos y los goles obtenidos

    #R: ninguna

    def mostrar_resultado(self):
    # ------------------------------

        if self.penales_1 > 0 or self.penales_2 > 0:

            return f"{self.equipo_1.pais.nombre_pais} {self.goles_1} - {self.goles_2} {self.equipo_2.pais.nombre_pais} | Penales: {self.penales_1}-{self.penales_2}"

        else:
            return f"{self.equipo_1.pais.nombre_pais} {self.goles_1} - {self.goles_2} {self.equipo_2.pais.nombre_pais}"




 
    # Objetivo; actualizar la informacion en el archivo de texto y generar el ganador

    #E: no recibe parametros aparte de si mismo

    #S: retorna el objeto equipo con mas goles obtenidos o None en caso de Empate 

    #R: solo puede retornar Empate si esta en fase de grupos

    def generar_ganador(self):
    # ------------------------------

        # validacion previa
        if self.equipo_1.entrenador == None or self.equipo_2.entrenador == None:
            return f"Error, algunos de los equipos no tiene los requisitos para iniciar el partido"
        
        if len(self.equipo_1.titulares) < 11 or len(self.equipo_2.titulares) < 11:
            return f"Error, algunos de los equipos no tiene los requisitos para iniciar el partido"
    


        # variables
        txt_partidos = []


        """
        Descripcion ; se guardara el resultado del partido en su archivo de texto correspondiente a "partidos.txt"

        Nota: el partido debe estar anterriormete registrado en "partidos.txt"

        """
        txt_partidos = open("partidos.txt", "w")

        for partido in Datos.g_partidos:

            txt_partidos.write(f"{partido.equipo_1.pais.nombre_pais};{partido.equipo_2.pais.nombre_pais};{partido.fase};{partido.id_partido};{partido.fecha};{partido.goles_1};{partido.goles_2};{partido.penales_1};{partido.penales_2}\n")

        txt_partidos.close()





        if self.goles_1 > self.goles_2:
            return self.equipo_1

        elif self.goles_2 > self.goles_1:
            return self.equipo_2

        else:
            if self.fase == "Fase de Grupos":
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

        6. en caso de empate se realizara otra simulacion con tiempo extra(1 tiempo)  |  el proceso repite el punto 2 en adelante hasta terminar el partido

        """




        # Variables
        tiempo_tarnscurrido = 1
        tiempo_partido = 2
        titulares_1 = self.equipo_1.titulares
        titulares_2 = self.equipo_2.titulares
        fuerza_equipo_1 = (self.equipo_1.fuerza_equipo) // 1
        fuerza_equipo_2 = (self.equipo_2.fuerza_equipo) // 1
        gol_obtenido_1 = 0
        gol_obtenido_2 = 0
        cambio_titulares = []





        # paso 1
        while tiempo_tarnscurrido <= tiempo_partido:
            
            
            # paso 2
            if fuerza_equipo_1 > fuerza_equipo_2:
                diferencia = fuerza_equipo_1 - fuerza_equipo_2

            else:
                diferencia = fuerza_equipo_2 - fuerza_equipo_1



            print("tiempo_tarnscurrido", tiempo_tarnscurrido)
            print("Diferencia de fuerza",diferencia)




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






            print("gol_obtenido_1", gol_obtenido_1)
            print("gol_obtenido_2", gol_obtenido_2)

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

                    goleador = titulares_2[random.randint(0, len(titulares_2) - 1)]
                    goleador.registrar_estadistica(1, 0, 0, 0)

                    asistencia = True
                    while asistencia:

                        asistidor = titulares_2[random.randint(0, len(titulares_2) - 1)]
                        if asistidor.nombre != goleador.nombre and asistidor.apellido != goleador.apellido:

                            asistidor.registrar_estadistica(0, 1, 0, 0)
                            asistencia = False
            

            self.goles_1 += gol_obtenido_1
            self.goles_2 += gol_obtenido_2

            self.equipo_1.registrar_resultados(gol_obtenido_1, gol_obtenido_2, 0, 0)
            self.equipo_2.registrar_resultados(gol_obtenido_2, gol_obtenido_1, 0, 0)

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
                    jugador.tarjeta_adquirida += 1
                    jugador.registrar_estadistica(0, 0, 1, 0)
                    equipo_asosciado.registrar_resultados(0, 0, 1, 0)

                    if jugador.tarjeta_adquirida == 2:
                        jugador.registrar_estadistica(0, 0, 0, 1)
                        equipo_asosciado.registrar_resultados(0, 0, 0, 1)

                        if jugador.calidad <= 60:
                            fuerza_equipo -= 5
                        elif jugador.calidad > 60 and jugador.calidad <= 78:
                            fuerza_equipo -= 10
                        elif jugador.calidad > 78 and jugador.calidad <= 95:
                            fuerza_equipo -= 15
                        else:
                            fuerza_equipo -= 18


                        for traspaso in titulares:

                            if traspaso.nombre != jugador.nombre or traspaso.apellido != jugador.apellido:
                                cambio_titulares.append(traspaso)
                        

                        if equipo == 1:
                            titulares_1 = cambio_titulares
                            fuerza_equipo_1 = fuerza_equipo
                        else:
                            titulares_2 = cambio_titulares
                            fuerza_equipo_2 = fuerza_equipo

                        cambio_titulares = []
                        jugador.tarjeta_adquirida = 0
                
                else:
                    if tarjeta <= 3:

                        jugador = titulares[random.randint(0, len(titulares) - 1)]

                        jugador.registrar_estadistica(0, 0, 0, 1)
                        equipo_asosciado.registrar_resultados(0, 0, 0, 1)

                        if jugador.calidad <= 60:
                            fuerza_equipo -= 5
                        elif jugador.calidad > 60 and jugador.calidad <= 78:
                            fuerza_equipo -= 10
                        elif jugador.calidad > 78 and jugador.calidad <= 95:
                            fuerza_equipo -= 15
                        else:
                            fuerza_equipo -= 18


                        for traspaso in titulares:

                            if traspaso.nombre != jugador.nombre or traspaso.apellido != jugador.apellido:
                                cambio_titulares.append(traspaso)
                        

                        if equipo == 1:
                            titulares_1 = cambio_titulares
                            fuerza_equipo_1 = fuerza_equipo
                        else:
                            titulares_2 = cambio_titulares
                            fuerza_equipo_2 = fuerza_equipo

                        cambio_titulares = []
                        jugador.tarjeta_adquirida = 0
        



            # paso 6
            if tiempo_tarnscurrido == 2:
                if not self.fase == "Fase de Grupos":
                    if self.goles_1 == self.goles_2:
                        tiempo_partido += 1
                        tiempo_tarnscurrido += 1
                    
                    else:
                        tiempo_tarnscurrido += 1
                
                else:
                    tiempo_tarnscurrido += 1

            else:
                tiempo_tarnscurrido += 1
                




        if not self.fase == "Fase de Grupos":


            """
            Descripcion ;  si resulta que estamos en una fase eliminatoria y no en fase de grupos, ambos equipos jugaran una tanda de penales 
            hasta que uno sea el vencedor

            1. validar que ambos equipos no tengan la misma cantidad de goles.

            2. simular una tanda de penales de (2, 5) en ambos equipos.
    
            3. la cantidad de goles obtenidos se pasara a los goleadores y posteiormente a las estadisticas de la seleccion.

            4. se validara el resultado del calculo y si resulta parejo se repetira el punto 2 hasta obtener una diferencia en en ambos equipos.
            
            """



            # vdariables
            gol_obtenido_1 = 0
            gol_obtenido_2 = 0
            continuar = True
            
            
            # paso 1
            if self.goles_1 == self.goles_2:
                
            



                # paso 2
                while continuar:


                    gol_obtenido_1 = random.randint(2, 5)
                    gol_obtenido_2 = random.randint(2, 5)




                    # paso 3
                    for gol in range(gol_obtenido_1):

                        goleador = titulares_1[random.randint(0, len(titulares_1) - 1)]
                        goleador.registrar_estadistica(1, 0, 0, 0)
                    
                    
                    for gol in range(gol_obtenido_2):

                        goleador = titulares_2[random.randint(0, len(titulares_2) - 1)]
                        goleador.registrar_estadistica(1, 0, 0, 0)
                    

                    
                    self.penales_1 += gol_obtenido_1
                    self.penales_2 += gol_obtenido_2

                    self.equipo_1.registrar_resultados(self.penales_1, self.penales_2, 0, 0)
                    self.equipo_2.registrar_resultados(self.penales_2, self.penales_1, 0, 0)

                    gol_obtenido_1 = 0
                    gol_obtenido_2 = 0



                    # paso 4
                    if self.penales_1 != self.penales_2:

                        continuar = False


#################################################################################################################################
#################################################################################################################################

# Obtener Fecha Segun la fase
# ------------------------------


# Objetivo; obtener un fecha para el partido 

#E: recibe una fase actual

#S: retorna la fecha segun la fase en la que este

#R: ninguna 
def fechas(fase):
# ------------------------------

    if not Datos.inicio:
        if fase == "Fase de Grupos":
                    
            fecha = f"{random.randint(1, 30)}/06/2026"

        elif fase == "Dieciceisavos de Final":

            fecha = f"{random.randint(1, 20)}/07/2026"
                    
        elif fase == "Octavos de Final":

            fecha = f"{random.randint(21, 30)}/07/2026"
                
        elif fase == "Cuartos de Final":

            fecha = f"{random.randint(1, 5)}/08/2026"

        elif fase == "Semifinales":

            fecha = f"{random.randint(6, 7)}/06/2026"
                
        else:

            fecha = "10/06/2026"
    
    else:
        return None



    return fecha
