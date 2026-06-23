# Modulos
import Datos

from Clase_Persona_FUT_ENT import Futbolista, Entrenador




#################################################################################################################################
#################################################################################################################################

# Clase Paises y Selecciones
# Herencia; Ninguna
# ------------------------------


# Clase constructor Pais
class Pais:


    def __init__(self, codigo_fifa, nombre_pais, continente, ranking_fifa):


        if isinstance(codigo_fifa, str) and isinstance(nombre_pais, str) and isinstance(continente, str) and isinstance(ranking_fifa, int):
                

            self.codigo_fifa = codigo_fifa      # Codigo de la FIFA
            self.nombre_pais = nombre_pais      # Nombre del Pais
            self.continente = continente        # Continente al que pertenece, Confederacion
            self.ranking_fifa = ranking_fifa    # Su Posicion en el tabla del Mundial

    
        else:
            return f"Error, datos incorrectos"
    




    # Objetivo ; permite modificar los atributos del objeto Pais 

    #E: recibe los siguientes parametros para modificar los atributos del objeto

    #S: retorna la modificacion de los atributos del objeto  |  la modificacion se aplicara en el archivo de texto correspondiente a paises

    #R: el codigo de fifa, nombre_pais, contienente debe ser string(str)  |  el ranking debe ser un interger(int)

    def actualizar_datos(self, codigo_fifa, nombre_pais, continente, ranking_fifa):
    # ------------------------------

        if isinstance(codigo_fifa, str) and isinstance(nombre_pais, str) and isinstance(continente, str) and isinstance(ranking_fifa, int):
            

            # variables
            txt_paises = []



            """
            Descripcion ; 

            1. Validar que la modificacion de los atributos del objeto pais no sea igual a otra ya existente

            2. la modificacion se aplicara a los atributos del objeto especifico

            3. se buscara primero modificar la informacion del objeto pais especifico en la base de datos

            """



            # paso 1
            for c in range(len(Datos.g_paises)):

                if Datos.g_paises[c].codigo_fifa == codigo_fifa or Datos.g_paises[c].nombre_pais == nombre_pais:
                    return f"Error, la informacion del objeto a modificar ya se encuentra incluido"
                

            
            # paso 2
            self.codigo_fifa = codigo_fifa      # Codigo de la FIFA
            self.nombre_pais = nombre_pais      # Nombre del Pais
            self.continente = continente        # Continente al que pertenece, Confederacion
            self.ranking_fifa = ranking_fifa    # Su Posicion en el tabla del Mundial

            
            
            # paso 3
            txt_paises = open("paises.txt", "w")
            for c in range(len(Datos.g_paises)):

                txt_paises.write(f"{Datos.g_paises[c].codigo_fifa};{Datos.g_paises[c].nombre_pais};{Datos.g_paises[c].continente};{Datos.g_paises[c].ranking_fifa}")
                

            return f"Pais Modificado"







        else:
            return f"Error, datos incorrectos"
    
#################################################################################################################################

# Clase constructor Selecciones
class Seleccion:

    def __init__(self, codigo_equipo, nombre_pais):

        if isinstance(codigo_equipo, str) and isinstance(nombre_pais, str):
                

                # buscara en el Modulo de base de datos el pais a incluir a la seleccion
                for c in range(len(Datos.g_paises)):

                    if Datos.g_paises[c].nombre_pais == nombre_pais:
                        pais = Datos.g_paises[c]

            
                #Bloque, gestionado por el usuario
                self.codigo_equipo = codigo_equipo
                self.pais = pais
                self.entrenador = None
                self.jugadores = []

                # Bloque, gestionado por el programa
                self.titulares = [] 
                self.total_goles_afavor = 0
                self.total_goles_encontra = 0
                self.total_tarjetas_amarillas = 0
                self.total_tarjetas_rojas = 0
                self.fuerza_equipo = 0

        
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
        print(f"Pais: {self.pais.nombre_pais}")
        print(f"Fuerza de la Seleccion: {self.fuerza_equipo}\n\n")


        print(f"== ENTRENADOR ==")
        if self.entrenador == None:
            print("No tiene un entrenador asignado")
            print("")
        else:
            print(f"Entrenador: {self.entrenador.nombre}\n\n")
            print("")

            
        print(f"== 11 OFICIAL ==")
        print("")
        if self.jugadores == []:
            print("No hay juagdores en la plantilla")
        else:
            for c in range(len(self.jugadores)):
                jugador = self.jugadores[c]
                
                print(f"Nombre: {jugador.nombre}  Apellido: {jugador.apellido}")
                print(f"Dorsal: {jugador.dorsal}")
                print(f"Posicion: {jugador.posicion}")
                print(f"Puntaje Individual: {jugador.calidad}")
                print(f"Tarjetas amarillas: {jugador.tarjeta_amarilla}  Tarjetas Rojas: {jugador.tarjeta_roja}")
                print(f"Goles: {jugador.goles}  Aistencias: {jugador.asistencias}\n")

        
        print(f"\n\n")
        



    # Objetivo; agregar juagdores a al seleccion participante

    #E: recibe los parametros para la persona futbolista

    #S: retorna la creacion del objeto futbolista y se integra en la lista de juagdores de la seleccion

    #R: nombre, apellido, nacimiento, nacionalidad, posicion deben ser string(str)  |  dorsal, puntaje individual deben ser interger(int)

    def agregar_juagdor(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual):
    # ------------------------------
        
        if len(self.jugadores) <= 23:

            if isinstance(nombre, str) and isinstance(apellido, str) and (fecha_nacimiento, str) and isinstance(nacionalidad, str):

                if isinstance(dorsal, int) and isinstance(posicion, str) and isinstance(puntaje_individual, int):

                    

                    # Variable
                    txt_jugadores = []


                    """
                    Descripcion ; 
                    
                    1. Al ingresar un nuevo jugador primero se validara en la lista de jugadores del objeto seleccion no exista un jugandor
                    con el mismo nombre y apellido o con el mismo dorsal.
                    
                    2. La informacion del futbolista se guardara en el archivo de texto jugadores.txt.

                    3. El objeto futbolista se creara y se guardara en la lista de jugadores del objeto seleccion.

                    4. se realizara una validacion previa antes de calcular la fuerza de equipo

                    """


                    # Paso 1
                    for c in range(len(self.jugadores)):
                        jugador = self.jugadores[c]

                        if jugador.nombre == nombre and jugador.apellido == apellido or jugador.dorsal == dorsal:
                            return f"Error, no pueden existir dos jugadores iguales o con el mismo dorsal"
                    



                    # paso 2
                    txt_jugadores = open("jugadores.txt", "a")
                    txt_jugadores.write(f"{nombre};{apellido};{fecha_nacimiento};{nacionalidad};{dorsal};{posicion};{puntaje_individual};{self.codigo_equipo};{0};{0};{0};{0}\n")
                    txt_jugadores.close()




                    # paso 3
                    self.jugadores.append(Futbolista(nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual))




                    # paso 4
                    if len(self.jugadores) >= 11 and self.entrenador != None:
                        self.calcular_fuerza()
                



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
                txt_jugadores = []
                lista_jugadores = []



                """
                Descripcion ; por cada jugador en la lista de jugadores, guardara en lista_jugadores todo juagdor que no tenga el numero
                del dorsal que se plantea eliminar de la plantilla de la seleccion
                """
                for c in range(len(self.jugadores)):
                    jugador = self.jugadores[c]

                    if jugador.dorsal != dorsal:

                        lista_jugadores.append(jugador)
                

                # Si lista_jugadores es igual a la lista de jugadores del objeto seleccion quiere decir que no encontro al jugador
                if len(lista_jugadores) == len(self.jugadores):
                    return f"Error, el jugador a eliminar no se encuentra en la plantilla"
                



                else:
                    self.jugadores = lista_jugadores
                    lista_jugadores = []

                    """
                    Descripcion ; posterior a la eliminacion del jugador de la plantilla, se buscara en la base de datos para eliminarlo igualmente.
                    
                    1. "lista_jugadores" guardara todo lo que este en el archivo de texto.
                    
                    2. luego cada jugador pasara a validarse su dorsal y equipo actual, si cumple alguna
                    entonces se guardara en el archivo de texto, de no cumplir ninguna es el jugador a eliminar.

                    3. se realizara una validacion previa antes de calcular la fuerza de equipo.

                    """


                    # paso 1
                    txt_jugadores = open("jugadores.txt", "r")
                    for linea in txt_jugadores:
                        
                        lista_jugadores.append(linea.strip().split(";"))
                    txt_jugadores.close()






                    # paso 2
                    txt_jugadores = open("jugadores.txt", "w")
                    for f in range(len(lista_jugadores)):


                        # Se valida su dorsal y equipo al que pertenece
                        if lista_jugadores[f][4] != dorsal or lista_jugadores[f][7] != self.codigo_equipo:



                            lista_jugadores.write(f"{lista_jugadores[f][0]};{lista_jugadores[f][1]};{lista_jugadores[f][2]};{lista_jugadores[f][3]};{lista_jugadores[f][4]};{lista_jugadores[f][5]};{lista_jugadores[f][6]};{lista_jugadores[f][7]}\n")
                    txt_jugadores.close()




                    # paso 3
                    if len(self.jugadores) >= 11 and self.entrenador != None:
                        self.calcular_fuerza()




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
        lista_entrenadores = []
        txt_entrenadores = []


        """
        Descripcion ; 

        1. El entrenador nuevo se guardara en el atributo del objeto seleccion correspondiente.

        2. la informacion del nuevo entrenador se guardara en el archivo de texto "entrenadores.txt".

        3. se eliminara la informacion del entrenador remplazado de la seleccion objeto especifico.

        4. Se hara una validacion previa antes de calcular la fuerza de equipo

        """

        # PASO 1
        self.entrenador = Entrenador(nombre, apellido, fecha_nacimiento, nacionalidad, licencia, años_experiencia, alineacion)
        




        # PASO 2
        txt_entrenadores = open("entrenadores.txt", "a")
        txt_entrenadores.write(f"{nombre};{apellido};{fecha_nacimiento};{nacionalidad};{licencia};{años_experiencia};{alineacion};{self.codigo_equipo}")
        txt_entrenadores.close()





        # PASO 3
        txt_entrenadores = open("entrenadores.txt", "r")
        for linea in txt_entrenadores:

            lista_entrenadores.append(linea.strip().split(";"))
        txt_entrenadores.close()




        txt_entrenadores = open("entrenadores.txt", "w")
        for f in range(len(lista_entrenadores)):

            
            if not lista_entrenadores[f][7] == self.codigo_equipo:
               txt_entrenadores.write(f"{lista_entrenadores[f][0]};{lista_entrenadores[f][1]};{lista_entrenadores[f][2]};{lista_entrenadores[f][3]};{lista_entrenadores[f][4]};{lista_entrenadores[f][5]};{lista_entrenadores[f][6]};{lista_entrenadores[f][7]}\n")


            else:
                if lista_entrenadores[f][0] == self.entrenador.nombre:
                    txt_entrenadores.write(f"{lista_entrenadores[f][0]};{lista_entrenadores[f][1]};{lista_entrenadores[f][2]};{lista_entrenadores[f][3]};{lista_entrenadores[f][4]};{lista_entrenadores[f][5]};{lista_entrenadores[f][6]};{lista_entrenadores[f][7]}\n")


        txt_entrenadores.close()





        # paso 4
        if len(self.jugadores) >= 11 and self.entrenador != None:
            self.calcular_fuerza()



    # Objetivo; Calcular la fuerza de la seleccion

    #E: No recibe parametros aparte de si mismo

    #S: Retorna la fuerza que tiene el Objeto Seleccion del pais

    #R: Como minimo debe tener un entrenador y un jugador

    def calcular_fuerza(self):
    # ------------------------------

        """
        Descripcion ;

        1. se buscara a los 11 jugadores con mayor puntaje de la plantilla.

        2. los jugadores titulares se guardaran en la lista de titulares del objeto seleccion

        3. se realizara el calculo de la fuerza de objeto Seleccion especifico  |  sera neceario: 11 Jugadores, Un entrenador, La posicion actual del pais

        """ 

        

        if len(self.jugadores) >= 11 and self.entrenador != None:



            # Variables
            titulares = []
            jugador_seleccionado = None
            lista_jugadores = []
            jugadores_seleccion = self.jugadores
                
            suma_total = 0

            c = 1
            f = 0

                

            # paso 1
            while c <= 11:

                jugador_seleccionado = None
                lista_jugadores = []
                    


                for c1 in range(len(jugadores_seleccion)):

                    if jugador_seleccionado == None:
                        jugador_seleccionado = jugadores_seleccion[c1]
                        



                    if c1 + 1 < len(jugadores_seleccion):
                        if jugador_seleccionado.calidad >jugadores_seleccion[c1 + 1].calidad:
                                lista_jugadores.append(jugadores_seleccion[c1 + 1])
                            
                        else:
                            lista_jugadores.append(jugador_seleccionado)
                            jugador_seleccionado = jugadores_seleccion[c1 + 1]


                    else:
                        if jugador_seleccionado != []:
                            titulares.append(jugador_seleccionado)
                    


                jugadores_seleccion = lista_jugadores
                c += 1


            
            
            # paso 2
            self.titulares = titulares





            # paso 3
            for jugador in titulares:

                suma_total += jugador.calidad
                
            promedio_jugadores = suma_total / 11


            factor_entrenador = self.entrenador.experiencia * 4
            if factor_entrenador > 100:
                factor_entrenador = 100
                

            factor_ranking = 100 - self.pais.ranking_fifa

            self.fuerza_equipo = (promedio_jugadores * 0.6) + (factor_entrenador * 0.25) + (factor_ranking * 0.15)

            if self.fuerza_equipo > 100:
                self.fuerza_equipo = 100
                
            else:
                if self.fuerza_equipo < 1:
                    self.fuerza_equipo = 1
    




    # Objetivo; Guardar datos estadisticos de la seleccion para cada partido durante toda la competicion

    #E: recibe los parametros relacionados conteo de goles y conteo de tarjetas durante la competicion

    #S: retorna el total de goles a favor y en contra  |  tambien el total de tarjetas recibidas

    #R: ninguna

    def registrar_resultados(self, goles_afavor, goles_encontra, tarjetas_Amarillas, tarjetas_Rojas):
    # ------------------------------
    
        # Variables
        txt_selecciones = []

        self.total_goles_afavor += goles_afavor
        self.total_goles_encontra += goles_encontra
        self.total_tarjetas_amarillas += tarjetas_Amarillas
        self.total_tarjetas_rojas += tarjetas_Rojas





        txt_selecciones = open("selecciones.txt", "w")
        for c in range(len(Datos.g_selecciones)):

            txt_selecciones.write(f"{Datos.g_selecciones[c].codigo_equipo};{Datos.g_selecciones[c].pais};{Datos.g_selecciones[c].total_goles_afavor};{Datos.g_selecciones[c].total_goles_encontra};{Datos.g_selecciones[c].total_tarjetas_amarillas};{Datos.g_selecciones[c].total_tarjetas_rojas}\n")

        txt_selecciones.close()



#################################################################################################################################
#################################################################################################################################

# Registrar paises y selecciones
# ------------------------------


# Objetivo; guardar la informacion del objeto pais en la base de datos correspondiente a paises.txt  |  evitar validaciones cada vez que el programa se ejecute

#E: receibe los datos especificos para el objeto pais

#S: retorna la informacion del objeto pais en el Modulo de base de datos y en su archivo de texto correspondiente

#R: la informacion del objeto pais no puede ser otra ya existente en la base de datos  |  evitar guardarlo en el archivo de texto cada vez que el programa se ejecute

def registrar_pais(codigo_fifa, nombre_pais, continente, ranking_fifa):
# ------------------------------

    if Datos.inicio:

        return Pais(codigo_fifa, nombre_pais, continente, ranking_fifa)

    else:

        # Variables
        txt_paises = []


        for c in range(len(Datos.g_paises)):

            if Datos.g_paises[c].codigo_fifa == codigo_fifa or Datos.g_paises[c].nombre_pais == nombre_pais:
                return f"Error, los datos ingresados ya se encuentran incluidos"
            


        Datos.g_paises.append(Pais(codigo_fifa, nombre_pais, continente, ranking_fifa))



        txt_paises = open("paises.txt", "a")
        txt_paises.write(f"{codigo_fifa};{nombre_pais};{continente};{ranking_fifa}\n")

        txt_paises.close()






# Objetivo; guardar la informacion del objeto Seleccion en la base de datos correspondiente a selecciones.txt

#E: recibe los datos especificos para el objeto seleccion

#S: retorna la informacion del objeto seleccion en el Modulo de base de datos y en su archivo de texto correspondiente

#R: la informacion del objeto seleccion no puede ser otra ya existente en la base de datos  |  evitar guardarlo en el archivo de texto cada vez que el programa se ejecute

def registrar_seleccion(codigo_equipo, nombre_pais):

    if Datos.inicio:

        return Seleccion(codigo_equipo, nombre_pais)
    

    else:

        # variable
        txt_selecciones = []

        for c in range(len(Datos.g_selecciones)):

            if Datos.g_selecciones[c].codigo_equipo == codigo_equipo or Datos.g_selecciones[c].pais.nombre_pais == nombre_pais:
                return f"Error, los datos ya se encuentran incluidos"
        


        Datos.g_selecciones.append(Seleccion(codigo_equipo, nombre_pais))



        txt_selecciones = open("selecciones.txt", "a")
        txt_selecciones.write(f"{codigo_equipo};{nombre_pais};0;0;0;0\n")

        txt_selecciones.close()