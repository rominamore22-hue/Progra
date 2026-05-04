# 🎓 GradeLab – Asistente Académico Inteligente

## Descripción General

Este proyecto implementa una aplicación académica inteligente desarrollada con Programación Orientada a Objetos (POO) en Python y una interfaz gráfica utilizando CustomTkinter.

GradeLab ayuda a estudiantes universitarios a tomar mejores decisiones sobre sus materias y su beca académica.

No es solo una calculadora de calificaciones: analiza si conviene continuar en una materia, si es mejor darla de baja, cuánto se necesita para aprobar y cómo esto afecta el promedio general y la conservación de la beca.

---

## Funcionalidades

* Registro de materias
* Registro de evaluaciones y parciales
* Cálculo de promedio por materia
* Simulación de escenarios académicos
* Análisis de riesgo académico
* Recomendación de continuar o dar de baja una materia
* Cálculo de promedio general
* Evaluación del estado de beca
* Interfaz gráfica con flujo de pantallas

---

## Flujo del Sistema

1. Registrar o seleccionar una materia
2. Ingresar calificaciones parciales
3. Calcular promedio actual
4. Analizar si es posible aprobar
5. Obtener recomendación académica
6. Revisar promedio general
7. Evaluar el estado de la beca

---

## Ejemplo de Resultado

```python
Promedio: 42.0
Rango: (42.0, 72.0)
Análisis: RIESGO: Se requiere mejorar
Beca: BECA EN PELIGRO
```

(Este resultado puede variar según las calificaciones ingresadas.)

---

## Conceptos Aplicados

* Programación Orientada a Objetos (POO)
* Clases y Objetos
* Encapsulamiento
* Herencia aplicada en GUI
* Lógica de negocio
* Simulación de escenarios
* Interfaz gráfica con CustomTkinter
* Separación Modelo – Controlador – Vista

---

## Estructura Principal

### Clases del sistema

* Alumno
* Materia
* Evaluacion
* Calculadora
* Simulador
* Analizador
* Beca
* GUIGradeLab
* ControladorCalculador

---

## ¿Por qué este proyecto es importante?

Muchos estudiantes no saben si aún pueden aprobar una materia o si conviene darla de baja antes de afectar su promedio general y perder una beca.

GradeLab busca resolver este problema proporcionando información clara y simulaciones académicas que permitan tomar decisiones más inteligentes y a tiempo.

Representa una aplicación real de la programación orientada a objetos para resolver una problemática universitaria cotidiana.

---

## Tecnologías Utilizadas

* Python 3
* CustomTkinter
* Programación Orientada a Objetos (POO)

---

## Requisitos

```bash
pip install customtkinter
```

---
## Archivos

- main.py → archivo principal
- gui.py → interfaz
- modelo.py → lógica
- controlador.py → conexión entre componentes
