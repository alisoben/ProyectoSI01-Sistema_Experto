from app import app
from models import *
from flask import render_template, request, jsonify
import json
import os

@app.route("/")
def index():
    return render_template("bienvenida.html")

@app.route("/recomendaciones", methods=['GET', 'POST'])
def recomendaciones():
    if request.method == 'POST':
        # Obtener los datos enviados por el formulario
        genero = request.form.get('gender')
        objetivo = request.form.get('objetivo')
        actividad_fisica = int(request.form.get('actividad_fisica'))  # Ahora como 0 o 1

        # Obtener los valores binarios para preferencias y condiciones
        preferencias_bin = request.form.get('preferencias', '0000')
        condiciones_bin = request.form.get('condiciones', '0000')

        # Mapeo de las preferencias y condiciones con los valores binarios
        preferencias = {
            "vegetariano": int(preferencias_bin[0]),
            "sin_lactosa": int(preferencias_bin[1]),
            "sin_gluten": int(preferencias_bin[2]),
            "bajo_carbohidratos": int(preferencias_bin[3])
        }

        condiciones_medicas = {
            "diabetes": int(condiciones_bin[0]),
            "hipertension": int(condiciones_bin[1]),
            "colesterol": int(condiciones_bin[2]),
            "anemia": int(condiciones_bin[3])
        }

        # Crear el diccionario del usuario
        usuario = {
            "genero": genero,
            "objetivo": objetivo,
            "actividad_fisica": actividad_fisica,  # Guardado como 0 (Baja) o 1 (Alta)
            "preferencias": preferencias,
            "condiciones_medicas": condiciones_medicas
        }

        # Convertir el diccionario de usuario a formato JSON para depuración
        usuario_json = json.dumps(usuario, indent=4)
        print("Datos del usuario en formato JSON:")
        print(usuario_json)

        # Obtener recomendaciones usando el motor de inferencia
        from models.motor_experta import motor_inferencia

        # Ruta de los archivos
        ruta_reglas_txt = os.path.join('models', 'reglas.txt')
        # Ruta de los archivos
        ruta_base_conocimiento = os.path.join('knowledge', 'base_conocimiento.txt')


        recomendaciones_dieta = motor_inferencia(usuario, ruta_reglas_txt, ruta_base_conocimiento)

        # Desglosar las recomendaciones obtenidas (suponiendo que están en formato texto separado por saltos de línea)
        if "recomendaciones" in recomendaciones_dieta:
            comidas = recomendaciones_dieta["recomendaciones"].split('\n')

            # Extraer las comidas en base a su sección (Desayuno, Almuerzo, Cena)
            desayuno = next((line for line in comidas if line.startswith("Desayuno:")), "No disponible")
            almuerzo = next((line for line in comidas if line.startswith("Almuerzo:")), "No disponible")
            cena = next((line for line in comidas if line.startswith("Cena:")), "No disponible")

            # Pasar las comidas al template
            return render_template('resultado.html', recomendaciones={
                'desayuno': desayuno,
                'almuerzo': almuerzo,
                'cena': cena
            })

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
