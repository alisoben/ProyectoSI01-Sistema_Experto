from experta import *

# Definimos los hechos: Usuario y Comida
class Usuario(Fact):
    """Información del usuario."""
    pass

class Comida(Fact):
    """Información de la comida."""
    pass

# Definimos el sistema de recomendación
class SistemaRecomendacion(KnowledgeEngine):
