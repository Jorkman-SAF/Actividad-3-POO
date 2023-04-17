import tkinter as tk

def calcular_salario():
    nombre = nombre_entry.get()
    salario_hora = float(salario_hora_entry.get())
    horas_trabajadas = float(horas_trabajadas_entry.get())

    salario_mensual = salario_hora * horas_trabajadas

    if salario_mensual > 450000:
        resultado_label.config(text="El salario mensual de {} es de ${:.2f}".format(nombre, salario_mensual))
    else:
        resultado_label.config(text=nombre)

ventana = tk.Tk()
ventana.title("Calculadora de Salario Mensual")

nombre_label = tk.Label(ventana, text="Nombre del empleado:")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

salario_hora_label = tk.Label(ventana, text="Salario básico por hora:")
salario_hora_label.pack()
salario_hora_entry = tk.Entry(ventana)
salario_hora_entry.pack()

horas_trabajadas_label = tk.Label(ventana, text="Horas trabajadas en el mes:")
horas_trabajadas_label.pack()
horas_trabajadas_entry = tk.Entry(ventana)
horas_trabajadas_entry.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

calcular_button = tk.Button(ventana, text="Calcular", command=calcular_salario)
calcular_button.pack()

ventana.mainloop()
