# Importar modulos
import Datos

from Modulo_int_str import entero
from Clase_Persona_FUT_ENT import Futbolista, Entrenador
from Clase_Partido import Partido
from Clase_Fases import Fase
from Clase_Grupo import Grupo
from Clase_Mundial import Mundial






#################################################################################################################################
#################################################################################################################################

# Orden de ejecucion
# ------------------------------

"""
Descripcion ; 

El objetivo de este módulo es proporcionar al programa la capacidad de reconstruir automáticamente los objetos y restaurarlos al estado en que se encontraban antes de cerrarse.
Para lograrlo, se utilizan como referencia los archivos de texto que almacenan la información necesaria para recrear cada objeto y recuperar sus datos.


El orden de ejecucion ira de esta manera:

1. Crear la Clase mundial
2. Crear los paises
3. Crear las selecciones  |  necesita pais, entrenador y jugadores
4. crear los partidos  |  requiere la fase de grupos y fases eliminatorias


5. probablemete mas pasos

- Nota: cada paso sera una metodo diferente
"""


#################################################################################################################################
#################################################################################################################################

# Paso 1, crear mundial


Datos.g_mundial = Mundial()


#################################################################################################################################
#################################################################################################################################

# Paso 1. Crear Paises


# Objetivo; crear todos los objetos paises guardados en la base de datos 

#E: la funcion no recibe parametros

#S: retorna una lista global de objetos

#R: ninguna

def Crear_paises():
# ------------------------------
    
    # Variable
    txt_paises = None

    
    txt_paises = open("paises.txt", "r")
    for linea in txt_paises:
        
        pais = linea.strip().split(";")

        Datos.g_mundial.lista_paises.append(Datos.g_mundial.registrar_pais(pais[0], pais[1], pais[2], entero(pais[3])))


#################################################################################################################################
#################################################################################################################################

# Paso 2. Crear selecciones


# Objetivo; crear todos los objetos de equipos de seleccion guardados en la base de datos 

#E: la funcion no recibe parametros

#S: retorna una lista global de objetos

#R: ninguna

def Crear_seleccion():
# ------------------------------

    # variables
    txt_selecciones = open("selecciones.txt", "r")
    txt_jugadores = None
    txt_entrenadores = None

    f1 = 0
    


    """
    Descripcion ; se creara el objeto seleccion con toda su informacion necesaria: entrenador y jugadores.

    1. Primero se creara el objeto seleccion.

    
    2. Segundo se abrira el archivo de texto relacionado a entrenadores.txt y buscara al entrenador relacionado al atributo del equipo del objeto de seleccion
    si lo encuentra entonces creara el objeto y lo guardara en Seleccion.
    

    3. Tercero se abrira el archivo de texto relacionado a jugadores.txt y buscara a todos los juagdores que esten relacionados al atributo codigo_equipo
    de la seleccion, de poder encontrarlo entonces se creara el objeto y se añadira a la lista de jugadores.

    4. se devolvera al paso 1 hasta que deje de cumplirse la condicion  |  hasta haberse creado todos los objetos de seleccion y sus objetos relacionados

    """




    # paso 1
    for linea in txt_selecciones:
        seleccion = linea.strip().split(";")

        Datos.g_mundial.lista_selecciones.append(Datos.g_mundial.registrar_seleccion(seleccion[0], seleccion[1]))

        Datos.g_mundial.lista_selecciones[f1].total_goles_afavor = entero(seleccion[2])
        Datos.g_mundial.lista_selecciones[f1].total_goles_encontra = entero(seleccion[3])
        Datos.g_mundial.lista_selecciones[f1].total_tarjetas_amarillas = entero(seleccion[4])
        Datos.g_mundial.lista_selecciones[f1].total_tarjetas_rojas = entero(seleccion[5])


        
        
        
        #paso 2
        txt_entrenadores = open("entrenadores.txt", "r")
        for linea in txt_entrenadores:
            entrenador = linea.strip().split(";")

            if entrenador[7] == Datos.g_mundial.lista_selecciones[f1].codigo_equipo:
                Datos.g_mundial.lista_selecciones[f1].entrenador = Entrenador(entrenador[0], entrenador[1], entrenador[2], entrenador[3], entrenador[4], entero(entrenador[5]), entrenador[6])
        txt_entrenadores.close()

        
        
        
        
        
        # paso 3
        txt_jugadores = open("jugadores.txt", "r")
        for linea in txt_jugadores:
            jugador = linea.strip().split(";")

            if jugador[7] == Datos.g_mundial.lista_selecciones[f1].codigo_equipo:
                obj_jugador = Futbolista(jugador[0], jugador[1], jugador[2], jugador[3], entero(jugador[4]), jugador[5], entero(jugador[6]))
                obj_jugador.tarjeta_amarilla = entero(jugador[8])
                obj_jugador.tarjeta_roja = entero(jugador[9])
                obj_jugador.goles = entero(jugador[10])
                obj_jugador.asistencias = entero(jugador[11])

                Datos.g_mundial.lista_selecciones[f1].jugadores.append(obj_jugador)
        txt_jugadores.close()
            
           
        
        
        
        f1 += 1
        # podria indicar otras cosas mas
    
    txt_selecciones.close()


#################################################################################################################################
#################################################################################################################################

# Paso 3. Crear los Partidos


# Objetivo; crear todos los objetos de partidos y guardarlos en la lista general de partidos y luego en su lista correspondiente de clasificacion 

#E: la funcion no recibe parametros

#S: retorna la creacion de cada objeto partido en su archivo de texto correspondiente

#R: ninguna

def Crear_partidos():
# ------------------------------



    """
    Descripcion ; en esta primera parte se crearan los equipos que esten asociados a un a una fase de grupo,  si no hay un grupo en la lista general
    entonces se creara el grupo

    1. crear los grupos  |  valido que el id_partido sea de 5 digitos

    2. devuelovo las cuatro selecciones que pertenecen al grupo asociado  

    3. creo los partidos del grupo asociado y los guardo en su atributo self.__partidos
    
    """


    # Variables
    txt_partidos = []
    lista_seleccion_4 = []
    cant_grupos = []



    
    # paso 1
    txt_partidos = open("partidos.txt", "r")
    for linea in txt_partidos:

        partido = linea.strip().split(";")
        
        # este es el partido de fase de grupos
        if len(partido[4]) == 5:
            

            # lo que quiero es obtener la cantidad de grupos sin repetir
            if cant_grupos == []:

                cant_grupos.append(partido[3])
            else:
                validar = False
                for caracter in cant_grupos:

                    if caracter == partido[3]:
                        validar = True
                    
                if not validar:
                    cant_grupos.append(partido[3])

    txt_partidos.close()
    Datos.g_mundial.crear_grupos(len(cant_grupos))





    
    # Paso 2
    for grupo in Datos.g_mundial.lista_grupos:

        lista_seleccion_4 = []

        txt_partidos = open("partidos.txt", "r")
        for linea in txt_partidos:

            partido = linea.strip().split(";")

            # este es el partido de fase de grupos
            if len(partido[4]) == 5 and partido[3] == grupo.obtener_Nombre_De_Grupo():

                if lista_seleccion_4 == []:
                    lista_seleccion_4.append(partido[0])
                    lista_seleccion_4.append(partido[1])
                
                else:
                    validar = False
                    for pais in lista_seleccion_4:

                        if pais == partido[0] or pais == partido[1]:
                            validar = True
                    
                    if not validar:
                        lista_seleccion_4.append(partido[0])
                        lista_seleccion_4.append(partido[1])
        
        txt_partidos.close()
        
        for nombre_equipo in lista_seleccion_4:

            for seleccion in Datos.g_mundial.lista_selecciones:

                if seleccion.pais.nombre_pais == nombre_equipo:
                    grupo.agregar_equipo(seleccion)
        
    




    # Paso 3
    for grupo in Datos.g_mundial.lista_grupos:

        seleccion_1 = None
        seleccion_2 = None

        txt_partidos = open("partidos.txt", "r")
        for linea in txt_partidos:

            partido = linea.strip().split(";")

            # este es el partido de fase de grupos
            if len(partido[4]) == 5 and partido[3] == grupo.obtener_Nombre_De_Grupo():

                # Bloque, se buscara al primer y segunda seleccion
                for seleccion in Datos.g_mundial.lista_selecciones:

                    if seleccion.pais.nombre_pais == partido[0]:
                        seleccion_1 = seleccion
                    
                    else:
                        if seleccion.pais.nombre_pais == partido[1]:
                            seleccion_2 = seleccion
                
                creo_partido = Partido(seleccion_1, seleccion_2, partido[2], entero(partido[4]), partido[5])
                creo_partido.grupo = partido[3]
                creo_partido.goles_1 = entero(partido[6])
                creo_partido.goles_2 = entero(partido[7])

                
                grupo.obtener_partido_inicio(creo_partido)
        
        grupo.calcular_tabla()
        
        






    """
    Descripcion ; ahora luego de la fases de grupos, se crearan los partidos de la fase de eliminacion

    1. se crearan todas las fases  |  menos campeon del mundo y fase de grupos

    2. se crea el objeto partido

    3. se guarda en las diferentes lista tanto general y fases, luego  |  el metodo juga_fase clasificara a los equipos nuevamente
    """



    # variables
    txt_partidos = []


    # paso 1
    # Descripcion ;  se crearan todas las fases  |  menos campeon del mundo y fase de grupos
    for indice in range(1, len(Datos.fases_txt) - 2):

        Datos.g_mundial.lista_fases.append(Fase(Datos.fases_txt[indice]))
    

    


    txt_partidos = open("partidos.txt", "r")
    for linea in txt_partidos:

        partido = linea.strip().split(";")
        


        if len(partido[3]) == 6:

            # Bloque, se buscara al primer y segunda seleccion
            for seleccion in Datos.g_mundial.lista_selecciones:

                if seleccion.pais.nombre_pais == partido[0]:
                    seleccion_1 = seleccion
                
                else:
                    if seleccion.pais.nombre_pais == partido[1]:
                        seleccion_2 = seleccion




            # Se creara el objeto partido
            creo_partido = Partido(seleccion_1, seleccion_2, partido[2], entero(partido[3]), partido[4])

            creo_partido.goles_1 = entero(partido[5])
            creo_partido.goles_2 = entero(partido[6])
            creo_partido.penales_1 = entero(partido[7])
            creo_partido.penales_2 = entero(partido[8])
        


            # Se guardara en las diferentes listas
            Datos.g_partidos.append(creo_partido)

            for fase in Datos.g_mundial.lista_fases:

                if fase.fase == creo_partido.fase:

                    fase.fase_partidos.append(creo_partido)
            
            

    

    for fase in Datos.g_mundial.lista_fases:

        fase.jugar_fase()
        


    # es posible que se añada algo mas


#################################################################################################################################
#################################################################################################################################





def imprimir():  # prueba


    Datos.inicio = False
    
    """
    for c in range(len(Datos.g_mundial.lista_paises)):

       print(f"Nombre: {Datos.g_mundial.lista_paises[c].nombre_pais}")
    
    for c in range(len(Datos.g_mundial.lista_selecciones)):

        Datos.g_mundial.lista_selecciones[c].calcular_fuerza()
        Datos.g_mundial.lista_selecciones[c].mostrar_datos()
    """
    
    for c in range(len(Datos.g_mundial.lista_grupos)):

        Datos.g_mundial.lista_grupos[c].mostrar_tabla()

    

Crear_paises()
Crear_seleccion()
Crear_partidos()
imprimir()