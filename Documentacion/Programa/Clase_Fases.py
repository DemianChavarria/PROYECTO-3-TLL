import Datos
import random
from Clase_Partido import Partido, fechas







#################################################################################################################################
#################################################################################################################################

# Clase Fases
# Herencia; Ninguna
# ------------------------------


# Clase Fases
class Fase:

    def __init__(self):
        pass




    # Objetivo ; registrar los partidos segun la fase actual del torneo

    #E: recibe la fase actual del torneo 

    #S: retorna la lista de partidos segun la fase actual del torneo

    #R: ninguna

    def registrar_juego(self, fase):
    # ------------------------------
        



        """
        Descripcion ; la idea general es que dependiendo de la fase en la que este, generara la cantidad de partidos necesarios para el torneo

        Nota = si sucediera que algun equipo se queda sin pareja entonces se buscara al mejor equipo de la fase anterior.

        

        el orden es mas o menos asi

        1. valido si algun equipo se quedo sin pareja, Entonces buscare en la lista de clasificados anterior su posicion en el rankin  |  solo para Octavos en adelante

        2. saco al equipo 1 con indice [0] y el segundo equipo sera elegido al azar

        3. quito a ambos equipos que ya se encuentran emparejados de la lista de clasificados

        4. crear el id_partido de 6 digitos  |  validar que no sea un id repetido

        5. crear el partido  |  guardarlo en la lista_partidos  |  guardarlo el partido en su lista correspondiente de fases  |  guardarlo en su archivo txt correspondiente a "partidos.txt"

        """




        # Variables
        nueva_lista = []
        id_partido = 0
        txt_partidos = []
        mejor_tercero = None
        clasificacion_anterior = None
        seleccion_2 = None











        if fase == "Dieciceisavos de Final":

            clasificados_grupos = Datos.equipos_grupos_clasificados
        
        elif fase == "Octavos de Final":

            clasificados_grupos = Datos.Clasificados_16
        
        elif fase == "Cuartos de Final":

            clasificados_grupos = Datos.clasificados_8

        elif clasificados_grupos == "Semifinales":

            clasificados_grupos = Datos.clasificados_4

        else:

            clasificados_grupos = Datos.clasificados_2









            while clasificados_grupos != []:
                


                # paso 1,  aqui estoy buscando en que fase estoy para sacar al mejor tercero de la clasificacion anterior
                if len(clasificados_grupos) == 1 and fase != "Dieciceisavos de Final":

                    if fase == "Octavos de Final":

                        clasificacion_anterior = Datos.Clasificados_16
        
                    elif fase == "Cuartos de Final":

                        clasificacion_anterior = Datos.clasificados_8

                    else:

                        clasificacion_anterior = Datos.clasificados_4

                    


                    # luego de encontrarlo entonces recorrere la lista para buscar al mejor tercer equipo
                    for c in range(len(clasificacion_anterior)):

                        if mejor_tercero == None:
                            mejor_tercero = clasificacion_anterior[c]

                        if c + 1 < len(clasificacion_anterior):

                            if mejor_tercero.pais.ranking_fifa < clasificacion_anterior[c + 1].pais.ranking_fifa:

                                mejor_tercero = clasificacion_anterior[c + 1]
                        




                        # se guardara aqui
                        seleccion_2 = mejor_tercero
                            

                        



                # Paso2,  Saco al equipo para emparejar
                seleccion_1 = clasificados_grupos[0]


                if seleccion_2 == None:
                    seleccion_2 = random.randint(1, len(clasificados_grupos) - 1)







                # Paso 3 ,  quitare a los equipos a emparejar de la lista de clasificados
                clasificados_grupos = clasificados_grupos[1:]

                if clasificados_grupos != []:
                    for equipo in clasificados_grupos:

                        if not equipo.pais.nombre_pais == seleccion_2.pais.nombre_pais:

                            nueva_lista.append(equipo)
                    

                clasificados_grupos = nueva_lista
                nueva_lista = []






                # Paso 4, Saco el Id con random y valido con for que no sea un id repetido de la lista de partidos
                while id_partido == 0:
                    
                    id_partido = random.randint(100000, 999999)

                    validar_1 = False
                    
                    if Datos.g_partidos != []:
                        
                        for partido in Datos.g_partidos:

                            if partido.id_partido == id_partido:
                                validar_1 = True
                        
                        if validar_1:
                            id_partido = 0
                



                # Paso 5

                # se guardara en la lista general de partidos
                creo_partido = Partido(seleccion_1, seleccion_2, fase, id_partido)
                Datos.g_partidos.append(creo_partido)





                # se guardara en su lista de fase correspondiente
                if fase == "Dieciceisavos de Final":

                    Datos.partidos_16.append(creo_partido)
                
                elif fase == "Octavos de Final":

                    Datos.partidos_8.append(creo_partido)
                
                elif fase == "Cuartos de Final":

                    Datos.partidos_4.append(creo_partido)
                
                elif fase == "Semifinales":

                    Datos.clasificados_2.append(creo_partido)
                
                else:

                    Datos.partido_1.append(creo_partido)




                # se registrara en su archivo de texto correspondiente
                txt_partidos = open("partidos.txt", "a")

                txt_partidos.write(f"{creo_partido.equipo_1.pais.nombre_pais};{creo_partido.equipo_2.pais.nombre_pais};{fase};{id_partido};{fechas(fase)}0;0;0;0")

                txt_partidos.close()

                seleccion_2 = None
    






    # Objetivo ; jugar la fase 
    #E: 
    #S: activa cada partido de la fase correspondiente y retorna los resultados junto con el ganador
    #R:







                


            


