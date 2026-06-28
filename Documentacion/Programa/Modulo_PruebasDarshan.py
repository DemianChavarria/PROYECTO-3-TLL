import Datos
from Clase_Partido import Partido

import Modulo_Ejecucion

from Clase_Grupo import Grupo


grupo1 = Grupo("A")

grupo1.agregar_equipo(Datos.g_selecciones[0])
grupo1.agregar_equipo(Datos.g_selecciones[1])
grupo1.agregar_equipo(Datos.g_selecciones[2])
grupo1.agregar_equipo(Datos.g_selecciones[3])

grupo1.generar_partidos()

grupo1.calcular_tabla()

print(grupo1.mostrar_tabla())