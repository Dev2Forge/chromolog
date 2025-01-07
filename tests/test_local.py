# Prueba con espositorio descargado localmente
# Esta prueba está hecha en un "Entorno virtual" (.env),
# sin tener instalado chromolog

import sys
# Añadir ruta para poder acceder localmente
sys.path.append('../chromolog/')
# Importar módulo localmente
import chromolog as ch

# Crear instancia
pt = ch.Print()
# Usar prueba del módulo
pt.test()

# Imrpimir información de clase
pt.inf(f"\n{pt}\n")

pt.warn(ch.chromolog.__doc__)

# error intencional
try:
    tutosrivegamer
except NameError as e:
    pt.exc(e)