import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Función para cargar la base de conocimiento (no cambia)
def cargar_base_conocimiento(ruta_base_conocimiento):
    base_conocimiento = {}
    with open(ruta_base_conocimiento, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        secciones = contenido.split("[")
        for seccion in secciones:
            if seccion.strip():
                nombre_dieta, detalles = seccion.split("]", 1)
                base_conocimiento[nombre_dieta.strip()] = detalles.strip()
    return base_conocimiento

# Definir la lógica difusa para las preferencias y actividad física
def configurar_sistema_difuso():
    # Crear las variables difusas
    actividad_fisica = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'actividad_fisica')
    vegetariano = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'vegetariano')
    sin_lactosa = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'sin_lactosa')
    sin_gluten = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'sin_gluten')
    bajo_carbohidratos = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'bajo_carbohidratos')

    recomendacion = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'recomendacion')

    # Definir las funciones de pertenencia
    actividad_fisica['baja'] = fuzz.trimf(actividad_fisica.universe, [0, 0, 0.5])
    actividad_fisica['media'] = fuzz.trimf(actividad_fisica.universe, [0.25, 0.5, 0.75])
    actividad_fisica['alta'] = fuzz.trimf(actividad_fisica.universe, [0.5, 1, 1])

    vegetariano['bajo'] = fuzz.trimf(vegetariano.universe, [0, 0, 0.5])
    vegetariano['medio'] = fuzz.trimf(vegetariano.universe, [0.25, 0.5, 0.75])
    vegetariano['alto'] = fuzz.trimf(vegetariano.universe, [0.5, 1, 1])

    sin_lactosa['bajo'] = fuzz.trimf(sin_lactosa.universe, [0, 0, 0.5])
    sin_lactosa['medio'] = fuzz.trimf(sin_lactosa.universe, [0.25, 0.5, 0.75])
    sin_lactosa['alto'] = fuzz.trimf(sin_lactosa.universe, [0.5, 1, 1])

    sin_gluten['bajo'] = fuzz.trimf(sin_gluten.universe, [0, 0, 0.5])
    sin_gluten['medio'] = fuzz.trimf(sin_gluten.universe, [0.25, 0.5, 0.75])
    sin_gluten['alto'] = fuzz.trimf(sin_gluten.universe, [0.5, 1, 1])

    bajo_carbohidratos['bajo'] = fuzz.trimf(bajo_carbohidratos.universe, [0, 0, 0.5])
    bajo_carbohidratos['medio'] = fuzz.trimf(bajo_carbohidratos.universe, [0.25, 0.5, 0.75])
    bajo_carbohidratos['alto'] = fuzz.trimf(bajo_carbohidratos.universe, [0.5, 1, 1])

    # Recomendaciones de dieta difusas
    recomendacion['baja'] = fuzz.trimf(recomendacion.universe, [0, 0, 0.5])
    recomendacion['media'] = fuzz.trimf(recomendacion.universe, [0.25, 0.5, 0.75])
    recomendacion['alta'] = fuzz.trimf(recomendacion.universe, [0.5, 1, 1])

    # Definir reglas difusas (ejemplo sencillo)
    regla1 = ctrl.Rule(actividad_fisica['alta'] & vegetariano['alto'], recomendacion['alta'])
    regla2 = ctrl.Rule(sin_lactosa['bajo'] & sin_gluten['alto'], recomendacion['media'])
    regla3 = ctrl.Rule(bajo_carbohidratos['medio'] & actividad_fisica['media'], recomendacion['baja'])

    # Crear el sistema de control difuso
    sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])

    return ctrl.ControlSystemSimulation(sistema_control)

# Función para ejecutar el motor difuso y obtener la recomendación
def ejecutar_motor_difuso(usuario):
    sistema_difuso = configurar_sistema_difuso()

    # Ingresar los valores del usuario
    print("Entradas del usuario para el sistema difuso:")
    print(f"Actividad física: {usuario['actividad_fisica']}")
    print(f"Vegetariano: {usuario['preferencias']['vegetariano']}")
    print(f"Sin lactosa: {usuario['preferencias']['sin_lactosa']}")
    print(f"Sin gluten: {usuario['preferencias']['sin_gluten']}")
    print(f"Bajo carbohidratos: {usuario['preferencias']['bajo_carbohidratos']}")

    # Ingresar los valores del usuario
    sistema_difuso.input['actividad_fisica'] = usuario['actividad_fisica']
    sistema_difuso.input['vegetariano'] = usuario['preferencias']['vegetariano']
    sistema_difuso.input['sin_lactosa'] = usuario['preferencias']['sin_lactosa']
    sistema_difuso.input['sin_gluten'] = usuario['preferencias']['sin_gluten']
    sistema_difuso.input['bajo_carbohidratos'] = usuario['preferencias']['bajo_carbohidratos']

    # Calcular el resultado
    sistema_difuso.compute()

    return sistema_difuso.output['recomendacion']

# Motor de inferencia que integra la lógica difusa
def motor_inferencia(usuario, ruta_base_conocimiento):
    print("Iniciando motor de inferencia con lógica difusa...")

    # Ejecutar el motor difuso y obtener la recomendación
    resultado_difuso = ejecutar_motor_difuso(usuario)
    print(f"Recomendación difusa: {resultado_difuso}")

    # Cargar la base de conocimiento
    base_conocimiento = cargar_base_conocimiento(ruta_base_conocimiento)

    # Seleccionar la dieta en base al resultado difuso (adaptado)
    if resultado_difuso >= 0.66:
        dieta_encontrada = "Alta"
    elif resultado_difuso >= 0.33:
        dieta_encontrada = "Media"
    else:
        dieta_encontrada = "Baja"

    # Obtener la dieta desde la base de conocimiento
    recomendaciones = base_conocimiento.get(dieta_encontrada, "No se encontró información en la base de conocimiento.")

    print("\nComidas recomendadas:\n", recomendaciones)
    return {
        "recomendaciones": recomendaciones
    }
