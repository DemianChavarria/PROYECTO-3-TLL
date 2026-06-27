import Datos







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
        """


        # Variables






        if fase == "Dieciceisavos de Final":

            clasificados_grupos = Datos.equipos_grupos_clasificados


                


            


