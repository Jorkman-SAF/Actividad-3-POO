import tkinter as tk
import math

def calcular_soluciones():
    A = float(A_entry.get())
    B = float(B_entry.get())
    C = float(C_entry.get())

    discriminante = B**2 - 4*A*C

    if discriminante >= 0:
        x1 = (-B + math.sqrt(discriminante)) / (2*A)
        x2 = (-B - math.sqrt(discriminante)) / (2*A)
        
        resultado_label.config(text="Las soluciones son:\n x1 = {:.2f}\n x2 = {:.2f}".format(x1, x2))
    else:
        resultado_label.config(text="La ecuación no tiene solución real.")

ventana = tk.Tk()
ventana.title("Calculadora de Ecuación Cuadrática")

A_label = tk.Label(ventana, text="Valor de A:")
A_label.pack()
A_entry = tk.Entry(ventana)
A_entry.pack()

B_label = tk.Label(ventana, text="Valor de B:")
B_label.pack()
B_entry = tk.Entry(ventana)
B_entry.pack()

C_label = tk.Label(ventana, text="Valor de C:")
C_label.pack()
C_entry = tk.Entry(ventana)
C_entry.pack()

calcular_button = tk.Button(ventana, text="Calcular", command=calcular_soluciones)
calcular_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
