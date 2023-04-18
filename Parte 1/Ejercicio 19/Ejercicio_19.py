import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_perimetro(self):
        return 3 * self.lado
    
    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado
    
    def calcular_area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Triángulo Equilátero")
        
        self.lbl_lado = tk.Label(self.root, text="Valor del lado:")
        self.lbl_lado.pack()
        self.entry_lado = tk.Entry(self.root)
        self.entry_lado.pack()
        
        self.btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular_resultados)
        self.btn_calcular.pack()
        
        self.lbl_perimetro = tk.Label(self.root, text="")
        self.lbl_perimetro.pack()
        
        self.lbl_altura = tk.Label(self.root, text="")
        self.lbl_altura.pack()
        
        self.lbl_area = tk.Label(self.root, text="")
        self.lbl_area.pack()
        
    def calcular_resultados(self):
        lado = self.entry_lado.get()
        
        if lado == "":
            messagebox.showerror("Error", "Por favor ingrese un valor para el lado.")
            return
        
        try:
            lado = float(lado)
        except ValueError:
            messagebox.showerror("Error", "El valor del lado debe ser un número.")
            return
        
        triangulo = TrianguloEquilatero(lado)
        
        perimetro = triangulo.calcular_perimetro()
        self.lbl_perimetro.configure(text=f"El perímetro es {perimetro:.2f}.")
        
        altura = triangulo.calcular_altura()
        self.lbl_altura.configure(text=f"La altura es {altura:.2f}.")
        
        area = triangulo.calcular_area()
        self.lbl_area.configure(text=f"El área es {area:.2f}.")
        
root = tk.Tk()
ventana_principal = VentanaPrincipal(root)
root.mainloop()
