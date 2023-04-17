import tkinter as tk

class SalarioMensualCalculator:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Salario Mensual")

        # Etiqueta y entrada para el nombre del empleado
        self.lbl_nombre = tk.Label(self.ventana, text="Nombre del empleado:")
        self.lbl_nombre.pack()
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()

        # Etiqueta y entrada para el salario básico por hora
        self.lbl_salario_hora = tk.Label(self.ventana, text="Salario básico por hora:")
        self.lbl_salario_hora.pack()
        self.entry_salario_hora = tk.Entry(self.ventana)
        self.entry_salario_hora.pack()

        # Etiqueta y entrada para el número de horas trabajadas en el mes
        self.lbl_horas_trabajadas = tk.Label(self.ventana, text="Horas trabajadas en el mes:")
        self.lbl_horas_trabajadas.pack()
        self.entry_horas_trabajadas = tk.Entry(self.ventana)
        self.entry_horas_trabajadas.pack()

        # Botón para calcular
        self.btn_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.btn_calcular.pack()

        # Etiqueta para mostrar el resultado
        self.lbl_resultado = tk.Label(self.ventana, text="")
        self.lbl_resultado.pack()

    def calcular(self):
        nombre = self.entry_nombre.get()
        salario_hora = float(self.entry_salario_hora.get())
        horas_trabajadas = float(self.entry_horas_trabajadas.get())

        # Calcular el salario mensual
        salario_mensual = salario_hora * horas_trabajadas

        # Verificar si el salario mensual es mayor a $450.000
        if salario_mensual > 450000:
            self.lbl_resultado.config(text=f"Nombre: {nombre}\nSalario mensual: ${salario_mensual:.2f}")
        else:
            self.lbl_resultado.config(text=f"Nombre: {nombre}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = SalarioMensualCalculator(ventana)
    ventana.mainloop()
