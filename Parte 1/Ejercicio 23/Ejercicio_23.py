import tkinter as tk
from tkinter import messagebox
import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calcular_soluciones(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c
        if discriminante < 0:
            return None
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return x
        else:
            x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return x1, x2

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ecuación de Segundo Grado")
        
        self.lbl_a = tk.Label(self.root, text="Valor de a:")
        self.lbl_a.pack()
        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack()
        
        self.lbl_b = tk.Label(self.root, text="Valor de b:")
        self.lbl_b.pack()
        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack()
        
        self.lbl_c = tk.Label(self.root, text="Valor de c:")
        self.lbl_c.pack()
        self.entry_c = tk.Entry(self.root)
        self.entry_c.pack()
        
        self.btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular_soluciones)
        self.btn_calcular.pack()
        
        self.lbl_resultado = tk.Label(self.root, text="")
        self.lbl_resultado.pack()
        
    def calcular_soluciones(self):
        a = self.entry_a.get()
        b = self.entry_b.get()
        c = self.entry_c.get()
        
        if a == "" or b == "" or c == "":
            messagebox.showerror("Error", "Por favor ingrese valores para a, b y c.")
            return
        
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            messagebox.showerror("Error", "Los valores de a, b y c deben ser números.")
            return
        
        ecuacion = EcuacionSegundoGrado(a, b, c)
        soluciones = ecuacion.calcular_soluciones()
        
        if soluciones is None:
            self.lbl_resultado.configure(text="La ecuación no tiene soluciones reales.")
        elif type(soluciones) == float:
            self.lbl_resultado.configure(text=f"La solución es x = {soluciones:.2f}.")
        else:
            self.lbl_resultado.configure(text=f"Las soluciones son x1 = {soluciones[0]:.2f} y x2 = {soluciones[1]:.2f}.")

root = tk.Tk()
ventana_principal = VentanaPrincipal(root)
root.mainloop()
