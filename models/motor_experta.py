from experta import *
import random  # Para seleccionar aleatoriamente en caso de empate
import os

# Función para puntuar una comida basada en el motor de inferencia
def puntuar_comida(comida, usuario, ruta_reglas_cargadas):
    # Cargar las reglas desde el archivo combinado
    import importlib.util
    spec = importlib.util.spec_from_file_location("reglas_cargadas", ruta_reglas_cargadas)
    reglas = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reglas)

    # Crea el motor de inferencia basado en las reglas cargadas
    engine = reglas.SistemaRecomendacion()

    # Calcula el IMC del usuario
    imc = usuario["peso"] / (usuario["altura"] ** 2)

    # Inicializa el motor y pasa los hechos del Usuario
    engine.reset()  # Resetea las reglas
    engine.declare(reglas.Usuario(
        imc=imc,
        genero=usuario["genero"],
        edad=usuario["edad"],
        actividad_fisica=usuario["actividad_fisica"],
        condiciones_medicas=usuario.get("condiciones_medicas", []),
        preferencias=usuario.get("preferencias", []),
        objetivo=usuario["objetivo"]
    ))

    # Inicializa los hechos de Comida
    engine.declare(reglas.Comida(
        calorias=comida.get("calorias", 0),
        proteinas=comida.get("proteinas", 0),
        sodio=comida.get("sodio", 0),
        carbohidratos=comida.get("carbohidratos", 0),
        categorias=comida.get("categorias", [])
    ))

    # Ejecuta el motor de inferencia
    engine.run()

    # Aquí obtendríamos el puntaje acumulado
    puntaje = sum(fact['puntaje'] for fact in engine.facts.values() if 'puntaje' in fact)

    # Imprimir en consola el nombre de la comida y su puntaje
    print(f"Comida: {comida['nombre']}, Puntaje: {puntaje}")

    return puntaje

# Función para aplicar reglas a las comidas
def aplicar_reglas(comidas, tipo, usuario, ruta_reglas_cargadas, num_comidas=3):
    # Filtrar las comidas por el tipo (desayuno, almuerzo, cena, snack)
    comidas_filtradas = [comida for comida in comidas if comida["tipo"] == tipo]

    # Asegurarse de que hay comidas disponibles después de filtrar
    if not comidas_filtradas:
        print(f"No hay comidas disponibles para el tipo {tipo}.")
        return None, []

    # Puntuamos cada comida
    comidas_puntuadas = [(comida, puntuar_comida(comida, usuario, ruta_reglas_cargadas)) for comida in comidas_filtradas]

    # Ordenamos las comidas por su puntaje de mayor a menor
    comidas_ordenadas = sorted(comidas_puntuadas, key=lambda x: x[1], reverse=True)

    # Seleccionamos las tres comidas con mayor puntaje
    mejores_comidas = comidas_ordenadas[:num_comidas]

    # Obtener el puntaje más alto
    max_puntaje = mejores_comidas[0][1]  # Puntaje más alto entre las mejores comidas

    # Filtramos todas las comidas que tienen el puntaje máximo
    comidas_empate = [comida for comida, puntaje in comidas_ordenadas if puntaje == max_puntaje]

    # Imprimir todas las comidas que tienen el mismo puntaje en consola
    print(f"\nComidas con puntaje máximo de {max_puntaje} para {tipo.capitalize()}:")
    for idx, comida in enumerate(comidas_empate, start=1):
        print(f"{idx}. {comida['nombre']} - Puntaje: {max_puntaje}")

    # Reordenamos aleatoriamente la lista de comidas con el mismo puntaje
    random.shuffle(comidas_empate)
    print(f"\nComidas reordenadas aleatoriamente con el mismo puntaje para {tipo.capitalize()}:")
    for idx, comida in enumerate(comidas_empate, start=1):
        print(f"{idx}. {comida['nombre']}")

    print("\n")
    # Devolvemos las comidas reordenadas
    return comidas_empate

# Motor de inferencia híbrido: encadenamiento hacia atrás con puntuación heurística
def motor_inferencia(usuario, comidas, ruta_reglas_cargadas):
    print("Iniciando motor de inferencia con usuario:", usuario)

    # Obtenemos las mejores comidas por cada tipo y las mostramos por consola
    desayuno = aplicar_reglas(comidas, "desayuno", usuario, ruta_reglas_cargadas)
    almuerzo = aplicar_reglas(comidas, "almuerzo", usuario, ruta_reglas_cargadas)
    cena = aplicar_reglas(comidas, "cena", usuario, ruta_reglas_cargadas)
    snack = aplicar_reglas(comidas, "snack", usuario, ruta_reglas_cargadas)

    # Si no hay recomendaciones, devolvemos un valor predeterminado
    dieta_detallada = {
        "desayuno": desayuno or {"nombre": "No hay recomendación de desayuno"},
        "almuerzo": almuerzo or {"nombre": "No hay recomendación de almuerzo"},
        "cena": cena or {"nombre": "No hay recomendación de cena"},
        "snack": snack or {"nombre": "No hay recomendación de snack"}
    }

    return dieta_detallada
