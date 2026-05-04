# main.py
from modelo import Alumno
from gui import GUICalculador
from controlador import ControladorCalculador

# 1. Iniciamos al alumno solo con su nombre
estudiante = Alumno("")

interfaz = GUICalculador()
app = ControladorCalculador(estudiante, interfaz)

if __name__ == "__main__":
    app.run()