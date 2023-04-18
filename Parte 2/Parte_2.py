import tkinter as tk
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base + self.altura + math.sqrt(self.base ** 2 + self.altura ** 2)
    
    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)
    
    def tipo_triangulo(self):
        if self.base == self.altura:
            return "Equilátero"
        elif self.base == self.hipotenusa() or self.altura == self.hipotenusa():
            return "Isósceles"
        else:
            return "Escaleno"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculadora de figuras geométricas")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.figura_label = tk.Label(self, text="Seleccione la figura:")
        self.figura_label.grid(row=0, column=0, sticky="w")
        
        self.figura = tk.StringVar(self)
        self.figura.set("Círculo") # Valor por defecto
        
        self.figura_dropdown = tk.OptionMenu(self, self.figura, "Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo")
        self.figura_dropdown.grid(row=0, column=1)
        
        self.dimensiones_label = tk.Label(self, text="Ingrese las dimensiones (separadas por ','): ")
        self.dimensiones_label.grid(row=1, column=0, sticky="w")
        
        self.dimensiones_entry = tk.Entry(self)
        self.dimensiones_entry.grid(row=1, column=1)
        
        self.resultados_label = tk.Label(self, text="Resultados:")
        self.resultados_label.grid(row=2, column=0, sticky="w")
        
        self.resultados_text = tk.Text(self, height=5, width=40)
        self.resultados_text.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=4, column=0, pady=10)
        
        self.salir_button = tk.Button(self, text="Salir", command=self.master.quit)
        self.salir_button.grid(row=4, column=1, pady=10)
        
    def calcular(self):
        figura = self.figura.get()
        dimensiones = self.dimensiones_entry.get().split(",")
        if figura == "Círculo":
            radio = float(dimensiones[0])
            circulo = Circulo(radio)
            area = circulo.area()
            perimetro = circulo.perimetro()
            self.resultados_text.delete("1.0", tk.END)
            self.resultados_text.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        elif figura == "Rectángulo":
            base = float(dimensiones[0])
            altura = float(dimensiones[1])
            rectangulo = Rectangulo(base, altura)
            area = rectangulo.area()
            perimetro = rectangulo.perimetro()
            self.resultados_text.delete("1.0", tk.END)
            self.resultados_text.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        elif figura == "Cuadrado":
            lado = float(dimensiones[0])
            cuadrado = Cuadrado(lado)
            area = cuadrado.area()
            perimetro = cuadrado.perimetro()
            self.resultados_text.delete("1.0", tk.END)
            self.resultados_text.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        elif figura == "Triángulo Rectángulo":
            base = float(dimensiones[0])
            altura = float(dimensiones[1])
            triangulo = TrianguloRectangulo(base, altura)
            area = triangulo.area()
            perimetro = triangulo.perimetro()
            hipotenusa = triangulo.hipotenusa()
            tipo_triangulo = triangulo.tipo_triangulo()
            self.resultados_text.delete("1.0", tk.END)
            self.resultados_text.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}\nHipotenusa: {hipotenusa}\nTipo triangulo: {tipo_triangulo}")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
