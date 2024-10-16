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
        genero = 0 if request.form.get('gender') == 'M' else 1
        objetivo = {
              "bajar_peso": 1,
              "ganar_musculo": 2,
              "vida_saludable": 3
                   }.get(request.form.get('objetivo'))
        actividad_fisica = float(request.form.get('actividad_fisica'))

        # Obtener los datos de peso y altura para calcular el IMC
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        imc = peso / (altura ** 2)  # Calcular el IMC
        print(f"IMC calculado: {imc}")

        # Obtener los valores difusos para preferencias alimenticias
        # Ajustar nombres de claves para que coincidan con las reglas
        preferencias = [
          float(request.form.get('preferencias[vegetariano]', 0)),  # preferencia_1
          float(request.form.get('preferencias[sin_lactosa]', 0)),  # preferencia_2
          float(request.form.get('preferencias[sin_gluten]', 0)),  # preferencia_3
          float(request.form.get('preferencias[bajo_carbohidratos]', 0))  # preferencia_4 
          ]

        condiciones = [
          int(request.form.get('condiciones[diabetes]', 0)),  # condicion_1
          int(request.form.get('condiciones[hipertension]', 0)),  # condicion_2
          int(request.form.get('condiciones[colesterol]', 0)),  # condicion_3
          int(request.form.get('condiciones[anemia]', 0))  # condicion_4
        ]


        # Crear el diccionario del usuario
        usuario = {
            "genero": genero,
            "objetivo": objetivo,
            "actividad_fisica": actividad_fisica,
            "imc": imc,  # Añadimos el IMC calculado
            "preferencias": preferencias,
            "condiciones": condiciones  # Usamos la clave 'condiciones' en vez de 'condiciones_medicas'
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
            comidas = recomendaciones_dieta["recomendaciones"].split('. ')

            desayuno = next((line for line in comidas if line.startswith("Desayuno:")), "Quinua con maca")
            almuerzo = next((line for line in comidas if line.startswith("Almuerzo:")), "bife a la parrilla")
            cena = next((line for line in comidas if line.startswith("Cena:")), "yogurt con cereal")

            # Pasar las comidas al template
            return render_template('resultado.html', recomendaciones={
                'desayuno': desayuno,
                'almuerzo': almuerzo,
                'cena': cena
            })

    return render_template("recomendacion.html")
