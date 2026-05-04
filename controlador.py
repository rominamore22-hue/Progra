from modelo import Materia, Evaluacion, Beca, Analizador

class ControladorCalculador:
    def __init__(self, alumno, gui):
        self.alumno = alumno
        self.gui = gui
        self.ir_a_inicio()

    def ir_a_inicio(self):
        self.gui.mostrar_inicio(self.ir_a_seleccion, self.ir_a_promedio, self.ir_a_config_beca)

    def ir_a_seleccion(self):
        nombres = [m.nombre for m in self.alumno.materias]
        self.gui.mostrar_seleccion_materia(nombres, self.gestionar_menu, self.ir_a_inicio)

    def gestionar_menu(self, eleccion):
        if eleccion == "+ Otra":
            self.ir_a_registrar()
        else:
            self.gui.pantalla_calculo(eleccion, lambda: self.ejecutar_calculo(eleccion), self.ir_a_seleccion)

    def ejecutar_calculo(self, nombre_materia):
        materia = self.alumno.obtener_materia(nombre_materia)
        try:
            n1 = float(self.gui.ent_p1.get())
            n2 = float(self.gui.ent_p2.get())
            materia.evaluaciones[0].calificacion = n1
            materia.evaluaciones[1].calificacion = n2
            resultado = Analizador.obtener_diagnostico_final(materia)
            color = "red" if "❌" in resultado else "green" if "✅" in resultado else "orange"
            self.gui.lbl_res.configure(text=resultado, text_color=color)
        except ValueError:
            self.gui.lbl_res.configure(text="⚠️ Ingresa números válidos", text_color="red")

    def ir_a_promedio(self):
        nombres_m = [m.nombre for m in self.alumno.materias]
        prom = self.alumno.calcular_promedio_general()
        beca_status = self.alumno.evaluar_beca()
        self.gui.mostrar_promedio_general(nombres_m, prom, beca_status, self.ir_a_registrar, self.ir_a_inicio)

    def ir_a_registrar(self):
        self.gui.pantalla_registro_materia(self.guardar_nueva_materia, self.ir_a_inicio)

    def guardar_nueva_materia(self):
        nombre = self.gui.ent_nombre_m.get()
        try:
            minima = float(self.gui.ent_minima.get())
            nueva = Materia(nombre, minima)
            nueva.agregar_evaluacion(Evaluacion("1° Parcial", 30, "NORMAL"))
            nueva.agregar_evaluacion(Evaluacion("2° Parcial", 30, "NORMAL"))
            nueva.agregar_evaluacion(Evaluacion("3° Parcial", 40, "FINAL"))
            self.alumno.agregar_materia(nueva)
            self.ir_a_seleccion()
        except:
            print("Error: Datos inválidos")

    def ir_a_config_beca(self):
        self.gui.pantalla_configurar_beca(self.establecer_beca, self.ir_a_inicio)

    def establecer_beca(self):
        try:
            prom_req = float(self.gui.ent_prom_beca.get())
            self.alumno.beca = Beca(prom_req)
            self.ir_a_inicio()
        except:
            print("Error: Promedio inválido")

    def run(self):
        self.gui.root.mainloop()