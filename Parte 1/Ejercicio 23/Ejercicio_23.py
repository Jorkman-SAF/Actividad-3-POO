import tkinter as tk
import math

class CalculadoraEcuacionSegundoGrado:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Ecuación de Segundo Grado")

        # Etiqueta y entrada para el valor de A
        self.lbl_a = tk.Label(self.ventana, text="Valor de A:")
        self.lbl_a.pack()
        self.entry_a = tk.Entry(self.ventana)
        self.entry_a.pack()

        # Etiqueta y entrada para el valor de B
        self.lbl_b = tk.Label(self.ventana, text="Valor de B:")
        self.lbl_b.pack()
        self.entry_b = tk.Entry(self.ventana)
        self.entry_b.pack()

        # Etiqueta y entrada para el valor de C
        self.lbl_c = tk.Label(self.ventana, text="Valor de C:")
        self.lbl_c.pack()
        self.entry_c = tk.Entry(self.ventana)
        self.entry_c.pack()

        # Botón para calcular
        self.btn_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.btn_calcular.pack()

        # Etiqueta para mostrar el resultado
        self.lbl_resultado = tk.Label(self.ventana, text="")
        self.lbl_resultado.pack()

    def calcular(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        # Calcular el discriminante
        discriminante = b ** 2 - 4 * a * c

        # Verificar si la ecuación tiene soluciones reales
        if discriminante > 0:
            # Calcular las soluciones
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            resultado = f"Soluciones:\n x1 = {x1:.2f}\n x2 = {x2:.2f}"
        elif discriminante < 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            resultado = f"Soluciones:\n x1 = {x1:.2f}\n x2 = {x2:.2f}"
        
            
        else:
            resultado = "La ecuación no tiene soluciones reales"

        self.lbl_resultado.config(text=resultado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraEcuacionSegundoGrado(ventana)
    ventana.mainloop()
