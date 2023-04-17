import tkinter as tk
from tkinter import messagebox

def calcular_matricula():
    numero_inscripcion = entry_numero_inscripcion.get()
    nombres = entry_nombres.get()
    patrimonio = float(entry_patrimonio.get())
    estrato_social = int(entry_estrato_social.get())

    valor_constante = 50000
    porcentaje_incremento = 0.03

    if patrimonio > 2000000 and estrato_social > 3:
        incremento = patrimonio * porcentaje_incremento
    else:
        incremento = 0

    pago_matricula = valor_constante + incremento

    messagebox.showinfo("Resultado", f"Número de inscripción: {numero_inscripcion}\nNombres: {nombres}\nPago de matrícula: ${pago_matricula}")

root = tk.Tk()
root.title("Calculadora de Matrícula")

label_numero_inscripcion = tk.Label(root, text="Número de inscripción:")
label_numero_inscripcion.grid(row=0, column=0, padx=10, pady=10)
entry_numero_inscripcion = tk.Entry(root)
entry_numero_inscripcion.grid(row=0, column=1)

label_nombres = tk.Label(root, text="Nombres:")
label_nombres.grid(row=1, column=0, padx=10, pady=10)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)

label_patrimonio = tk.Label(root, text="Patrimonio:")
label_patrimonio.grid(row=2, column=0, padx=10, pady=10)
entry_patrimonio = tk.Entry(root)
entry_patrimonio.grid(row=2, column=1)

label_estrato_social = tk.Label(root, text="Estrato social:")
label_estrato_social.grid(row=3, column=0, padx=10, pady=10)
entry_estrato_social = tk.Entry(root)
entry_estrato_social.grid(row=3, column=1)

button_calcular = tk.Button(root, text="Calcular", command=calcular_matricula)
button_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
