import json
import os

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

# Evaluar el grado de pertenencia y seleccionar la categoría dominante
def evaluar_pertenencia_general(valor, conjuntos):
    resultado = {}
    for categoria, parametros in conjuntos.items():
        resultado[categoria] = trapezoidal(valor, *parametros)
    # Seleccionar la categoría con la pertenencia más alta
    categoria_dominante = max(resultado, key=resultado.get)
    return categoria_dominante, resultado[categoria_dominante]

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

# Clasificar valores de IMC y actividad física utilizando lógica difusa
def clasificar_imc(imc):
    conjuntos_imc = {
        "bajo": [0, 0, 18.5, 20],
        "medio": [18.5, 22, 24, 30],
        "alto": [24, 28, 35, 100]
    }
    return evaluar_pertenencia_general(imc, conjuntos_imc)

def clasificar_actividad_fisica(nivel_actividad):
    conjuntos_actividad = {
        "baja": [0, 0, 1, 2],
        "media": [1, 2, 3, 5],
        "alta": [3, 5, 6, 10]
    }
    return evaluar_pertenencia_general(nivel_actividad, conjuntos_actividad)

# Función para clasificar preferencias utilizando lógica difusa
def clasificar_preferencia(valor):
    conjuntos_preferencia = {
        "baja": [0, 0, 0.3, 0.4],
        "media": [0.3, 0.4, 0.6, 0.7],
        "alta": [0.6, 0.7, 1, 1]
    }
    return evaluar_pertenencia_general(valor, conjuntos_preferencia)

# Evaluar reglas basadas en el IMC, actividad física, género, preferencias, condiciones y objetivos
def evaluar_reglas(datos_usuario, reglas):
    resultados = {}
    imc_clasificado, _ = clasificar_imc(datos_usuario['imc'])
    actividad_clasificada, _ = clasificar_actividad_fisica(datos_usuario['actividad_fisica'])

    # Clasificar cada preferencia del usuario
    preferencias_clasificadas = [clasificar_preferencia(pref)[0] for pref in datos_usuario['preferencias']]

    for regla, condiciones in reglas["reglas"].items():
        try:
            # Verificar coincidencias exactas
            genero_match = condiciones['genero'] == datos_usuario['genero']
            objetivo_match = condiciones['objetivo'] == datos_usuario['objetivo']
            imc_match = condiciones['imc'] == imc_clasificado
            actividad_match = condiciones['actividad_fisica'] == actividad_clasificada
            
            # Evaluar coincidencias exactas de condiciones médicas
            condiciones_medicas_match = all(condiciones[f'condicion_{i}'] == datos_usuario['condiciones'][i-1] 
                                            for i in range(1, 5))
            
            # Evaluar coincidencias exactas de preferencias
            preferencias_match = all(condiciones[f'preferencia_{i}'] == preferencias_clasificadas[i-1] 
                                     for i in range(1, 5))

            # Calcular un puntaje general para la regla
            puntaje = (
                (1 if genero_match else 0) + 
                (1 if objetivo_match else 0) + 
                (1 if imc_match else 0) + 
                (1 if actividad_match else 0) + 
                (1 if condiciones_medicas_match else 0) + 
                (1 if preferencias_match else 0)
            ) / 6

            resultados[regla] = puntaje
        except KeyError as e:
            print(f"Error: Falta una clave en las reglas - {e}")
            continue
    return resultados


# Seleccionar la recomendación basada en la regla con mayor pertenencia
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
