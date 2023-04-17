import tkinter as tk
from math import sqrt

class CalculadoraNumericaGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora Numérica")

        # Lista para almacenar los números ingresados
        self.numeros = []

        # Etiqueta y entrada para el valor de entrada
        self.lbl_valor = tk.Label(self.ventana, text="Ingrese un número entero positivo:")
        self.lbl_valor.pack()
        self.entry_valor = tk.Entry(self.ventana)
        self.entry_valor.pack()

        # Botón para agregar el valor ingresado
        self.btn_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_numero)
        self.btn_agregar.pack()

        # Canvas para mostrar los resultados
        self.canvas = tk.Canvas(self.ventana, width=750, height=400)
        self.canvas.pack()

        # Botón para calcular la raíz cuadrada, el cuadrado y el cubo
        self.btn_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular_resultados)
        self.btn_calcular.pack()

    def agregar_numero(self):
        valor = self.entry_valor.get()
        if valor.isdigit() and int(valor) > 0:
            self.numeros.append(int(valor))
            self.actualizar_canvas()

    def calcular_resultados(self):
        self.actualizar_canvas()
        if self.numeros:
            self.canvas.create_text(400, 150, text="Resultados:", font=("Arial", 14))
            for i, numero in enumerate(self.numeros):
                x = 50
                y = 200 + i * 30
                self.canvas.create_text(x, y, text=f"Número: {numero}", font=("Arial", 12))
                self.canvas.create_text(x + 200, y, text=f"Raíz cuadrada: {sqrt(numero):.2f}", font=("Arial", 12))
                self.canvas.create_text(x + 400, y, text=f"Cuadrado: {numero ** 2}", font=("Arial", 12))
                self.canvas.create_text(x + 600, y, text=f"Cubo: {numero ** 3}", font=("Arial", 12))
        else:
            self.canvas.create_text(200, 150, text="No se ha ingresado ningún número", font=("Arial", 12))

    def actualizar_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraNumericaGUI(ventana)
    ventana.mainloop()
