import os

# Función para cargar las reglas desde el archivo reglas.txt
def cargar_reglas_desde_txt(ruta_reglas_txt):
    reglas = {}
    with open(ruta_reglas_txt, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Separar la regla binaria de la dieta asociada
            regla, dieta = linea.strip().split('->')
            regla = regla.replace(';', '').replace('A=', '').replace('G=', '').replace('O1=', '').replace('O2=', '').replace('O3=', '').replace('C1=', '').replace('C2=', '').replace('C3=', '').replace('C4=', '').replace('P1=', '').replace('P2=', '').replace('P3=', '').replace('P4=', '')
            reglas[regla] = dieta
    return reglas

# Función para cargar la base de conocimiento
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

# Función para convertir las preferencias del usuario en una cadena binaria
def convertir_usuario_a_binario(usuario):
    actividad = str(usuario["actividad_fisica"])
    genero = '1' if usuario["genero"] == 'M' else '0'

    o1 = '1' if usuario["objetivo"] == "bajar_peso" else '0'
    o2 = '1' if usuario["objetivo"] == "ganar_musculo" else '0'
    o3 = '1' if usuario["objetivo"] == "vida_saludable" else '0'

    p1 = str(usuario["preferencias"]["vegetariano"])
    p2 = str(usuario["preferencias"]["sin_lactosa"])
    p3 = str(usuario["preferencias"]["sin_gluten"])
    p4 = str(usuario["preferencias"]["bajo_carbohidratos"])

    c1 = str(usuario["condiciones_medicas"]["diabetes"])
    c2 = str(usuario["condiciones_medicas"]["hipertension"])
    c3 = str(usuario["condiciones_medicas"]["colesterol"])
    c4 = str(usuario["condiciones_medicas"]["anemia"])

    usuario_binario = f"{actividad}{genero}{o1}{o2}{o3}{c1}{c2}{c3}{c4}{p1}{p2}{p3}{p4}"
    return usuario_binario

# Motor de inferencia: toma al usuario y retorna las recomendaciones
def motor_inferencia(usuario, ruta_reglas_txt, ruta_base_conocimiento):
    print("Iniciando motor de inferencia con usuario:", usuario)

    # Convertir usuario a cadena binaria
    usuario_binario = convertir_usuario_a_binario(usuario)
    print(f"Usuario en binario: {usuario_binario}")

    reglas = cargar_reglas_desde_txt(ruta_reglas_txt)

    # Buscar si existe una coincidencia exacta en las reglas
    dieta_encontrada = reglas.get(usuario_binario)

    base_conocimiento = cargar_base_conocimiento(ruta_base_conocimiento)

    # Si no se encuentra la dieta, usar la dieta [Extra]
    if not dieta_encontrada:
        print("No se encontró una dieta exacta, usando la dieta [Extra].")
        dieta_encontrada = "Extra"

    print(f"Dieta encontrada: {dieta_encontrada}")

    # Obtener la dieta desde la base de conocimiento
    recomendaciones = base_conocimiento.get(dieta_encontrada, "No se encontró información en la base de conocimiento.")

    print("\nComidas recomendadas:\n")
    print(recomendaciones)
    return {
        "recomendaciones": recomendaciones
    }
