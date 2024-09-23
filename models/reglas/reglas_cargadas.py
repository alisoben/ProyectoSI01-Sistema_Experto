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
        coincidencias = sum(1 for pref in preferencias if pref in categorias)  # Cuenta las coincidencias
        if coincidencias > 0:
            self.declare(Fact(puntaje=20 * coincidencias))  # Suma 20 puntos por cada coincidencia

    # 7. Reglas basadas en el objetivo: Perder peso
    # Calorias
    @Rule(Usuario(objetivo="Perder peso"), Comida(calorias=P(lambda calorias: calorias < 200)))
    def calorias_muy_bajas_perder_peso(self):
        self.declare(Fact(puntaje=50))  # Comidas con muy pocas calorías son muy recomendadas para perder peso

    @Rule(Usuario(objetivo="Perder peso"), Comida(calorias=P(lambda calorias: 200 <= calorias < 300)))
    def calorias_bajas_perder_peso(self):
        self.declare(Fact(puntaje=40))  # Comidas con calorías bajas siguen siendo buenas para perder peso

    @Rule(Usuario(objetivo="Perder peso"), Comida(calorias=P(lambda calorias: 300 <= calorias < 400)))
    def calorias_moderadas_perder_peso(self):
        self.declare(Fact(puntaje=20))  # Las comidas moderadas en calorías se pueden permitir ocasionalmente

    @Rule(Usuario(objetivo="Perder peso"), Comida(calorias=P(lambda calorias: calorias >= 400)))
    def calorias_altas_perder_peso(self):
        self.declare(Fact(puntaje=-20))  # Penalización por comidas con demasiadas calorías para perder peso
    
    # Proteinas
    @Rule(Usuario(objetivo="Perder peso"), Comida(proteinas=P(lambda proteinas: proteinas >= 20)))
    def alta_proteina_perder_peso(self):
        self.declare(Fact(puntaje=40))  # Las comidas altas en proteínas ayudan a mantener la masa muscular

    @Rule(Usuario(objetivo="Perder peso"), Comida(proteinas=P(lambda proteinas: 10 <= proteinas < 20)))
    def moderada_proteina_perder_peso(self):
        self.declare(Fact(puntaje=20))  # Una cantidad moderada de proteínas sigue siendo buena para perder peso

    @Rule(Usuario(objetivo="Perder peso"), Comida(proteinas=P(lambda proteinas: proteinas < 10)))
    def baja_proteina_perder_peso(self):
        self.declare(Fact(puntaje=5))  # Comidas bajas en proteínas no son las mejores para perder peso

    # Carbohidratos
    @Rule(Usuario(objetivo="Perder peso"), Comida(carbohidratos=P(lambda carbohidratos: carbohidratos <= 20)))
    def bajos_carbohidratos_perder_peso(self):
        self.declare(Fact(puntaje=35))  # Control de carbohidratos es clave para perder peso

    @Rule(Usuario(objetivo="Perder peso"), Comida(carbohidratos=P(lambda carbohidratos: 20 < carbohidratos <= 40)))
    def moderados_carbohidratos_perder_peso(self):
        self.declare(Fact(puntaje=20))  # Carbohidratos moderados pueden estar bien para ciertos usuarios

    @Rule(Usuario(objetivo="Perder peso"), Comida(carbohidratos=P(lambda carbohidratos: carbohidratos > 40)))
    def altos_carbohidratos_perder_peso(self):
        self.declare(Fact(puntaje=-10))  # Penalización por demasiados carbohidratos

    # Sodio
    @Rule(Usuario(objetivo="Perder peso"), Comida(sodio=P(lambda sodio: sodio <= 100)))
    def bajo_sodio_perder_peso(self):
        self.declare(Fact(puntaje=30))  # Control de sodio es importante para evitar la retención de líquidos

    @Rule(Usuario(objetivo="Perder peso"), Comida(sodio=P(lambda sodio: 100 < sodio <= 200)))
    def moderado_sodio_perder_peso(self):
        self.declare(Fact(puntaje=10))  # Moderado nivel de sodio es aceptable

    @Rule(Usuario(objetivo="Perder peso"), Comida(sodio=P(lambda sodio: sodio > 200)))
    def alto_sodio_perder_peso(self):
        self.declare(Fact(puntaje=-15))  # Penalización por comidas con mucho sodio

    # 8. Reglas basadas en el objetivo: Mantener peso
    # Calorias
    @Rule(Usuario(objetivo="Mantener peso"), Comida(calorias=P(lambda calorias: 300 <= calorias <= 400)))
    def calorias_equilibradas_mantener_peso(self):
        self.declare(Fact(puntaje=40))  # Buen equilibrio de calorías para mantener el peso

    @Rule(Usuario(objetivo="Mantener peso"), Comida(calorias=P(lambda calorias: 200 <= calorias < 300)))
    def calorias_bajas_mantener_peso(self):
        self.declare(Fact(puntaje=30))  # Comidas bajas en calorías aún pueden ser buenas para mantener el peso

    @Rule(Usuario(objetivo="Mantener peso"), Comida(calorias=P(lambda calorias: calorias < 200)))
    def calorias_muy_bajas_mantener_peso(self):
        self.declare(Fact(puntaje=10))  # Demasiado pocas calorías podrían no ser ideales

    @Rule(Usuario(objetivo="Mantener peso"), Comida(calorias=P(lambda calorias: calorias > 400)))
    def calorias_altas_mantener_peso(self):
        self.declare(Fact(puntaje=-10))  # Penalización por calorías altas que podrían llevar a aumento de peso

    # Proteinas
    @Rule(Usuario(objetivo="Mantener peso"), Comida(proteinas=P(lambda proteinas: 15 <= proteinas < 20)))
    def moderada_proteina_mantener_peso(self):
        self.declare(Fact(puntaje=20))  # Cantidad moderada de proteínas es adecuada para mantener el peso

    @Rule(Usuario(objetivo="Mantener peso"), Comida(proteinas=P(lambda proteinas: proteinas < 15)))
    def baja_proteina_mantener_peso(self):
        self.declare(Fact(puntaje=10))  # Proteínas bajas son aceptables pero no ideales para mantener el peso

    # Carbohidratos
    @Rule(Usuario(objetivo="Mantener peso"), Comida(carbohidratos=P(lambda carbohidratos: 30 <= carbohidratos <= 50)))
    def moderados_carbohidratos_mantener_peso(self):
        self.declare(Fact(puntaje=30))  # Un equilibrio moderado de carbohidratos es clave para mantener el peso

    @Rule(Usuario(objetivo="Mantener peso"), Comida(carbohidratos=P(lambda carbohidratos: carbohidratos < 30)))
    def bajos_carbohidratos_mantener_peso(self):
        self.declare(Fact(puntaje=10))  # Carbohidratos bajos también funcionan

    # 9. Reglas basadas en el objetivo: Ganar músculo
    # Calorias
    @Rule(Usuario(objetivo="Ganar músculo"), Comida(calorias=P(lambda calorias: calorias >= 500)))
    def alta_calorias_ganar_musculo(self):
        self.declare(Fact(puntaje=50))  # Se necesita un consumo alto de calorías para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(calorias=P(lambda calorias: 400 <= calorias < 500)))
    def moderada_calorias_ganar_musculo(self):
        self.declare(Fact(puntaje=30))  # Una cantidad moderada de calorías también es aceptable para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(calorias=P(lambda calorias: 300 <= calorias < 400)))
    def baja_calorias_ganar_musculo(self):
        self.declare(Fact(puntaje=10))  # Comidas con pocas calorías no son ideales para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(calorias=P(lambda calorias: calorias < 300)))
    def muy_baja_calorias_ganar_musculo(self):
        self.declare(Fact(puntaje=-20))  # Penalización por comidas con muy pocas calorías, no ayudan a ganar músculo

    # Proteinas
    @Rule(Usuario(objetivo="Ganar músculo"), Comida(proteinas=P(lambda proteinas: proteinas >= 25)))
    def alta_proteina_ganar_musculo(self):
        self.declare(Fact(puntaje=50))  # Las comidas muy altas en proteínas son esenciales para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(proteinas=P(lambda proteinas: 20 <= proteinas < 25)))
    def moderada_proteina_ganar_musculo(self):
        self.declare(Fact(puntaje=30))  # Una cantidad moderada de proteínas sigue siendo buena para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(proteinas=P(lambda proteinas: 15 <= proteinas < 20)))
    def baja_proteina_ganar_musculo(self):
        self.declare(Fact(puntaje=10))  # Proteínas bajas no son ideales para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(proteinas=P(lambda proteinas: proteinas < 15)))
    def muy_baja_proteina_ganar_musculo(self):
        self.declare(Fact(puntaje=-10))  # Penalización por proteínas insuficientes para ganar músculo

    # Carbohidratos
    @Rule(Usuario(objetivo="Ganar músculo"), Comida(carbohidratos=P(lambda carbohidratos: 40 <= carbohidratos < 60)))
    def moderado_carbohidratos_ganar_musculo(self):
        self.declare(Fact(puntaje=30))  # Una cantidad moderada de carbohidratos ayuda en el proceso de ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(carbohidratos=P(lambda carbohidratos: 60 <= carbohidratos < 80)))
    def alto_carbohidratos_ganar_musculo(self):
        self.declare(Fact(puntaje=40))  # Una cantidad alta de carbohidratos apoya el crecimiento muscular

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(carbohidratos=P(lambda carbohidratos: carbohidratos >= 80)))
    def muy_alto_carbohidratos_ganar_musculo(self):
        self.declare(Fact(puntaje=50))  # Una cantidad muy alta de carbohidratos es ideal para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(carbohidratos=P(lambda carbohidratos: carbohidratos < 40)))
    def bajo_carbohidratos_ganar_musculo(self):
        self.declare(Fact(puntaje=10))  # Comidas bajas en carbohidratos no son óptimas para ganar músculo

    # Sodio
    @Rule(Usuario(objetivo="Ganar músculo"), Comida(sodio=P(lambda sodio: sodio <= 100)))
    def bajo_sodio_ganar_musculo(self):
        self.declare(Fact(puntaje=30))  # Es bueno mantener el sodio bajo mientras se gana músculo para evitar retención

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(sodio=P(lambda sodio: 100 < sodio <= 200)))
    def moderado_sodio_ganar_musculo(self):
        self.declare(Fact(puntaje=10))  # Moderado nivel de sodio es aceptable para ganar músculo

    @Rule(Usuario(objetivo="Ganar músculo"), Comida(sodio=P(lambda sodio: sodio > 200)))
    def alto_sodio_ganar_musculo(self):
        self.declare(Fact(puntaje=-20))  # Penalización por comidas con alto contenido de sodio, no ideal para ganar músculo