import tkinter as tk

class MayorValorGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Encontrar Mayor Valor")

        # Lista para almacenar los números ingresados
        self.numeros = []

        # Etiqueta y entrada para el valor de entrada
        self.lbl_valor = tk.Label(self.ventana, text="Ingrese un valor positivo:")
        self.lbl_valor.pack()
        self.entry_valor = tk.Entry(self.ventana)
        self.entry_valor.pack()

        # Botón para agregar el valor ingresado
        self.btn_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_numero)
        self.btn_agregar.pack()

        # Etiqueta para mostrar los números ingresados en orden
        self.lbl_numeros = tk.Label(self.ventana, text="")
        self.lbl_numeros.pack()

        # Botón para encontrar el mayor valor
        self.btn_encontrar_mayor = tk.Button(self.ventana, text="Encontrar Mayor Valor", command=self.encontrar_mayor_valor)
        self.btn_encontrar_mayor.pack()

    def agregar_numero(self):
        valor = self.entry_valor.get()
        if valor.isdigit() and int(valor) > 0:
            self.numeros.append(int(valor))
            self.lbl_numeros.config(text=f"Números ingresados: {self.numeros}")

    def encontrar_mayor_valor(self):
        if self.numeros:
            mayor_valor = max(self.numeros)
            self.lbl_numeros.config(text=f"Números ingresados: {self.numeros}\nMayor valor: {mayor_valor}")
        else:
            self.lbl_numeros.config(text="No se ha ingresado ningún número")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MayorValorGUI(ventana)
    ventana.mainloop()
