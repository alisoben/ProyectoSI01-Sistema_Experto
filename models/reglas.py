# reglas.py

def puntuar_comida(comida, usuario):
    puntaje = 0

    # Calcular IMC usando peso y altura
    imc = usuario["peso"] / (usuario["altura"] ** 2)

    # 1. Reglas basadas en el IMC
    if imc >= 25 and comida.get("calorias", 0) <= 300:
        puntaje += 25  # Comidas bajas en calorías para personas con sobrepeso/obesidad
    elif imc < 18.5 and comida.get("calorias", 0) >= 400:
        puntaje += 15  # Personas con bajo peso necesitan más calorías

    # 2. Género
    if usuario["genero"] == "M" and comida.get("calorias", 0) >= 500:
        puntaje += 10  # Los hombres tienden a necesitar más calorías
    elif usuario["genero"] == "F" and comida.get("calorias", 0) <= 500:
        puntaje += 10  # Control de calorías más común en mujeres
    elif usuario["genero"] == "F" and comida.get("proteinas", 0) >= 15:
        puntaje += 15  # Aumentar proteínas es importante para las mujeres

    # 3. Nivel de actividad física 
    if usuario["actividad_fisica"] == "alto" and comida.get("proteinas", 0) >= 20:
        puntaje += 30  # Alta proteína para actividades físicas intensas
    elif usuario["actividad_fisica"] == "moderado" and comida.get("proteinas", 0) >= 15:
        puntaje += 20  # Moderado nivel de actividad, requiere proteína pero menos
    elif usuario["actividad_fisica"] == "baja" and comida.get("calorias", 0) <= 300:
        puntaje += 25  # Personas con actividad baja deben controlar más las calorías

    # 4. Edad
    if usuario["edad"] < 18:
        if comida.get("calorias", 0) >= 600:
            puntaje += 10  # Los adolescentes requieren más calorías
        if comida.get("proteinas", 0) >= 20:
            puntaje += 20  # Proteínas necesarias para el crecimiento
    elif 18 <= usuario["edad"] < 30:
        if comida.get("calorias", 0) >= 500:
            puntaje += 10  # Los jóvenes pueden requerir más calorías
        if comida.get("proteinas", 0) >= 15:
            puntaje += 15  # Las proteínas son clave a esta edad
    elif 30 <= usuario["edad"] <= 50:
        if comida.get("calorias", 0) <= 400:
            puntaje += 20  # Control de calorías recomendado para adultos
        if comida.get("grasas", 0) <= 10:
            puntaje += 15  # Control de grasas importante en esta etapa
    elif 51 <= usuario["edad"] <= 65:
        if comida.get("proteinas", 0) >= 20:
            puntaje += 30  # Los mayores de 50 necesitan más proteínas
        if comida.get("calorias", 0) <= 350:
            puntaje += 20  # Control de calorías también importante
    elif usuario["edad"] > 65:
        if comida.get("proteinas", 0) >= 20:
            puntaje += 35  # Mayor énfasis en proteínas para personas mayores
        if comida.get("calorias", 0) <= 300:
            puntaje += 25  # Control estricto de calorías en personas mayores

    # 5. Condiciones médicas
    if "diabetes" in usuario["condiciones_medicas"] and comida.get("carbohidratos", 0) <= 20:
        puntaje += 30  # Control estricto de carbohidratos es vital para la diabetes
    if "enfermedad celíaca" in usuario["condiciones_medicas"] and "sin gluten" in comida.get("categorias", []):
        puntaje += 35  # La comida sin gluten es esencial para los celiacos
    if "hipertension" in usuario["condiciones_medicas"] and comida.get("sodio", 0) <= 100:
        puntaje += 25  # Control del sodio es clave para la hipertensión
    if "colesterol alto" in usuario["condiciones_medicas"] and comida.get("grasas", 0) <= 10:
        puntaje += 30  # Control de grasas y colesterol es muy importante
    if "anemia" in usuario["condiciones_medicas"] and "hierro" in comida.get("nutrientes", []):
        puntaje += 35  # El hierro es vital para personas con anemia
    if "hipotiroidismo" in usuario["condiciones_medicas"] and comida.get("yodo", 0) >= 30:
        puntaje += 25  # Las comidas con yodo pueden ayudar a pacientes con hipotiroidismo
    if "intolerancia a la lactosa" in usuario["condiciones_medicas"] and "sin lactosa" in comida.get("categorias", []):
        puntaje += 30  # Las comidas sin lactosa son cruciales para esta condición
    if "insuficiencia renal" in usuario["condiciones_medicas"] and comida.get("proteinas", 0) <= 15:
        puntaje += 30  # Control estricto de proteínas en insuficiencia renal
    if "alergia a los frutos secos" in usuario["condiciones_medicas"] and "sin frutos secos" in comida.get("categorias", []):
        puntaje += 35  # Evitar frutos secos es fundamental para alérgicos
    if "obesidad" in usuario["condiciones_medicas"] and comida.get("calorias", 0) <= 300:
        puntaje += 30  # Control calórico esencial en personas con obesidad

    # 6. Preferencias alimenticias
    if any(pref in comida.get("categorias", []) for pref in usuario["preferencias"]):
        puntaje += 20  

    return puntaje
