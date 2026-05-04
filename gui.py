import customtkinter as ctk

class GUICalculador:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Calculador Académico")
        self.root.geometry("500x620")
        self.main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def limpiar(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def mostrar_inicio(self, callback_materia, callback_promedio, callback_config_beca):
        self.limpiar()
        ctk.CTkLabel(self.main_frame, text="Calculador de Notas", font=("Arial", 24, "bold")).pack(pady=20)
        ctk.CTkButton(self.main_frame, text="Calcular Materia", command=callback_materia, width=220, height=45).pack(pady=10)
        ctk.CTkButton(self.main_frame, text="Resumen y Beca", command=callback_promedio, width=220, height=45).pack(pady=10)
        ctk.CTkButton(self.main_frame, text="Configurar Beca", fg_color="#555555", command=callback_config_beca, width=220, height=45).pack(pady=10)

    def mostrar_seleccion_materia(self, lista_materias, callback_seleccion, callback_volver):
        self.limpiar()
        ctk.CTkLabel(self.main_frame, text="Selecciona tu materia", font=("Arial", 18)).pack(pady=20)
        self.menu = ctk.CTkOptionMenu(self.main_frame, values=lista_materias + ["+ Otra"], command=callback_seleccion)
        self.menu.pack(pady=10)
        self.menu.set("Seleccionar...")
        ctk.CTkButton(self.main_frame, text="Volver al Inicio", fg_color="gray", command=callback_volver).pack(pady=20)

    def pantalla_calculo(self, nombre_materia, callback_calcular, callback_volver):
        self.limpiar()
        ctk.CTkLabel(self.main_frame, text=f"Materia: {nombre_materia}", font=("Arial", 20, "bold")).pack(pady=10)
        self.ent_p1 = ctk.CTkEntry(self.main_frame, placeholder_text="Nota 1° Parcial (0-10)", width=200)
        self.ent_p1.pack(pady=5)
        self.ent_p2 = ctk.CTkEntry(self.main_frame, placeholder_text="Nota 2° Parcial (0-10)", width=200)
        self.ent_p2.pack(pady=5)
        self.btn_calc = ctk.CTkButton(self.main_frame, text="Calcular Situación", command=callback_calcular)
        self.btn_calc.pack(pady=20)
        self.lbl_res = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 15), wraplength=400)
        self.lbl_res.pack(pady=10)
        self.btn_volver = ctk.CTkButton(self.main_frame, text="Regresar", fg_color="#333333", command=callback_volver)
        self.btn_volver.pack(side="bottom", pady=20)

    def pantalla_registro_materia(self, callback_guardar, callback_volver):
        self.limpiar()
        ctk.CTkLabel(self.main_frame, text="Nueva Materia", font=("Arial", 20, "bold")).pack(pady=20)
        self.ent_nombre_m = ctk.CTkEntry(self.main_frame, placeholder_text="Nombre (ej. Física)", width=250)
        self.ent_nombre_m.pack(pady=10)
        self.ent_minima = ctk.CTkEntry(self.main_frame, placeholder_text="Mínima aprobatoria (ej. 7.0)", width=250)
        self.ent_minima.pack(pady=10)
        ctk.CTkButton(self.main_frame, text="Guardar Materia", command=callback_guardar).pack(pady=20)
        ctk.CTkButton(self.main_frame, text="Volver", fg_color="gray", command=callback_volver).pack(pady=5)

    def pantalla_configurar_beca(self, callback_guardar, callback_volver):
        self.limpiar()
        ctk.CTkLabel(self.main_frame, text="¿Tienes Beca?", font=("Arial", 20, "bold")).pack(pady=20)
        ctk.CTkLabel(self.main_frame, text="Ingresa el promedio que te piden:", font=("Arial", 14)).pack(pady=5)
        self.ent_prom_beca = ctk.CTkEntry(self.main_frame, placeholder_text="Ej. 8.5", width=200)
        self.ent_prom_beca.pack(pady=10)
        ctk.CTkButton(self.main_frame, text="Establecer Beca", command=callback_guardar).pack(pady=20)
        ctk.CTkButton(self.main_frame, text="Cancelar", fg_color="gray", command=callback_volver).pack(pady=5)

    def mostrar_promedio_general(self, lista_materias, promedio, estado_beca, callback_agregar, callback_volver):
        self.limpiar()
        ctk.CTkLabel(self.main_frame, text="Resumen General", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self.main_frame, text=f"Promedio Actual: {round(promedio, 2)}", font=("Arial", 18)).pack(pady=10)
        color_beca = "green" if "SEGURA" in estado_beca else "orange" if "RIESGO" in estado_beca else "red"
        ctk.CTkLabel(self.main_frame, text=f"Beca: {estado_beca}", text_color=color_beca, font=("Arial", 16, "bold")).pack(pady=5)
        ctk.CTkLabel(self.main_frame, text="Materias registradas:", font=("Arial", 14, "underline")).pack(pady=10)
        for materia in lista_materias:
            ctk.CTkLabel(self.main_frame, text=f"• {materia}").pack()
        ctk.CTkButton(self.main_frame, text="Agregar más materias", command=callback_agregar).pack(pady=20)
        ctk.CTkButton(self.main_frame, text="Volver al Inicio", fg_color="#555555", command=callback_volver).pack(pady=5)