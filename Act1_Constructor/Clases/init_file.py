# __init__.py
# Archivo de inicialización del paquete Clases
# Este archivo permite que Python trate la carpeta Clases como un paquete

"""
Paquete Clases
Contiene las definiciones de clases del proyecto
"""

# Importar la clase Animal para facilitar su uso
from .animal import Animal

# Definir qué se exporta cuando se hace "from Clases import *"
__all__ = ['Animal']