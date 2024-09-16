from experta import Fact, KnowledgeEngine, Rule, AND, OR, P

class Usuario(Fact):
    """Hecho que representa a un usuario."""
    pass

class Comida(Fact):
    """Hecho que representa una comida."""
    pass

class MotorRecomendacion(KnowledgeEngine):

    @Rule(AND(Usuario(imc=P(lambda imc: imc >= 25)), Comida(calorias=P(lambda cal: cal <= 300))))
    def regla_imc_sobrepeso(self):
        self.declare(Fact(puntaje=25))  # Comidas bajas en calorías para personas con sobrepeso

    @Rule(AND(Usuario(imc=P(lambda imc: imc < 18.5)), Comida(calorias=P(lambda cal: cal >= 400))))
    def regla_imc_bajo_peso(self):
        self.declare(Fact(puntaje=15))  # Personas con bajo peso necesitan más calorías

    # Reglas basadas en el género
    @Rule(AND(Usuario(genero="M"), Comida(calorias=P(lambda cal: cal >= 500))))
    def regla_genero_masculino(self):
        self.declare(Fact(puntaje=10))  # Hombres tienden a necesitar más calorías

    @Rule(AND(Usuario(genero="F"), Comida(calorias=P(lambda cal: cal <= 500))))
    def regla_genero_femenino(self):
        self.declare(Fact(puntaje=10))  # Control de calorías más común en mujeres

    @Rule(AND(Usuario(genero="F"), Comida(proteinas=P(lambda prot: prot >= 15))))
    def regla_genero_femenino_proteinas(self):
        self.declare(Fact(puntaje=15))  # Aumentar proteínas es importante para las mujeres

    # Reglas para la actividad física
    @Rule(AND(Usuario(actividad_fisica="alto"), Comida(proteinas=P(lambda prot: prot >= 20))))
    def regla_alta_actividad_fisica(self):
        self.declare(Fact(puntaje=30))  # Alta proteína para actividades físicas intensas

    @Rule(AND(Usuario(actividad_fisica="moderado"), Comida(proteinas=P(lambda prot: prot >= 15))))
    def regla_moderada_actividad_fisica(self):
        self.declare(Fact(puntaje=20))  # Moderado nivel de actividad, requiere proteína pero menos

    @Rule(AND(Usuario(actividad_fisica="baja"), Comida(calorias=P(lambda cal: cal <= 300))))
    def regla_baja_actividad_fisica(self):
        self.declare(Fact(puntaje=25))  # Personas con actividad baja deben controlar más las calorías

    # Reglas para la edad
    @Rule(AND(Usuario(edad=P(lambda edad: edad < 18)), Comida(calorias=P(lambda cal: cal >= 600))))
    def regla_edad_adolescente_calorias(self):
        self.declare(Fact(puntaje=10))  # Los adolescentes requieren más calorías

    @Rule(AND(Usuario(edad=P(lambda edad: 18 <= edad < 30)), Comida(calorias=P(lambda cal: cal >= 500))))
    def regla_edad_joven_calorias(self):
        self.declare(Fact(puntaje=10))  # Los jóvenes pueden requerir más calorías

    @Rule(AND(Usuario(edad=P(lambda edad: 30 <= edad <= 50)), Comida(calorias=P(lambda cal: cal <= 400))))
    def regla_edad_adulto_calorias(self):
        self.declare(Fact(puntaje=20))  # Control de calorías recomendado para adultos

    @Rule(AND(Usuario(edad=P(lambda edad: edad > 65)), Comida(proteinas=P(lambda prot: prot >= 20))))
    def regla_edad_mayor_proteinas(self):
        self.declare(Fact(puntaje=35))  # Mayor énfasis en proteínas para personas mayores

    # Reglas para condiciones médicas
    @Rule(AND(Usuario(condiciones_medicas=P(lambda cond: "diabetes" in cond)), Comida(carbohidratos=P(lambda carb: carb <= 20))))
    def regla_diabetes(self):
        self.declare(Fact(puntaje=30))  # Control estricto de carbohidratos es vital para la diabetes

    @Rule(AND(Usuario(condiciones_medicas=P(lambda cond: "hipertension" in cond)), Comida(sodio=P(lambda sod: sod <= 100))))
    def regla_hipertension(self):
        self.declare(Fact(puntaje=25))  # Control del sodio es clave para la hipertensión

    @Rule(AND(Usuario(condiciones_medicas=P(lambda cond: "anemia" in cond)), Comida(nutrientes=P(lambda nut: "hierro" in nut))))
    def regla_anemia(self):
        self.declare(Fact(puntaje=35))  # El hierro es vital para personas con anemia

    # Reglas para preferencias alimenticias
    @Rule(AND(Usuario(preferencias=P(lambda prefs: any(pref in prefs for pref in ["sin gluten", "vegetariano"]))), Comida(categorias=P(lambda cat: "sin gluten" in cat))))
    def regla_preferencias_alimenticias(self):
        self.declare(Fact(puntaje=20))  # Preferencias alimenticias del usuario

    # Puedes seguir añadiendo más reglas según las necesidades del sistema
