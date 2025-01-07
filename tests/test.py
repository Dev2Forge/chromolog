import sys
# Añadir ruta para poder acceder localmente
sys.path.append('../chromalog/')
# Importar módulo localmente
from chromalog.chromalog import Print

# Crear instancia
pt = Print()
# Usar prueba del módulo
pt.test()