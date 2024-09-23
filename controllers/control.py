from app import app
from models import *
from flask import render_template, request, jsonify
import json
import os

# Función para combinar archivos y generar reglas_cargadas.py usando rutas relativas
def generar_archivo_combinado():
    # Ruta del archivo reglas.txt (ruta relativa)
    ruta_txt = os.path.join('models', 'reglas', 'reglas.txt')
    # Ruta del archivo reglas_expertas.py (ruta relativa)
    ruta_reglas_expertas = os.path.join('models', 'reglas_expertas.py')
    # Nueva ruta para el archivo reglas_cargadas.py (ruta relativa)
    ruta_reglas_cargadas = os.path.join('models', 'reglas', 'reglas_cargadas.py')

    # Verificar si el archivo ya existe para evitar duplicados
    if os.path.exists(ruta_reglas_cargadas):
        print(f"El archivo {ruta_reglas_cargadas} ya existe. No se hará nada.")
        return ruta_reglas_cargadas

    # Leer el contenido del archivo reglas_expertas.py
    with open(ruta_reglas_expertas, 'r', encoding='utf-8') as f_expertas:
        contenido_expertas = f_expertas.read()

    # Leer el contenido del archivo reglas.txt
    with open(ruta_txt, 'r', encoding='utf-8') as f_txt:
        contenido_txt = f_txt.read()

    # Combinar el contenido de reglas_expertas.py con el contenido de reglas.txt
    contenido_combinado = f"{contenido_expertas}\n    {contenido_txt}"

    # Escribir el contenido combinado en el nuevo archivo reglas_cargadas.py
    with open(ruta_reglas_cargadas, 'w', encoding='utf-8') as f_cargadas:
        f_cargadas.write(contenido_combinado)

    print(f"Archivo {ruta_reglas_cargadas} generado correctamente.")
    return ruta_reglas_cargadas

@app.route("/")
def index():
    return render_template("bienvenida.html")

@app.route("/recomendaciones", methods=['GET', 'POST'])
def recomendaciones():
    if request.method == 'POST':
        # Generar el archivo combinado antes de continuar
        ruta_reglas_cargadas = generar_archivo_combinado()

        # Obtener los datos enviados por el formulario
        edad = request.form.get('edad')
        peso = request.form.get('peso')
        altura = request.form.get('altura')
        genero = request.form.get('gender')
        objetivo = request.form.get('objetivo')

        # Obtener las restricciones y condiciones como cadenas y dividirlas en listas
        restricciones_str = request.form.get('preferencias')
        condiciones_str = request.form.get('condiciones')

        # Dividir las cadenas en listas si no están vacías
        restricciones = restricciones_str.split(',') if restricciones_str else []
        condiciones = condiciones_str.split(',') if condiciones_str else []

        actividad_fisica = request.form.get('actividad_fisica')  # Nuevo campo

        # Crear el diccionario del usuario
        usuario = {
            "edad": int(edad),
            "peso": float(peso),
            "altura": float(altura) / 100,  # Convertir de cm a metros
            "genero": genero,
            "objetivo": objetivo,
            "preferencias": restricciones,  # Usar la lista de restricciones
            "condiciones_medicas": condiciones,  # Usar la lista de condiciones
            "actividad_fisica": actividad_fisica  # Nuevo campo añadido
        }

        # Convertir el diccionario de usuario a formato JSON
        usuario_json = json.dumps(usuario, indent=4)

        # Imprimir el JSON del usuario para depuración
        print("Datos del usuario en formato JSON:")
        print(usuario_json)

        # Obtener recomendaciones usando el motor de inferencia
        from knowledge.base_conocimiento import comidas
        from models.motor_experta import motor_inferencia

        # Pasamos la ruta del archivo combinado al motor de inferencia
        recomendaciones_dieta = motor_inferencia(usuario, comidas, ruta_reglas_cargadas)

        # Convertir las recomendaciones a formato JSON para imprimirlas también
        recomendaciones_json = json.dumps(recomendaciones_dieta, indent=4)
        print("Recomendaciones generadas en formato JSON:")
        print(recomendaciones_json)

        # Renderizar el template con las recomendaciones
        return render_template('resultado.html', recomendaciones=recomendaciones_dieta)

    return render_template("recomendacion.html")

@app.route("/manejar_indicacion", methods=['POST'])
def manejar_indicacion():
    data = request.get_json()
    indicacion = data.get('indicacion')
    respuesta = {
        "mensaje": "Mensaje recibido",
        "indicacion": indicacion
    }
    return jsonify(respuesta)
