import tkinter as tk

def calcular_salario():
    codigo = codigo_entry.get()
    nombres = nombres_entry.get()
    horas_trabajadas = float(horas_entry.get())
    valor_hora = float(valor_entry.get())
    porcentaje_retencion = float(retencion_entry.get())

    salario_bruto = horas_trabajadas * valor_hora
    retencion = salario_bruto * (porcentaje_retencion / 100)
    salario_neto = salario_bruto - retencion

    codigo_label.config(text="Código del empleado: {}".format(codigo))
    nombres_label.config(text="Nombres del empleado: {}".format(nombres))
    salario_bruto_label.config(text="Salario bruto: {}".format(salario_bruto))
    salario_neto_label.config(text="Salario neto: {}".format(salario_neto))

# Crear ventana
ventana = tk.Tk()

# Crear etiquetas
codigo_label = tk.Label(ventana, text="Código del empleado:")
nombres_label = tk.Label(ventana, text="Nombres del empleado:")
horas_label = tk.Label(ventana, text="Horas trabajadas al mes:")
valor_label = tk.Label(ventana, text="Valor por hora trabajada:")
retencion_label = tk.Label(ventana, text="Porcentaje de retención en la fuente:")
salario_bruto_label = tk.Label(ventana, text="Salario bruto:")
salario_neto_label = tk.Label(ventana, text="Salario neto:")

# Crear campos de entrada
codigo_entry = tk.Entry(ventana)
nombres_entry = tk.Entry(ventana)
horas_entry = tk.Entry(ventana)
valor_entry = tk.Entry(ventana)
retencion_entry = tk.Entry(ventana)

# Crear botón
calcular_button = tk.Button(ventana, text="Calcular", command=calcular_salario)

# Colocar elementos en la ventana
codigo_label.grid(row=0, column=0)
codigo_entry.grid(row=0, column=1)
nombres_label.grid(row=1, column=0)
nombres_entry.grid(row=1, column=1)
horas_label.grid(row=2, column=0)
horas_entry.grid(row=2, column=1)
valor_label.grid(row=3, column=0)
valor_entry.grid(row=3, column=1)
retencion_label.grid(row=4, column=0)
retencion_entry.grid(row=4, column=1)
calcular_button.grid(row=5, column=1)
salario_bruto_label.grid(row=6, column=0)
salario_neto_label.grid(row=7, column=0)

# Ejecutar la ventana
ventana.mainloop()
