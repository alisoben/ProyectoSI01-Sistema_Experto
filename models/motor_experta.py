import json
import os

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función de pertenencia trapezoidal con límites más flexibles
def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)

# Cargar las reglas difusas desde un archivo JSON
def cargar_reglas(archivo):
    try:
        with open(archivo, 'r') as f:
            reglas = json.load(f)
        return reglas
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: No se pudo leer el archivo JSON {archivo}.")
        return {}

# Cargar las recomendaciones desde la base de conocimientos
def cargar_recomendaciones(archivo):
    recomendaciones = {}
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                if ':' in linea:
                    try:
                        clave, recomendacion = linea.strip().split(':', 1)
                        recomendaciones[clave] = recomendacion.strip()
                    except ValueError:
                        print(f"Error al procesar la línea: {linea}")
                        continue
                else:
                    print(f"Línea malformada, sin separador ':': {linea}")
        return recomendaciones
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")
        return {}

# Evaluar las reglas basadas en el IMC, actividad física, género, preferencias, condiciones y objetivos
def evaluar_reglas(datos_usuario, reglas):
    resultados = {}
    for regla, condiciones in reglas.items():
        try:
            # Ampliamos los rangos de pertenencia difusa
            imc_fuzzy = trapezoidal(datos_usuario['imc'], *condiciones['imc'])
            actividad_fisica_fuzzy = trapezoidal(datos_usuario['actividad_fisica'], *condiciones['actividad_fisica'])
            
            # Permitir cierta flexibilidad en género y objetivo (usamos un rango continuo de pertenencia)
            genero_fuzzy = 1 if condiciones['genero'] == datos_usuario['genero'] else 0.8  # Se asigna 0.8 si el género no es exactamente igual
            objetivo_fuzzy = 1 if datos_usuario['objetivo'] == condiciones['objetivo'] else 0.8  # Flexibilidad en el objetivo

            # Condiciones médicas, evaluamos con cierta flexibilidad
            condiciones_medicas_fuzzy = sum([1 if condiciones[f'condicion_{i}'] == datos_usuario['condiciones'][i-1] else 0.8 for i in range(1, 5)]) / 4
            
            # Flexibilidad en las preferencias alimenticias
            preferencias_fuzzy = sum([1 - abs(condiciones[f'preferencia_{i}'] - datos_usuario['preferencias'][i-1]) for i in range(1, 5)]) / 4  # Suavizar la diferencia

            # Se puede optar por el producto o promedio para combinar
            resultado = (imc_fuzzy + actividad_fisica_fuzzy + genero_fuzzy + objetivo_fuzzy + condiciones_medicas_fuzzy + preferencias_fuzzy) / 6
            resultados[regla] = resultado
        except KeyError as e:
            print(f"Error: Falta una clave en las reglas - {e}")
            continue
    return resultados

# Seleccionar la recomendación basándose en la regla con mayor pertenencia
def obtener_recomendacion(resultados, recomendaciones, umbral=0.4):
    # Filtrar las reglas que superen el umbral de pertenencia
    reglas_validas = {regla: valor for regla, valor in resultados.items() if valor > umbral}
    
    if not reglas_validas:
        return "No se encontró una recomendación adecuada para tus características."
    
    # Elegir la regla con mayor valor de pertenencia
    mejor_regla = max(reglas_validas, key=reglas_validas.get)
    
    return recomendaciones.get(mejor_regla, "No se encontró una recomendación adecuada.")

# Definir la función 'motor_inferencia' para ser usada en el proyecto Flask
def motor_inferencia(usuario, ruta_base_conocimiento):
    # Cargar reglas y base de conocimientos
    reglas = cargar_reglas('models/reglas.json')

    print("Reglas cargadas:", reglas)

    if not reglas:
        return {"recomendaciones": "No se pudieron cargar las reglas."}
    
    recomendaciones = cargar_recomendaciones(ruta_base_conocimiento)
    print("Recomendaciones cargadas:", recomendaciones)

    if not recomendaciones:
        return {"recomendaciones": "No se pudieron cargar las recomendaciones."}

    # Evaluar reglas con los datos del usuario
    resultados = evaluar_reglas(usuario, reglas)
    print("Resultados de la evaluación de reglas:", resultados)

    # Obtener la recomendación con base en las reglas evaluadas y umbral mínimo
    recomendacion = obtener_recomendacion(resultados, recomendaciones)

    return {
        "recomendaciones": recomendacion
    }
