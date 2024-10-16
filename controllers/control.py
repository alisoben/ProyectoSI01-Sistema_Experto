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
        actividad_fisica = float(request.form.get('actividad_fisica'))

        # Obtener los valores difusos para preferencias alimenticias
        preferencias = {
            "vegetariano": float(request.form.get('preferencias[vegetariano]')),
            "sin_lactosa": float(request.form.get('preferencias[sin_lactosa]')),
            "sin_gluten": float(request.form.get('preferencias[sin_gluten]')),
            "bajo_carbohidratos": float(request.form.get('preferencias[bajo_carbohidratos]'))
        }

        # Obtener los valores binarios para las condiciones médicas
        condiciones_medicas = {
            "diabetes": int(request.form.get('condiciones[diabetes]')),
            "hipertension": int(request.form.get('condiciones[hipertension]')),
            "colesterol": int(request.form.get('condiciones[colesterol]')),
            "anemia": int(request.form.get('condiciones[anemia]'))
        }

        # Crear el diccionario del usuario
        usuario = {
            "genero": genero,
            "objetivo": objetivo,
            "actividad_fisica": actividad_fisica,
            "preferencias": preferencias,
            "condiciones_medicas": condiciones_medicas
        }

        usuario_json = json.dumps(usuario, indent=4)
        print("Datos del usuario en formato JSON:")
        print(usuario_json)

        # Obtener recomendaciones usando el motor de inferencia con lógica difusa
        from models.motor_experta import motor_inferencia

        ruta_base_conocimiento = os.path.join('knowledge', 'base_conocimiento.txt')

        recomendaciones_dieta = motor_inferencia(usuario, ruta_base_conocimiento)

        # Desglosar las recomendaciones obtenidas
        if "recomendaciones" in recomendaciones_dieta:
            comidas = recomendaciones_dieta["recomendaciones"].split('\n')

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
