# Modulos
import Datos

from Modulo_Persona_FUT_ENT import Futbolista, Entrenador




#################################################################################################################################
#################################################################################################################################

# Clase Paises y Selecciones
# Herencia; Ninguna
# ------------------------------


# Clase constructor Pais
class Pais:


    def __init__(self, codigo_fifa, nombre_pais, continente, ranking_fifa):


        if isinstance(codigo_fifa, str) and isinstance(nombre_pais, str) and isinstance(continente, str) and isinstance(ranking_fifa, int):
                
                #if not inicio:
                    #registrar_pais()

                self.codigo_fifa = codigo_fifa      # Codigo de la FIFA
                self.nombre_pais = nombre_pais      # Nombre del Pais
                self.continente = continente        # Continente al que pertenece, Confederacion
                self.ranking_fifa = ranking_fifa    # Su Posicion en el tabla del Mundial

    
        else:
            return f"Error, datos incorrectos"
    




    # Objetivo ; permite modificar los atributos del objeto Pais 

    #E: recibe los siguientes parametros para modificar los atributos del objeto

    #S: retorna la modificacion de los atributos del objeto  |  la modificacion se aplicara en el archivo de texto correspondiente a paises

    #R: el codigo de fifa, nombre, contienente debe ser string(str)  |  el ranking debe ser un interger(int)

    def actualizar_datos(self, codigo_fifa, nombre, continente, ranking_fifa):
    # ------------------------------

        if isinstance(codigo_fifa, str) and isinstance(nombre, str) and isinstance(continente, str) and isinstance(ranking_fifa, int):
                
            # Variables
            nombre_viejo = self.nombre_pais
            lista_paises = []
            paises = []

            self.codigo_fifa = codigo_fifa      # Codigo de la FIFA
            self.nombre_pais = nombre           # Nombre del Pais
            self.continente = continente        # Continente al que pertenece, Confedereacion
            self.ranking_fifa = ranking_fifa    # Su Posicion en el tabla del Mundial

                


            """
            Descripcion ; el cambio se realizara en el archivo de texto posteior a la modificacion de los atributos del objeto pais, 
            la variable "paises" guardara todo lo que tenga el txt. de "lista_paises", luego en modo sobreescritura guarda cada pais en txt. 
            si se encuentra con el pais a modificar entonces realizara los cambios segun el contenido actual del objeto y se guardara en el txt.
            """
            lista_paises = open("paises.txt", "r")
            for linea in lista_paises:
                    
                pais = linea.strip().split(";")
                paises = paises + [pais]
            lista_paises.close()

            lista_paises = open("paises.txt", "w")
            for f in range(len(paises)):
                
                if paises[f][1] == nombre_viejo:
                    paises[f][0] = self.codigo_fifa
                    paises[f][1] = self.nombre_pais
                    paises[f][2] = self.continente
                    paises[f][3] = self.ranking_fifa
                
                lista_paises.write(paises[f][0] + ";" + paises[f][1] + ";" + paises[f][2] + ";" + f"{paises[f][3]}" + "\n")
            lista_paises.close()




        else:
            return f"Error, datos incorrectos"
    
#################################################################################################################################

# Clase constructor Selecciones
class Seleccion:

    def __init__(self, codigo_equipo, nom_pais):

        if isinstance(codigo_equipo, str) and isinstance(nom_pais, str):
                

                # buscara en la variable global de paises el objeto pais a incluir a la seleccion 
                for c in range(len(Datos.g_paises)):

                    if Datos.g_paises[c].nombre_pais == nom_pais:
                        pais = Datos.g_paises[c]

            
                #Bloque, gestionado por el usuario
                self.codigo_equipo = codigo_equipo
                self.pais = pais
                self.entrenador = ""
                self.jugadores = []

                # Bloque, gestionado por el programa
                self.total_goles_afavor = 0
                self.total_goles_encontra = 0
                self.total_tarjetas_amarillas = 0
                self.total_tarjetas_rojas = 0
                self.fuerza_equipo = 0

                if Datos.inicio == False:
                    print("validar")
        
        else:
            return f"Error, los datos ingresados no son validos"




    # Objetivo; mostrar la informacion especifica del objeto de seleccion

    #E: no recibe parametros aparte de si mismo

    #S: retorna la informacion del objeto

    #R: Ninguno

    def mostrar_datos(self):
    # ------------------------------

        print(f"== SELECCION ==")
        print(f"Escudo: {self.codigo_equipo}")
        f"Pais: {self.pais.nombre_pais}\n\n"
        f"== ENTRENADOR =="
        f"Entrenador: {self.entrenador.nombre}\n\n"
        f"== 11 OFICIAL =="
        for c in range(len(self.jugadores)):
            jugador = self.jugadores[c]
            
            f"Nombre: {jugador.nombre}  Apellido: {jugador.apellido}"
            f"Dorsal: {jugador.dorsal}"
            f"Posicion: {jugador.posicion}"
            f"Puntaje Individual: {jugador.calidad}"
            f"Tarjetas amarillas: {jugador.tarjeta_amarilla}  Tarjetas Rojas: {jugador.tarjeta_roja}"
            f"Goles: {jugador.goles}  Aistencias: {jugador.asistencias}"
    



    # Objetivo; agregar juagdores a al seleccion participante

    #E: recibe los parametros para la persona futbolista

    #S: retorna la creacion del objeto futbolista y se integra en la lista de juagdores de la seleccion

    #R: nombre, apellido, nacimiento, nacionalidad, posicion deben ser string(str)  |  dorsal, puntaje individual deben ser interger(int)

    def agregar_juagdor(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual):
    # ------------------------------
        
        if len(self.jugadores) <= 23:

            if isinstance(nombre, str) and isinstance(apellido, str) and (fecha_nacimiento, str) and isinstance(nacionalidad, str):

                if isinstance(dorsal, int) and isinstance(posicion, str) and isinstance(puntaje_individual, int):


            

                    """
                    Descripcion ; al ingresar un nuevo jugador primero se validara en la lista de jugadores no exista un jugandor
                    con el mismo nombre y apellido o con el mismo dorsal de no ser asi, el objeto futbolista se creara y se guardara en la lista de jugadores
                    """
                    for c in range(len(self.juagdores)):
                        jugador = self.jugadores[c]

                        if jugador.nombre == nombre and jugador.apellido == apellido or jugador.dorsal == dorsal:
                            return f"Error, no pueden existir dos jugadores iguales o con el mismo dorsal"
                    
                    # falta registrarlo
                    self.jugadores.append(Futbolista(nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual))
                



                else:
                    return f"Error, los datos del futbolista no son validos"
            
            else:
                return f"Error, los datos de la persona no son validos"
        
        else:
            return f"Error, la plantilla esta llena"
    



    # Objetivo; eliminar a un jugador de la plantilla

    #E: recibe el dorsal del futbolista a eliminar

    #S: retorna la eliminarcion del futbolista de la seleccion

    #R: el dorsal debe ser un entero  |  el futbolista a eliminar debe estar en la plantilla

    def eliminar_jugador(self, dorsal):
    # ------------------------------

        if isinstance(dorsal, int) and dorsal >= 0 and dorsal <= 100:
            if self.jugadores != []:


                
                # Variables
                nueva_lista = []        # aqui se incluyen los jugadores no marcados a eliminar
                lista_jugadores = []



                """
                Descripcion ; por cada jugador en la lista de jugadores, guardara en nueva_lista todo juagdor que no tenga el numero
                del dorsal que se plantea eliminar de la plantilla de la seleccion
                """
                for c in range(len(self.jugadores)):
                    jugador = self.jugadores[c]

                    if jugador.dorsal != dorsal:

                        nueva_lista = nueva_lista + [jugador]
                

                # Si nueva lista es igual a la lista de jugadores quiere decir que no se encontro al jugador
                if len(nueva_lista) == len(self.jugadores):
                    return f"Error, el jugador a eliminar no se encuentra en la plantilla"
                



                else:
                    self.jugadores = nueva_lista
                    nueva_lista = []

                    """
                    Descripcion ; posterior a la eliminacion del jugador de la plantilla, se buscara en la base de datos para eliminarlo igualmente.
                    "nueva_lista" guardara todo lo que este en el archivo de texto, luego cada jugador pasara a validarse su dorsal y equipo actual, si cumple alguna
                    entonces se guardara en el archivo de texto, de no cumplir ninguna es el jugador a eliminar.
                    """
                    lista_jugadores = open("jugadores.txt", "r")
                    for linea in lista_jugadores:
                        
                        nueva_lista = nueva_lista + [linea.strip().split(";")]
                    lista_jugadores.close()

                    lista_jugadores = open("jugadores.txt", "w")
                    for f in range(len(nueva_lista)):


                        # Se valida su dorsal y equipo al que pertenece
                        if nueva_lista[f][4] != dorsal or nueva_lista[f][7] != self.codigo_equipo:

                            lista_jugadores.write(f"{nueva_lista[f][0]};{nueva_lista[f][1]};{nueva_lista[f][2]};{nueva_lista[f][3]};{nueva_lista[f][4]};{nueva_lista[f][5]};{nueva_lista[f][6]};{nueva_lista[f][7]}\n")
                    lista_jugadores.close()

                    return f"Jugador eliminado!"
            



            else:
                return f"Error, no hay jugadores en la plantilla"
        
        else:
            return f"Error, el dato ingresado es invalido"
    



    # Objetivo; asignar un entrenador o remplazarlo

    #E: recibe los parametros para el objeto entrenador de la selecccion

    #S: retorna la creacion del objeto Entrenador y se integra como atributo de la seleccion

    #R: nombre, apellido, nacimiento, nacionalidad, posicion deben ser string(str)  |  años de experiencia un interger(int)

    def asignar_entrenador(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, años_experiencia, alineacion):
    # ------------------------------

        self.entrenador = Entrenador(nombre, apellido, fecha_nacimiento, nacionalidad, licencia, años_experiencia, alineacion)


        # Variables
        nueva_lista = []
        lista_entrenadores = [] 


        """
        Descripcion ; luego de cambiar de entrenador, hay que eliminarlo de la bsae de datos correspondiente a entrenadores.txt
        para validar eso, el entrenador no debe pertenecer al codigo de equipo del objeto especifico, y si lo es o si pertenece
        entonces hay que validar que sea el entrenador actual del objeto seleccion especifico, de no ser asi entonces es el entrenador
        a eliminar
        """
        lista_entrenadores = open("entrenadores.txt", "r")
        for linea in lista_entrenadores:

            nueva_lista = nueva_lista + [linea.strip().split(";")]
        lista_entrenadores.close()


        lista_entrenadores = open("entrenadores.txt", "w")
        for f in range(len(nueva_lista)):

            
            if not nueva_lista[f][7] == self.codigo_equipo:
               lista_entrenadores.write(f"{nueva_lista[f][0]};{nueva_lista[f][1]};{nueva_lista[f][2]};{nueva_lista[f][3]};{nueva_lista[f][4]};{nueva_lista[f][5]};{nueva_lista[f][6]};{nueva_lista[f][7]}\n")

            else:
                if nueva_lista[f][0] == self.entrenador.nombre:
                    lista_entrenadores.write(f"{nueva_lista[f][0]};{nueva_lista[f][1]};{nueva_lista[f][2]};{nueva_lista[f][3]};{nueva_lista[f][4]};{nueva_lista[f][5]};{nueva_lista[f][6]};{nueva_lista[f][7]}\n")

        lista_entrenadores.close()    
    

    # Objetivo;
    #E:
    #S:
    #R:

#################################################################################################################################
#################################################################################################################################

# Registrar paises y selecciones
# ------------------------------


# Objetivo; guardar la informacion del objeto pais en la base de datos correspondiente a paises.txt  |  evitar validaciones cada vez que el programa se ejecute

#E: recibe el objeto pais

#S: retorna la informacion del objeto pais en la base de datos

#R: la informacion del objeto pais no puede ser otra ya existente en la base de datos

#def registrar_pais(pais):
# ------------------------------