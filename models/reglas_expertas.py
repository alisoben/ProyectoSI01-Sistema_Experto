from experta import *

# Definimos los hechos: Usuario y Comida
class Usuario(Fact):
    """Información del usuario."""
    pass

class Comida(Fact):
    """Información de la comida."""
    pass

# Definimos el sistema de recomendación
class SistemaRecomendacion(KnowledgeEngine):

    # 1. Reglas basadas en el IMC y calorías
    @Rule(Usuario(imc=P(lambda imc: imc >= 30)), Comida(calorias=P(lambda calorias: calorias < 200)))
    def comida_muy_baja_calorias_obesidad(self):
        self.declare(Fact(puntaje=50))  # Obesidad con comidas muy bajas en calorías

    @Rule(Usuario(imc=P(lambda imc: imc >= 30)), Comida(calorias=P(lambda calorias: 200 <= calorias <= 300)))
    def comida_baja_calorias_obesidad(self):
        self.declare(Fact(puntaje=40))  # Obesidad con comidas moderadamente bajas en calorías

    @Rule(Usuario(imc=P(lambda imc: imc >= 30)), Comida(calorias=P(lambda calorias: calorias > 300)))
    def comida_media_calorias_obesidad(self):
        self.declare(Fact(puntaje=10))  # Penalizar comidas con más de 300 calorías para personas con obesidad

    @Rule(Usuario(imc=P(lambda imc: 25 <= imc < 30)), Comida(calorias=P(lambda calorias: calorias < 200)))
    def comida_muy_baja_calorias_sobrepeso(self):
        self.declare(Fact(puntaje=40))

    @Rule(Usuario(imc=P(lambda imc: 25 <= imc < 30)), Comida(calorias=P(lambda calorias: 200 <= calorias <= 300)))
    def comida_baja_calorias_sobrepeso(self):
        self.declare(Fact(puntaje=30))

    @Rule(Usuario(imc=P(lambda imc: 25 <= imc < 30)), Comida(calorias=P(lambda calorias: calorias > 300)))
    def comida_media_calorias_sobrepeso(self):
        self.declare(Fact(puntaje=5))  # Penalización leve por sobrepeso

    @Rule(Usuario(imc=P(lambda imc: imc < 18.5)), Comida(calorias=P(lambda calorias: calorias >= 400)))
    def comida_alta_calorias_bajo_peso(self):
        self.declare(Fact(puntaje=25))  # Personas con bajo peso necesitan más calorías

    # 2. Reglas basadas en el género y proteínas
    @Rule(Usuario(genero="M"), Comida(proteinas=P(lambda proteinas: proteinas >= 20)))
    def hombre_alta_proteina(self):
        self.declare(Fact(puntaje=20))

    @Rule(Usuario(genero="M"), Comida(proteinas=P(lambda proteinas: 10 <= proteinas < 20)))
    def hombre_moderada_proteina(self):
        self.declare(Fact(puntaje=10))

    @Rule(Usuario(genero="F"), Comida(proteinas=P(lambda proteinas: proteinas >= 15)))
    def mujer_alta_proteinas(self):
        self.declare(Fact(puntaje=20))

    @Rule(Usuario(genero="F"), Comida(proteinas=P(lambda proteinas: 10 <= proteinas < 15)))
    def mujer_moderada_proteinas(self):
        self.declare(Fact(puntaje=10))

    @Rule(Usuario(genero="M"), Comida(proteinas=P(lambda proteinas: 5 <= proteinas < 10)))
    def hombre_baja_proteina(self):
        self.declare(Fact(puntaje=5))

    # 3. Reglas basadas en el nivel de actividad física
    # **Actividad física alta**: más proteínas y calorías necesarias
    @Rule(Usuario(actividad_fisica="alto"), Comida(proteinas=P(lambda proteinas: proteinas >= 25)))
    def alta_proteina_muy_alto_ejercicio(self):
        self.declare(Fact(puntaje=50))  # Gran cantidad de proteínas para ejercicios intensos

    @Rule(Usuario(actividad_fisica="alto"), Comida(proteinas=P(lambda proteinas: 20 <= proteinas < 25)))
    def alta_proteina_alto_ejercicio(self):
        self.declare(Fact(puntaje=40))  # Proteínas suficientes para mantener actividad alta

    @Rule(Usuario(actividad_fisica="alto"), Comida(proteinas=P(lambda proteinas: 15 <= proteinas < 20)))
    def moderada_proteina_alto_ejercicio(self):
        self.declare(Fact(puntaje=20))  # Proteínas moderadas, aceptables para actividad alta

    @Rule(Usuario(actividad_fisica="alto"), Comida(proteinas=P(lambda proteinas: proteinas < 15)))
    def baja_proteina_alto_ejercicio(self):
        self.declare(Fact(puntaje=-10))  # Penalización: proteína baja para actividad alta

    # Para comidas con alto contenido calórico en usuarios de actividad alta
    @Rule(Usuario(actividad_fisica="alto"), Comida(calorias=P(lambda calorias: calorias >= 500)))
    def alta_calorias_alto_ejercicio(self):
        self.declare(Fact(puntaje=40))  # Se requiere una cantidad alta de calorías para actividad intensa

    @Rule(Usuario(actividad_fisica="alto"), Comida(calorias=P(lambda calorias: 400 <= calorias < 500)))
    def moderada_calorias_alto_ejercicio(self):
        self.declare(Fact(puntaje=30))  # Aceptable cantidad de calorías

    @Rule(Usuario(actividad_fisica="alto"), Comida(calorias=P(lambda calorias: 300 <= calorias < 400)))
    def baja_calorias_alto_ejercicio(self):
        self.declare(Fact(puntaje=10))  # Un poco bajo para actividad intensa

    @Rule(Usuario(actividad_fisica="alto"), Comida(calorias=P(lambda calorias: calorias < 300)))
    def muy_baja_calorias_alto_ejercicio(self):
        self.declare(Fact(puntaje=-20))  # Penalización por calorías insuficientes

    # **Actividad física moderada**: moderación en proteínas y calorías
    @Rule(Usuario(actividad_fisica="moderado"), Comida(proteinas=P(lambda proteinas: 20 <= proteinas < 25)))
    def moderada_proteina_moderado_ejercicio(self):
        self.declare(Fact(puntaje=30))  # Proteínas adecuadas para actividad moderada

    @Rule(Usuario(actividad_fisica="moderado"), Comida(proteinas=P(lambda proteinas: 15 <= proteinas < 20)))
    def moderada_proteina_para_moderado_ejercicio(self):
        self.declare(Fact(puntaje=20))  # Proteínas moderadas para actividad moderada

    @Rule(Usuario(actividad_fisica="moderado"), Comida(proteinas=P(lambda proteinas: proteinas < 15)))
    def baja_proteina_moderado_ejercicio(self):
        self.declare(Fact(puntaje=-10))  # Penalización por baja proteína

    # Para calorías en usuarios con actividad moderada
    @Rule(Usuario(actividad_fisica="moderado"), Comida(calorias=P(lambda calorias: 400 <= calorias < 500)))
    def alta_calorias_moderado_ejercicio(self):
        self.declare(Fact(puntaje=30))  # Calorías altas pero aceptables

    @Rule(Usuario(actividad_fisica="moderado"), Comida(calorias=P(lambda calorias: 300 <= calorias < 400)))
    def moderada_calorias_moderado_ejercicio(self):
        self.declare(Fact(puntaje=20))  # Calorías moderadas adecuadas

    @Rule(Usuario(actividad_fisica="moderado"), Comida(calorias=P(lambda calorias: 200 <= calorias < 300)))
    def baja_calorias_moderado_ejercicio(self):
        self.declare(Fact(puntaje=10))  # Un poco bajo para actividad moderada

    @Rule(Usuario(actividad_fisica="moderado"), Comida(calorias=P(lambda calorias: calorias < 200)))
    def muy_baja_calorias_moderado_ejercicio(self):
        self.declare(Fact(puntaje=-20))  # Penalización por calorías insuficientes

    # **Actividad física baja**: se deben evitar las calorías altas y demasiadas proteínas
    @Rule(Usuario(actividad_fisica="baja"), Comida(proteinas=P(lambda proteinas: 15 <= proteinas < 20)))
    def alta_proteina_baja_ejercicio(self):
        self.declare(Fact(puntaje=20))  # Cantidad aceptable de proteínas

    @Rule(Usuario(actividad_fisica="baja"), Comida(proteinas=P(lambda proteinas: 10 <= proteinas < 15)))
    def moderada_proteina_baja_ejercicio(self):
        self.declare(Fact(puntaje=10))  # Un nivel bajo pero suficiente de proteínas

    @Rule(Usuario(actividad_fisica="baja"), Comida(proteinas=P(lambda proteinas: proteinas < 10)))
    def baja_proteina_baja_ejercicio(self):
        self.declare(Fact(puntaje=5))  # Aceptable pero bajo para actividad física baja

    @Rule(Usuario(actividad_fisica="baja"), Comida(proteinas=P(lambda proteinas: proteinas >= 20)))
    def demasiado_alta_proteina_baja_ejercicio(self):
        self.declare(Fact(puntaje=-20))  # Penalización por proteínas en exceso para actividad baja

    # Para comidas con calorías bajas en usuarios de actividad baja
    @Rule(Usuario(actividad_fisica="baja"), Comida(calorias=P(lambda calorias: 200 <= calorias < 300)))
    def moderada_calorias_baja_ejercicio(self):
        self.declare(Fact(puntaje=30))  # Se requiere una cantidad moderada de calorías para actividad baja

    @Rule(Usuario(actividad_fisica="baja"), Comida(calorias=P(lambda calorias: calorias < 200)))
    def baja_calorias_baja_ejercicio(self):
        self.declare(Fact(puntaje=40))  # Buenas comidas bajas en calorías

    @Rule(Usuario(actividad_fisica="baja"), Comida(calorias=P(lambda calorias: 300 <= calorias < 400)))
    def demasiadas_calorias_baja_ejercicio(self):
        self.declare(Fact(puntaje=10))  # Un poco alto en calorías, pero aceptable

    @Rule(Usuario(actividad_fisica="baja"), Comida(calorias=P(lambda calorias: calorias > 400)))
    def exceso_calorias_baja_ejercicio(self):
        self.declare(Fact(puntaje=-30))  # Penalización por calorías en exceso

    # 4. Reglas basadas en la edad
    @Rule(Usuario(edad=P(lambda edad: edad < 18)), Comida(calorias=P(lambda calorias: calorias >= 600)))
    def adolescente_alta_calorias(self):
        self.declare(Fact(puntaje=10))

    @Rule(Usuario(edad=P(lambda edad: edad < 18)), Comida(proteinas=P(lambda proteinas: proteinas >= 20)))
    def adolescente_alta_proteinas(self):
        self.declare(Fact(puntaje=20))

    @Rule(Usuario(edad=P(lambda edad: 18 <= edad < 30)), Comida(calorias=P(lambda calorias: calorias >= 500)))
    def joven_alta_calorias(self):
        self.declare(Fact(puntaje=10))

    @Rule(Usuario(edad=P(lambda edad: 18 <= edad < 30)), Comida(proteinas=P(lambda proteinas: proteinas >= 15)))
    def joven_alta_proteinas(self):
        self.declare(Fact(puntaje=15))

    @Rule(Usuario(edad=P(lambda edad: 30 <= edad <= 50)), Comida(calorias=P(lambda calorias: calorias <= 400)))
    def adulto_baja_calorias(self):
        self.declare(Fact(puntaje=20))

    @Rule(Usuario(edad=P(lambda edad: 51 <= edad <= 65)), Comida(proteinas=P(lambda proteinas: proteinas >= 20)))
    def mayor_alta_proteinas(self):
        self.declare(Fact(puntaje=30))

    @Rule(Usuario(edad=P(lambda edad: 51 <= edad <= 65)), Comida(calorias=P(lambda calorias: calorias <= 350)))
    def mayor_baja_calorias(self):
        self.declare(Fact(puntaje=20))

    @Rule(Usuario(edad=P(lambda edad: edad > 65)), Comida(proteinas=P(lambda proteinas: proteinas >= 20)))
    def anciano_alta_proteinas(self):
        self.declare(Fact(puntaje=35))

    @Rule(Usuario(edad=P(lambda edad: edad > 65)), Comida(calorias=P(lambda calorias: calorias <= 300)))
    def anciano_baja_calorias(self):
        self.declare(Fact(puntaje=25))

    # 5. Reglas para condiciones médicas
    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(carbohidratos=P(lambda carbohidratos: carbohidratos <= 20)))
    def diabetes_baja_carbohidratos(self, condiciones):
        if "diabetes" in condiciones:
            self.declare(Fact(puntaje=30))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(categorias=MATCH.categorias))
    def celiacos_sin_gluten(self, condiciones, categorias):
        if "enfermedad celíaca" in condiciones and "sin gluten" in categorias:
            self.declare(Fact(puntaje=35))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(sodio=P(lambda sodio: sodio <= 100)))
    def hipertension_bajo_sodio(self, condiciones):
        if "hipertension" in condiciones:
            self.declare(Fact(puntaje=25))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(calorias=P(lambda calorias: calorias > 400)))
    def eliminar_comida_por_condiciones(self, condiciones):
        # Ejemplo: Elimina comidas con más de 400 calorías para usuarios con ciertas condiciones
        if any(cond in condiciones for cond in ["obesidad", "insuficiencia renal"]):
            self.declare(Fact(invalid=True))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(grasas=P(lambda grasas: grasas <= 10)))
    def colesterol_alto_baja_grasas(self, condiciones):
        if "colesterol alto" in condiciones:
            self.declare(Fact(puntaje=30))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(nutrientes=MATCH.nutrientes))
    def anemia_alto_hierro(self, condiciones, nutrientes):
        if "anemia" in condiciones and "hierro" in nutrientes:
            self.declare(Fact(puntaje=35))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(yodo=P(lambda yodo: yodo >= 30)))
    def hipotiroidismo_alto_yodo(self, condiciones):
        if "hipotiroidismo" in condiciones:
            self.declare(Fact(puntaje=25))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(categorias=MATCH.categorias))
    def intolerancia_lactosa_sin_lactosa(self, condiciones, categorias):
        if "intolerancia a la lactosa" in condiciones and "sin lactosa" in categorias:
            self.declare(Fact(puntaje=30))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(proteinas=P(lambda proteinas: proteinas <= 15)))
    def insuficiencia_renal_baja_proteinas(self, condiciones):
        if "insuficiencia renal" in condiciones:
            self.declare(Fact(puntaje=30))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(categorias=MATCH.categorias))
    def alergia_frutos_secos_sin_frutos_secos(self, condiciones, categorias):
        if "alergia a los frutos secos" in condiciones and "sin frutos secos" in categorias:
            self.declare(Fact(puntaje=35))

    @Rule(Usuario(condiciones_medicas=MATCH.condiciones), Comida(calorias=P(lambda calorias: calorias <= 300)))
    def obesidad_baja_calorias(self, condiciones):
        if "obesidad" in condiciones:
            self.declare(Fact(puntaje=30))


    # 6. Reglas para preferencias alimenticias
    @Rule(Usuario(preferencias=MATCH.preferencias), Comida(categorias=MATCH.categorias))
    def preferencias_alimenticias(self, preferencias, categorias):
        if any(pref in categorias for pref in preferencias):
            self.declare(Fact(puntaje=20))