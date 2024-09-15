# motor_inferencia.py

from models.reglas import puntuar_comida

def aplicar_reglas(comidas, tipo, usuario, num_comidas=1):
    comidas_filtradas = [comida for comida in comidas if comida["tipo"] == tipo]
    comidas_puntuadas = [(comida, puntuar_comida(comida, usuario)) for comida in comidas_filtradas]

    # Ordenar por puntaje y seleccionar las mejores
    comidas_ordenadas = sorted(comidas_puntuadas, key=lambda x: x[1], reverse=True)

    mejores_comidas = [comida for comida, puntaje in comidas_ordenadas[:num_comidas]]
   
    return mejores_comidas    

# Motor de inferencia híbrido: encadenamiento hacia atrás con puntuación heurística
def motor_inferencia(usuario, comidas):
    print("Iniciando motor de inferencia con usuario:", usuario)
    
    dieta_detallada = {
        "desayuno": aplicar_reglas(comidas, "desayuno", usuario),
        "almuerzo": aplicar_reglas(comidas, "almuerzo", usuario),
        "cena": aplicar_reglas(comidas, "cena", usuario),
        "snack": aplicar_reglas(comidas, "snack", usuario)
    }
    
    return dieta_detallada
