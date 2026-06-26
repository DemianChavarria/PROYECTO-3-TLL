# Importar modulos
import Datos





#################################################################################################################################
#################################################################################################################################

# Clase Persona
# Herencia; Ninguna
# ------------------------------


# Clase constructor Persona
class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
            


            if not isinstance(nombre, str):

                raise ValueError("Error, El nombre es invalido")
            
            if not isinstance(apellido, str):

                raise ValueError("Error, El apellido es invalido")
            
            if not isinstance(fecha_nacimiento, str):

                raise ValueError("Error, La fecha de nacimiento es invalida")
            
            if not isinstance(nacionalidad, str):

                raise ValueError("Error, La nacionalidad es invalida")







            self.nombre = nombre
            self.apellido = apellido
            self.fecha_nacimiento = fecha_nacimiento
            self.nacionalidad = nacionalidad


#################################################################################################################################
#################################################################################################################################

# Clase futbolista y entrenador
# Herencia; Clase Persona
# ------------------------------


# Clase Constructor Futbolista
class Futbolista(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual):


        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)


        if not isinstance(dorsal, int) or not dorsal >= 0 or not dorsal <= 99:

            raise ValueError("Error, El dorsal es invalido")
        
        if not isinstance(posicion, str):

            raise ValueError("Error, La posicion es invalida")
        
        if not isinstance(puntaje_individual, int) or not puntaje_individual > 0 or not puntaje_individual <= 100:

            raise ValueError("Error, El puntaje individual es invalido")
        



        # datos manejados por el usuario
        self.dorsal = dorsal
        self.posicion = posicion
        self.calidad = puntaje_individual
                        
        # datos manejados por el programa
        self.tarjeta_adquirida = 0
        self.tarjeta_amarilla = 0    
        self.tarjeta_roja = 0        
        self.goles = 0             
        self.asistencias = 0



    # Objetivo ; mostrar informacion del futbolista

    #E: no recibe parametros aparte de si mismo

    #S: retorna la informacion especifica del objeto futbolista

    #R: el dorsal y puntaje individual deben ser interger(int)  |  la aposicion debe ser string(str)

    def mostrar(self):
    # ------------------------------

        super().mostrar()           # Datos de la persona
        

        return f"== FUTBOLISTA ==\n Dorsal: {self.dorsal}\n Posicion: {self.posicion}\n Puntaje Individual: {self.calidad}\n Goles: {self.goles}   Asistencias: {self.asistencias}\n Tarjetas Amarillas: {self.tarjeta_amarilla}   Tarjetas rojas: {self.tarjeta_roja}"
    



    # Objetivo; permite modificar los atributos del futbolista 

    #E: recibe un Dorsal, una posicion y un puntaje nuevo para el futbolista

    #S: retorna la modificacion de los atributos del objeto futbolista

    #R: el dorsal y puntaje individual deben ser interger(int)  |  la aposicion debe ser string(str)

    def actualizar_datos(self, dorsal, posicion, puntaje_individual):
    # ------------------------------

        if isinstance(dorsal, int) and isinstance(posicion, str) and isinstance(puntaje_individual, int):


            if dorsal >= 0 and dorsal <= 99:



                """
                Descripcion ; 

                1. validar que el dorsal del jugador no este repetido en la plantilla segun en la seleccion a la que pertenece

                2. reazlizar el cambio de los atributos del objeto jugador

                3. la modificacion se realizara en el archivo de texto correspondiente a jugadores.txt
                """


                # Variables
                txt_jugadores = []
                lista_jugadores = []




                # paso 1
                txt_jugadores = open("jugadores.txt", "r")
                for linea in txt_jugadores:
                    jugador = linea.strip().split(";")

                    lista_jugadores.append(jugador)

                    if jugador[3] == self.nacionalidad:
                        if jugador[4] == dorsal:
                            return f"Error, el dorsal del jugador ya se encuentra en uso"
                        
                txt_jugadores.close()
                



                # paso 2
                self.dorsal = dorsal
                self.posicion = posicion
                self.calidad = self.calidad




                # paso 3
                txt_jugadores = open("jugadores.txt", "w")
                for f in range(len(lista_jugadores)):

                    if lista_jugadores[f][0] == self.nombre and lista_jugadores[f][1] == self.apellido and lista_jugadores[f][2] == self.fecha_nacimiento and lista_jugadores[f][3] == self.nacionalidad:
                        lista_jugadores[f][4] = self.dorsal
                        lista_jugadores[f][5] = self.posicion
                        lista_jugadores[f][6] = self.calidad
                    
                    lista_jugadores.write(f"{lista_jugadores[f][0]};{lista_jugadores[f][1]};{lista_jugadores[f][2]};{lista_jugadores[f][3]};{lista_jugadores[f][4]};{lista_jugadores[f][5]};{lista_jugadores[f][6]};{lista_jugadores[f][7]}\n")
                lista_jugadores.close()
            








            else:
                return f"Error, Limite del dorsal solo de 0 a 99"
        
        else:
            return f"Error, los datos del futbolista no son validos"

    
    



    # Objetivo; registrar goles, asistencias y tarjetas obtenidas del objeto jugador

    #E: recibe los parametros para el conteo de goles, asistencias y tarjetas durante toda la competicion

    #S: retorna el total de goles anotados, asistencias y tarjetas obtenidas para el objeto, posteriormente se guardara en el archivo de texto correspondiente a "jugadres.txt" 

    #R: ninguna

    def registrar_estadistica(self, goles, asistencias, tarjeta_amarilla, tarjeta_roja):
    # ------------------------------
    

        # Variables
        txt_jugadores = []
        lista_jugadores = []


        self.goles += goles
        self.asistencias += asistencias
        self.tarjeta_amarilla += tarjeta_amarilla
        self.tarjeta_roja += tarjeta_roja




        txt_jugadores = open("jugadores.txt", "r")
        for linea in txt_jugadores:

            jugador = linea.strip().split(";")

            if jugador[3] == self.nacionalidad:
                if jugador[0] == self.nombre and jugador[1] == self.apellido:
                    
                    jugador[8] = self.goles
                    jugador[9] = self.asistencias
                    jugador[10] = self.tarjeta_amarilla
                    jugador[11] = self. tarjeta_roja

            lista_jugadores.append(jugador)
        
        txt_jugadores.close()



        txt_jugadores = open("jugadores.txt", "w")
        for f in range(len(lista_jugadores)):

            txt_jugadores.write(f"{lista_jugadores[f][0]};{lista_jugadores[f][1]};{lista_jugadores[f][2]};{lista_jugadores[f][3]};{lista_jugadores[f][4]};{lista_jugadores[f][5]};{lista_jugadores[f][6]};{lista_jugadores[f][7]};{lista_jugadores[f][8]};{lista_jugadores[f][9]};{lista_jugadores[f][10]};{lista_jugadores[f][11]}\n")

        txt_jugadores.close()

#################################################################################################################################

# Clase Constructor Entrenador
class Entrenador(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, años_experiencia, alineacion):


        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)

        if not isinstance(licencia, str):

            raise ValueError("Error, la licencia es invalida")
        
        if not isinstance(años_experiencia, int) or not años_experiencia >= 0 or not años_experiencia <= 100:

            raise ValueError("Error, los años de experiencias son invalidos")

        if not isinstance(licencia, str):

            raise ValueError("Error, la licencia es invalida")


        self.licencia = licencia
        self.experiencia = años_experiencia
        self.alineacion = alineacion
                






    # Objetivo; mostrar la informacion del objeto entrenador

    #E: no recibe parametros aparte de si mismo

    #S: retonrna la informacion especifica del objeto entrenador

    #R: licencia y alineacion deben ser string(str)  |  años de experiencia debe ser un interger(int)

    def mostrar(self):
    # ------------------------------

        super().mostrar()


        return f"== ENTRENADOR == \n Licencia: {self.licencia} \n Años de experiencia: {self.experiencia} \n Alineacion: {self.alineacion}"
        



    # Objetivo; modificar los atributos del objeto entrenador

    #E: recibe una licencia, los años de experiencia como entrenador y Alineacion preferida

    #S: retorna la modificacion de los atributos del objeto entrenador

    #R: licencia y alineacion deben ser string(str)  |  años de experiencia debe ser un interger(int)

    def actualizar_datos(self, licencia, años_experiencia, alineacion):


        if isinstance(licencia, str) and isinstance(años_experiencia, int) and isinstance(alineacion, str):


            if años_experiencia <= 50:

                #Variables
                nueva_lista = []
                lista_entrenadores = []

                self.licencia = licencia
                self.experiencia = años_experiencia
                self.alineacion = alineacion




                """
                Descripcion ; posterior a la modificacion de los atributos del entrenador, estos tambien se modificaran en txt. "nueva_lista" tomara
                todo lo que este en entrenadores.txt, luego, en modo sobreescritura se guardara la informacion de cada entrenador en el txt.
                si se encuentra con el entrenador a modificar, realizara los cambios y lo guardara en el txt.
                """
                lista_entrenadores = open("entrenadores.txt", "r")
                for linea in lista_entrenadores:

                    nueva_lista = nueva_lista + [linea.strip().split(";")]
                lista_entrenadores.close()



                lista_entrenadores = open("entrenadores.txt", "w")
                for f in range(len(nueva_lista)):

                    if nueva_lista[f][0] == self.nombre and nueva_lista[f][1] == self.apellido and nueva_lista[f][2] == self.fecha_nacimiento and nueva_lista[f][3] == self.nacionalidad:
                        nueva_lista[f][4] = self.licencia
                        nueva_lista[f][5] = self.experiencia
                        nueva_lista[f][6] = self.alineacion
                    
                    lista_entrenadores.write(f"{nueva_lista[f][0]};{nueva_lista[f][1]};{nueva_lista[f][2]};{nueva_lista[f][3]};{nueva_lista[f][4]};{nueva_lista[f][5]};{nueva_lista[f][6]};{nueva_lista[f][7]}\n")
                lista_entrenadores.close()
            



            else:
                return f"Error, nadie tiene mas de 50 años de experiencia" 
        
        else:
            return f"Error, los datos ingresados son invalidos"


#################################################################################################################################
#################################################################################################################################