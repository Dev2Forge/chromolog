import sys
# Añadir ruta para poder acceder localmente
sys.path.append('../chromolog/')
# Importar módulo localmente
from chromolog.chromolog import Print

# Crear instancia
pt = Print()
# Usar prueba del módulo
pt.test()