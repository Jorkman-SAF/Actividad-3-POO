import tkinter as tk

def comparar_valores():
    A = float(entry_A.get())
    B = float(entry_B.get())

    if A > B:
        resultado.set("A es mayor que B.")
    elif A < B:
        resultado.set("A es menor que B.")
    else:
        resultado.set("A es igual a B.")

ventana = tk.Tk()
ventana.title("Comparador de Valores")
ventana.geometry("300x200")

label_A = tk.Label(ventana, text="Valor de A:")
label_A.pack()
entry_A = tk.Entry(ventana)
entry_A.pack()

label_B = tk.Label(ventana, text="Valor de B:")
label_B.pack()
entry_B = tk.Entry(ventana)
entry_B.pack()

btn_comparar = tk.Button(ventana, text="Comparar", command=comparar_valores)
btn_comparar.pack()

resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()

ventana.mainloop()