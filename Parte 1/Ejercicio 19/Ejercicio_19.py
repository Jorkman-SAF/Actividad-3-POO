import tkinter as tk
import math

class TrianguloEquilateroCalculator:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Triángulo Equilátero")

        # Etiqueta y entrada para el lado del triángulo
        self.lbl_lado = tk.Label(self.ventana, text="Ingrese el valor del lado:")
        self.lbl_lado.pack()
        self.entry_lado = tk.Entry(self.ventana)
        self.entry_lado.pack()

        # Botón para calcular
        self.btn_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.btn_calcular.pack()

        # Etiquetas para mostrar el resultado
        self.lbl_perimetro = tk.Label(self.ventana, text="")
        self.lbl_perimetro.pack()
        self.lbl_altura = tk.Label(self.ventana, text="")
        self.lbl_altura.pack()
        self.lbl_area = tk.Label(self.ventana, text="")
        self.lbl_area.pack()

    def calcular(self):
        lado = float(self.entry_lado.get())

        # Calcular el perímetro
        perimetro = 3 * lado
        self.lbl_perimetro.config(text=f"Perímetro: {perimetro}")

        # Calcular la altura
        altura = (math.sqrt(3) / 2) * lado
        self.lbl_altura.config(text=f"Altura: {altura}")

        # Calcular el área
        area = (math.sqrt(3) / 4) * lado**2
        self.lbl_area.config(text=f"Área: {area}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = TrianguloEquilateroCalculator(ventana)
    ventana.mainloop()
