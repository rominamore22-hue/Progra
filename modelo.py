class Evaluacion:
    def __init__(self, nombre: str, porcentaje: float, tipo: str):
        self.nombre = nombre
        self.porcentaje = porcentaje
        self.calificacion = None
        self.tipo = tipo  

class Materia:
    def __init__(self, nombre: str, calificacion_minima: float):
        self.nombre = nombre
        self.calificacion_minima = calificacion_minima  
        self.evaluaciones = []
        self.estado = "ACTIVA"  

    def agregar_evaluacion(self, evaluacion: Evaluacion):
        self.evaluaciones.append(evaluacion)

class Alumno: 
    def __init__(self, nombre: str, beca=None):
        self.nombre = nombre
        self.materias = []
        self.beca = beca 
        
    def agregar_materia(self, materia):
        self.materias.append(materia)
    
    def obtener_materia(self, nombre_materia):
        for materia in self.materias:
            if materia.nombre == nombre_materia:
                return materia
        return None

    def calcular_promedio_general(self):
        total = 0
        cantidad_materias_con_nota = 0
        for materia in self.materias:
            promedio_m = Calculadora.calcular_promedio_materia(materia)
            if promedio_m > 0:
                total += promedio_m
                cantidad_materias_con_nota += 1
        return total / cantidad_materias_con_nota if cantidad_materias_con_nota > 0 else 0

    def evaluar_beca(self):
        if self.beca is None:
            return "Sin beca"
        return self.beca.evaluar_estado(self)

class Calculadora:
    @staticmethod
    def calcular_promedio_materia(materia):
        total_puntos = 0
        porcentaje_evaluado = 0
        for evaluacion in materia.evaluaciones:
            if evaluacion.calificacion is not None:
                total_puntos += evaluacion.calificacion * (evaluacion.porcentaje / 100)
                porcentaje_evaluado += evaluacion.porcentaje
        if porcentaje_evaluado == 0:
            return 0
        return (total_puntos / porcentaje_evaluado) * 100

class Analizador:
    @staticmethod
    def obtener_diagnostico_final(materia):
        puntos_actuales = Calculadora.calcular_promedio_materia(materia)
        necesario_str = Analizador.calcular_necesario_para_aprobar(materia)
        if "CRÍTICO" in necesario_str:
            return "❌ ESTADO CRÍTICO: Ya no es posible aprobar. Se recomienda dar de baja."
        if puntos_actuales >= materia.calificacion_minima:
            return f"✅ ¡MATERIA APROBADA! Tienes {round(puntos_actuales, 2)}."
        try:
            valor_necesario = float(necesario_str.split("obtener ")[1].split(" en")[0])
            if valor_necesario <= 5.0:
                return f"✅ ¡CASI SALVADA! {necesario_str}."
        except:
            pass
        return f"⚠️ {necesario_str}."

    @staticmethod
    def calcular_necesario_para_aprobar(materia):
        total_acumulado = 0
        porcentaje_evaluado = 0
        for ev in materia.evaluaciones:
            if ev.calificacion is not None:
                total_acumulado += ev.calificacion * (ev.porcentaje / 100)
                porcentaje_evaluado += ev.porcentaje
        
        puntos_faltantes = materia.calificacion_minima - total_acumulado
        porcentaje_restante = 100 - porcentaje_evaluado
        
        if porcentaje_restante <= 0:
            return "Evaluaciones completas"
        
        nota_necesaria = (puntos_faltantes / porcentaje_restante) * 100
        if nota_necesaria > 10.0: # Escala 0-10
            return "CRÍTICO"
        if nota_necesaria < 0:
            return "Ya aprobaste"
        return f"Necesitas obtener {round(nota_necesaria, 2)} en lo que falta"

class Beca:
    def __init__(self, promedio_minimo):
        self.promedio_minimo = promedio_minimo
    def evaluar_estado(self, alumno):
        promedio = alumno.calcular_promedio_general()
        if promedio >= self.promedio_minimo:
            return "BECA SEGURA"
        if promedio >= self.promedio_minimo - 1:
            return "RIESGO DE PERDER BECA"
        return "BECA EN PELIGRO"