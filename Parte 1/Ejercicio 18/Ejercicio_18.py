import tkinter as tk

def calcular_salario():
    codigo = codigo_entry.get()
    nombres = nombres_entry.get()
    horas_trabajadas = float(horas_trabajadas_entry.get())
    valor_hora = float(valor_hora_entry.get())
    porcentaje_retencion = float(porcentaje_retencion_entry.get())

    salario_bruto = horas_trabajadas * valor_hora
    retencion = salario_bruto * (porcentaje_retencion / 100)
    salario_neto = salario_bruto - retencion

    resultado_label.config(text="Código del empleado: {}\nNombres del empleado: {}\nSalario bruto: {}\nSalario neto: {}".format(codigo, nombres, salario_bruto, salario_neto))

ventana = tk.Tk()
ventana.title("Calculadora de Salario")
ventana.geometry("400x300")

codigo_label = tk.Label(ventana, text="Ingrese el código del empleado:")
codigo_label.pack()
codigo_entry = tk.Entry(ventana)
codigo_entry.pack()

nombres_label = tk.Label(ventana, text="Ingrese los nombres del empleado:")
nombres_label.pack()
nombres_entry = tk.Entry(ventana)
nombres_entry.pack()

horas_trabajadas_label = tk.Label(ventana, text="Ingrese el número de horas trabajadas al mes:")
horas_trabajadas_label.pack()
horas_trabajadas_entry = tk.Entry(ventana)
horas_trabajadas_entry.pack()

valor_hora_label = tk.Label(ventana, text="Ingrese el valor por hora trabajada:")
valor_hora_label.pack()
valor_hora_entry = tk.Entry(ventana)
valor_hora_entry.pack()

porcentaje_retencion_label = tk.Label(ventana, text="Ingrese el porcentaje de retención en la fuente:")
porcentaje_retencion_label.pack()
porcentaje_retencion_entry = tk.Entry(ventana)
porcentaje_retencion_entry.pack()

calcular_button = tk.Button(ventana, text="Calcular salario", command=calcular_salario)
calcular_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
