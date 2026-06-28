import Datos
import random
from Clase_Pais_Seleccion import Pais, Seleccion
from Clase_Partido import Partido, fechas

#Import para crear grupos en base a cuantos sean necesarios:
from Clase_Grupo import Grupo




#################################################################################################################################
#################################################################################################################################

# Clase MUndial
# Herencia; Ninguna
# ------------------------------


# Clase constructor Pais
class Mundial:

    def __init__(self):

        self.nombre_mundial = "Mundial FIFA "
        self.año = 2026

        self.lista_paises = []
        self.lista_selecciones = []
        self.lista_grupos = []
        self.lista_fases = []
        self.campeon = None





    # Objetivo ; registrar la creacion de los objetos paises

    #E: recibe los parametros para la creacion del objeto pais

    #S: retorna la creacion del objeto pais y lo guarda en su lista correspondiente  |  y en su archivo de texto correspondiente

    #R: la informacion del objeto pais no puede ser otra ya existente en la base de datos  |  evitar guardarlo en el archivo de texto cada vez que el programa se ejecute
    
    def registrar_paises(self, codigo_fifa, nombre_pais, continente, ranking_fifa):
    # ------------------------------

        if Datos.inicio:

            return Pais(codigo_fifa, nombre_pais, continente, ranking_fifa)

        else:

            # Variables
            txt_paises = []


            for c in range(len(self.lista_paises)):

                if self.lista_paises[c].codigo_fifa == codigo_fifa or self.lista_paises[c].nombre_pais == nombre_pais:
                    return f"Error, los datos ingresados ya se encuentran incluidos"
                


            self.lista_paises.append(Pais(codigo_fifa, nombre_pais, continente, ranking_fifa))



            txt_paises = open("paises.txt", "a")
            txt_paises.write(f"{codigo_fifa};{nombre_pais};{continente};{ranking_fifa}\n")

            txt_paises.close()







    # Objetivo; guardar la informacion del objeto Seleccion en la base de datos correspondiente a selecciones.txt

    #E: recibe los datos especificos para el objeto seleccion

    #S: retorna la informacion del objeto seleccion en el Modulo de base de datos y en su archivo de texto correspondiente

    #R: la informacion del objeto seleccion no puede ser otra ya existente en la base de datos  |  evitar guardarlo en el archivo de texto cada vez que el programa se ejecute

    def registrar_selecciones(self, codigo_equipo, nombre_pais):
    # ------------------------------

        if Datos.inicio:

            return Seleccion(codigo_equipo, nombre_pais)
        

        else:

            # variable
            txt_selecciones = []

            for c in range(len(self.lista_selecciones)):

                if self.lista_selecciones[c].codigo_equipo == codigo_equipo or self.lista_selecciones[c].pais.nombre_pais == nombre_pais:
                    return f"Error, los datos ya se encuentran incluidos"
            


            self.lista_selecciones.append(Seleccion(codigo_equipo, nombre_pais))



            txt_selecciones = open("selecciones.txt", "a")
            txt_selecciones.write(f"{codigo_equipo};{nombre_pais};0;0;0;0\n")

            txt_selecciones.close()

    




    # Objetivo; Armar cada fase del torneo
    #E: no recibe parametros aparte de si mismo
    #S: retorna un Armado del torneo segun la fase en la que este
    #R: no puede crear una fase si no se ha iniciado la fase de grupos
    def armar_fase(self):
    # ------------------------------


        if Datos.equipos_grupos_clasificados != []:

            if Datos.Clasificados_16 != []:

                if Datos.clasificados_8 != []:

                    if Datos.clasificados_4 != []:

                        if Datos.clasificados_2 != []:
                            return

                        
                        else:
                            self.lista_fases[3].registrar_juego()
                    
                    else:
                        self.lista_fases[2].registrar_juego()
                
                else:
                    self.lista_fases[1].registrar_juego()
        
            else:
                self.lista_fases[0].registrar_juego()
        
        else:
            self.lista_fases[0].registrar_juego()




    # Objetivo; obtener los resultados de cada enfrentamiento en las fases

    #E: no recibe parametros aparte de si mismo

    #S: retorna los resultados de cada enfrentamiento

    #R: no puede hacer un juego si ya hay clasificados

    def jugar_fases(self):
    # ------------------------------

        if Datos.Clasificados_16 == []:

            self.lista_fases[0].jugar_fase()
        
        elif Datos.Clasificados_8 == []:

            self.lista_fases[1].jugar_fase()
        
        elif Datos.clasificados_4 == []:

            self.lista_fases[2].jugar_fase()
        
        elif Datos.clasificados_2 == []:

            self.lista_fases[3].jugar_fase()
        
        else:
            return
        

    

    # Objetivo;  Determinar el campeon de la FIFA

    #E: no recibe parametros aparte de si mismo

    #S: retorna el campeon y se guardara en el atributo correspondiente

    #R: se necesitan clasificados en las semifinales

    def determinar_campeon(self):
    # ------------------------------

        if Datos.clasificados_2 != []:

            while id_partido == 0:
                    
                    id_partido = random.randint(100000, 999999)

                    validar_1 = False
                    
                    if Datos.g_partidos != []:
                        
                        for partido in Datos.g_partidos:

                            if partido.id_partido == id_partido:
                                validar_1 = True
                        
                        if validar_1:
                            id_partido = 0

            Datos.partido_1 = Partido(Datos.clasificados_2[0], Datos.clasificados_2[1], "Final de la Copa del Mundo", id_partido, fechas("Final de la Copa del Mundo"))


            Datos.partido_1.simular()
            Datos.partido_1.mostrar_resultado()
            Datos.campeon = Datos.partido_1.generar_ganador()
            self.campeon = Datos.campeon
        
        else:
            return 


    #Objetivo: Crear la cantidad de grupos que el usuario ingrese.

    #Entrada: Cantidad de grupos | un interger| Este es la cantidad de grupos a generar.

    #Salida: 

    #Restricciones:



    def crear_grupos(self, cantidad_grupos):


        if not len(self.lista_selecciones)/cantidad_grupos == 4:
            return "Error: La cantidad de se selecciones debe ser suficiente para que cada grupo tenga 4 equipos."


        #Cantidad de letras para cada grupo:
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.lista_grupos = []


        #Cada letra será un grupo 
        for i in range(cantidad_grupos):

            grupo = Grupo(letras[i])


            #Asignar 4 selecciones a cada grupo

                

            for indice_seleccion in range(i*4, i*4+4):

                grupo.agregar_equipo(self.lista_selecciones[indice_seleccion])
                                     
                                     


            self.lista_grupos.append(grupo)


#Objetivo: Simular los partidos de cada grupo y mostrar su respectiva tabla

#Entrada: objeto mismo.

#Salida: Quedan los partidos de cada grupo quetuvo un partido simulado (queda la tabla del grupo ordenada)

#Restricciones: Deben haber selecciones y todo lo que un objeto seleccion conlleve.


    def jugar_fase_grupos(self):


        for grupo in self.lista_grupos:

            grupo.generar_partidos()

            grupo.calcular_tabla()

        
    #Objetivo: Mostrar la tabla con todos los grupos y sus resultados.

    #Entrada: El mismo objeto, mundial

    #Salida: Una tabla donde están todos los grupos con sus resultados.

    #Restricciones: Deberían haber grupos en la lista_grupos.

    def mostrar_tabla_general(self):

        todos_los_grupos_str = ""

        for grupo in self.lista_grupos:

            todos_los_grupos_str = todos_los_grupos_str + f"{grupo.mostrar_tabla()}"

        
    
