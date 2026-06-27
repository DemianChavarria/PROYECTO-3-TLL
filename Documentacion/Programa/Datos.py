

# inicio del programa
"""
Descripcion; el programa debe reconstruir toda la informacion pero para ello puede ser necesario saltarse algunas validaciones o
problemas con la construccion de objetos, la variables impide que sucedan ciertas cosas que si deben de pasar con el usuario una vez finalizado la reconstruccion
"""
inicio = True


# Datos generales
"""
Descripcion ;  estos son los datos generales, es donde se pueden consultar todos los objetos creados y usarlos segun como lo necesite
"""
g_paises = []
g_selecciones = []
g_partidos = []




"""
Descripcion ; en "partidos_grupos" se guardaran todos los partidos de cada grupo 
cuando se juegue la fase grupos, los equipos que clasifiquen se guardaran en "equipos_grupos_clasificados"

Nota:  esto puede cambiar segun como lo acomode 
"""
# Fase Grupos
partidos_grupos = []
equipos_grupos_clasificados = []






"""
Descripcion ; en la fase eliminatorias una vez que la fase de grupos concluya los clasificados seran retornados a cada fase de eliminacion
se guardaran en partidos_16(16 - 8 - 4 - 2 - 1), los clasificados se guardaran en su clasificacion correspondiente 

por ejemplo

los clasificados de "partidos_16" se guardaran en "Clasificados_16"
"""
# Fase Eliminatorias
# ------------------

fases_txt = ["Fase de Grupos", "Dieciceisavos de Final", "Octavos de Final", "Cuartos de FInal", "Semifinales", "Final de la Copa del Mundo"]

# Dieciceisavos
partidos_16 = []
Clasificados_16 = []

# Octavos
partidos_8 = []
clasificados_8 = []

# Cuartos
partidos_4 = []
clasificados_4 = []

# semifinales
partidos_2 = []
clasificados_2 = []

# Final
partido_1 = None
campeon = None