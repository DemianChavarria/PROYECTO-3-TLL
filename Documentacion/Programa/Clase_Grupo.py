
#Para que python pueda ver la informacion de los partidos
import Datos

#Para poder crear los partidos de un grupo y simularlos
from Clase_Partido import Partido, fechas

#Para crear los IDs random de los partidos
import random

class Grupo :



#Objetivo: Método constructor de la clase Grupo

#Entrada: Nombre del grupo

#Salida: Un objeto tal construido de la clase Grupo

#Restricciones: nombre_grupo debe ser un string no vacío

    def __init__(self, nombre_grupo):

        

        self.__nombre_grupo = nombre_grupo

        self.__equipos = []

        self.__partidos = []




#Objetivo: Método que agrega un equipo a la lista de equipos del grupo

#Entrada: equipo (objeto de la clase Equipo), es una selección de un país que participa en el grupo

#Salida: Se agrega el equipo a la lista de equipos del grupo

#Restricciones: El equipo no puede ya estar en la lista del grupo, y debe tener máximo 3 selecciones para poder añadírsele una más | retorna un error sino.

    def agregar_equipo(self, equipo):
#Valida que no sea de =+4 el grupo ya.
        if len(self.__equipos) == 4:

            return f"Grupo ya tiene 4 selecciones"
        
#Validar no repetidos
        for seleccion in self.__equipos: 

            

            if (equipo.codigo_equipo == seleccion.codigo_equipo) or (equipo.pais.nombre_pais == seleccion.pais.nombre_pais):

                return f"Selección del país ya está en el grupo"
            
#Acción real de añadir selección al grupo

        self.__equipos.append(equipo)


#Método para crear un ID random para los partidos, asegurando que no se repita con los ya existentes.
    def crear_ID_random(self):
        id_partido = 0

        while id_partido == 0:
            
            id_partido = random.randint(10000, 99999)

            validar_1 = False
            
            if Datos.g_partidos != []:
                
                for partido in Datos.g_partidos:

                    if partido.id_partido == id_partido:
                        validar_1 = True
                
                if validar_1:
                    id_partido = 0

        return id_partido

    #Método para crear los partidos necesarios:

    #Objetivo: Generar los 6 partidos de la fase de grupos (formato todos contra todos).

    #Entrada: No recibe parámetros externos (utiliza la lista self.__equipos).

    #Salida: Se crean y agregan 6 objetos Partido a la lista self.__partidos.

    #Restricciones: El grupo debe tener exactamente 4 equipos para generar los partidos correctamente.

    def generar_partidos(self):

        
        # Validación defensiva
        if len(self.__equipos) != 4:
            return "Error: El grupo no tiene 4 equipos para generar los partidos."

        # Ciclos anidados para emparejar sin repetir
        for i in range(len(self.__equipos)):
            for j in range(i + 1, len(self.__equipos)):

    
                      
                id_por_partido = self.crear_ID_random()


                # Asignar local y visitante
                local = self.__equipos[i]
                visitante = self.__equipos[j]
       
                partido = Partido(local, visitante, "Fase de Grupos", id_por_partido, fechas("Fase de Grupos"))
                
                #Recopilamos el atributo nombre de cada grupo (Los atributos se pueden asignar en la ejecucion)
                partido.grupo = self.obtener_Nombre_De_Grupo()


                # Guardar en la lista del grupo
                self.__partidos.append(partido)

                # Guardar en la lista global de partidos
                Datos.g_partidos.append(partido)


    #Objetivo: Calcular la tabla de puntos de los partidos.

    #Entrada: El mismo objeto.

    #Salida: La tabla con valores numericos que representan los puntos de cada seleccion.

    #Restricciones: Deben haber partidos en la lista para poder calcular puntos

    def calcular_tabla(self):

        if len(self.__partidos) == 0:

            return f"No hay partidos para calcular la tabla de puntos."
    # self.__equipos | tipo: lista, contiene: objetos de la clase Seleccion, quién la usa: Grupo.
    # puntos_por_equipo | tipo: diccionario, contiene: claves (string codigo_equipo) y valores (int puntos), quién la usa: Grupo.
        puntos_por_equipo = {}

        for equipo in self.__equipos:

            puntos_por_equipo[equipo.codigo_equipo] = 0


#Simulacion de cada partido en self.__partidos, si Datos.inicio==True.
        if not Datos.inicio:

            for simulacion_de_partido in self.__partidos:

                

                simulacion_de_partido.simular()

            for partido in self.__partidos:

                partido.generar_ganador()
        




        for partido in self.__partidos:


    #Si el equipo 1 gana, se le asignan 3 puntos al equipo 1, si empatan se le asigna 1 punto a cada equipo, y si gana el equipo 2 se le asignan 3 puntos al equipo 2.
            if partido.goles_1 > partido.goles_2:

                puntos_por_equipo[partido.equipo_1.codigo_equipo] += 3
    #Si el equipo 1 y el equipo 2 empatan, se le asigna 1 punto a cada equipo.
            if partido.goles_1 == partido.goles_2:

                puntos_por_equipo[partido.equipo_1.codigo_equipo] +=1

                puntos_por_equipo[partido.equipo_2.codigo_equipo] +=1
    #Si el equipo 2 gana, se le asignan 3 puntos al equipo 2.
            if partido.goles_1 < partido.goles_2:

                puntos_por_equipo[partido.equipo_2.codigo_equipo] += 3

    #Usamos el método ordenar_tabla para ordenar la tabla de puntos de los equipos en el grupo de mayor a menor.
        self.ordenar_tabla(puntos_por_equipo)
        self.__puntos_por_equipo = puntos_por_equipo














    #Método para ordenar la tabla de puntos de los equipos en el grupo:

    #Objetivo: Ordenar la tabla de puntos de los equipos en el grupo de mayor a menor.

    #Entrada: La tabla de puntos calculada previamente.

    #Salida: La tabla de puntos ordenada de mayor a menor.

    #Restricciones: La tabla de puntos debe estar calculada previamente.

    def ordenar_tabla(self, puntos_por_equipo):


        for i in range(len(self.__equipos)):

            for j in range(i + 1, len(self.__equipos)):

                equipo_1 = self.__equipos[i]

                equipo_2 = self.__equipos[j]

                #Variables que almacenan los puntos de cada equipo para poder compararlos y ordenarlos.
                puntos_1 = puntos_por_equipo[equipo_1.codigo_equipo]

                puntos_2 = puntos_por_equipo[equipo_2.codigo_equipo]

                if puntos_1 < puntos_2:

                    # Intercambiar posiciones en la lista de equipos
                    self.__equipos[i] = equipo_2

                    self.__equipos[j] = equipo_1

#Objetivo: Retornar para TKINTER la tabla de posiciones del grupo ya ordenada.

#Entrada: puntos_por_equipo (diccionario con los puntos de cada selección, esto basado en sus codigos).

#Salida: Retorna las selecciones que hay en cada grupo ordenadas por sus puntos acumulados.

#Restricciones: La lista self.__equipos debe estar ordenada y el diccionario debe tener los puntos.


    def mostrar_tabla(self):

#Esta variable podía inicar directa pero visualmente se me hace mas facil entender que se genera, luego va el nombre como encabezado y ya luego la verdadera tabla de puntos.
        texto_tabla = ""


        texto_tabla = f"Grupo :{self.__nombre_grupo}\n"

        for indice, seleccion in enumerate(self.__equipos):

            posicion = indice + 1
            puntos = self.__puntos_por_equipo[seleccion.codigo_equipo]

            texto_tabla = texto_tabla + (f"{posicion}; {seleccion.pais.nombre_pais}; {puntos} puntos\n")
        



        return texto_tabla





    #Objetivo: Retornar los dos equipos mejor posicionados del grupo para que avancen a la fase eliminatoria.

    #Entrada: No recibe parámetros externos (usa la lista self.__equipos que ya debe estar ordenada).

    #Salida: Una lista con exactamente 2 objetos de la clase Seleccion (el 1er y 2do lugar).

    #Restricciones: La lista self.__equipos debe estar ordenada previamente por calcular_tabla() y tener al menos 2 equipos.

    def obtener_clasificados(self):
        return [self.__equipos[0], self.__equipos[1]]


#Atributos para usar en otras clases

    #Objetivo: Nombre de grupo está encapsulado|es necesario a la hora de usar atributos en otras clases o modulos "desencapsularlo" para acceder a este.

    #Entrada: mismo objeto Grupo

    #Salida: nombre grupo para poder ser utilizado en otras clases

    #Restricciones: Tiene que estar nombrado el grupo.

    def obtener_Nombre_De_Grupo(self):

        return self.__nombre_grupo 
    
    def obtener_equipos(self):

        return self.__equipos
    
    def obtener_partidos(self):

        return self.__partidos
             