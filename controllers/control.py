from app import app
from models import *
from flask import render_template, request, jsonify
import json  # Asegúrate de importar json

@app.route("/")
def index():
    return render_template("bienvenida.html")


@app.route("/recomendaciones", methods=['GET', 'POST'])
def recomendaciones():
    if request.method == 'POST':
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
    #    Para usar el motor de inferencia con anteior usar el de abajo :v
    #    from models.motor_inferencia import motor_inferencia

        recomendaciones_dieta = motor_inferencia(usuario, comidas)
        
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
