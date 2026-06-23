# Importar modulos
import Datos

from Clase_Pais_Seleccion import registrar_pais, registrar_seleccion
from Modulo_int_str import entero
from Clase_Persona_FUT_ENT import Futbolista, Entrenador






#################################################################################################################################
#################################################################################################################################

# Orden de ejecucion
# ------------------------------

"""
Descripcion ; 

El objetivo de este módulo es proporcionar al programa la capacidad de reconstruir automáticamente los objetos y restaurarlos al estado en que se encontraban antes de cerrarse.
Para lograrlo, se utilizan como referencia los archivos de texto que almacenan la información necesaria para recrear cada objeto y recuperar sus datos.


El orden de ejecucion ira de esta manera:

1. Crear los paises
2. Crear las selecciones  |  necesita pais, entrenador y jugadores


3. probablemete mas pasos

- Nota: cada paso sera una metodo diferente
"""


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
    lista_paises = None

    
    lista_paises = open("paises.txt", "r")
    for linea in lista_paises:
        
        pais = linea.strip().split(";")

        Datos.g_paises.append(registrar_pais(pais[0], pais[1], pais[2], entero(pais[3])))


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

        Datos.g_selecciones.append(registrar_seleccion(seleccion[0], seleccion[1]))

        Datos.g_selecciones[f1].total_goles_afavor = entero(seleccion[2])
        Datos.g_selecciones[f1].total_goles_encontra = entero(seleccion[3])
        Datos.g_selecciones[f1].total_tarjetas_amarillas = entero(seleccion[4])
        Datos.g_selecciones[f1].total_tarjetas_rojas = entero(seleccion[5])


        
        
        
        #paso 2
        txt_entrenadores = open("entrenadores.txt", "r")
        for linea in txt_entrenadores:
            entrenador = linea.strip().split(";")

            if entrenador[7] == Datos.g_selecciones[f1].codigo_equipo:
                Datos.g_selecciones[f1].entrenador = Entrenador(entrenador[0], entrenador[1], entrenador[2], entrenador[3], entrenador[4], entero(entrenador[5]), entrenador[6])
        txt_entrenadores.close()

        
        
        
        
        
        # paso 3
        txt_jugadores = open("jugadores.txt", "r")
        for linea in txt_jugadores:
            jugador = linea.strip().split(";")

            if jugador[7] == Datos.g_selecciones[f1].codigo_equipo:
                obj_jugador = Futbolista(jugador[0], jugador[1], jugador[2], jugador[3], entero(jugador[4]), jugador[5], entero(jugador[6]))
                obj_jugador.tarjeta_amarilla = entero(jugador[8])
                obj_jugador.tarjeta_roja = entero(jugador[9])
                obj_jugador.goles = entero(jugador[10])
                obj_jugador.asistencias = entero(jugador[11])

                Datos.g_selecciones[f1].jugadores.append(obj_jugador)
        txt_jugadores.close()
            
           
        
        
        
        f1 += 1
        # podria indicar otras cosas mas
    
    txt_selecciones.close()















def imprimir():  # prueba


    Datos.inicio = False

    for c in range(len(Datos.g_paises)):

        f"Nombre: {Datos.g_paises[c].nombre_pais}"
    
    for c in range(len(Datos.g_selecciones)):

        Datos.g_selecciones[c].calcular_fuerza()
        Datos.g_selecciones[c].mostrar_datos()





Crear_paises()
Crear_seleccion()
imprimir()