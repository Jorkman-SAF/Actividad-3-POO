import tkinter as tk

def calcular():
    lado = float(lado_entry.get())

    perimetro = 3 * lado
    altura = (lado * (3 ** 0.5)) / 2
    area = (lado ** 2) * (3 ** 0.5) / 4

    resultado_text.set("El perímetro del triángulo es: {}\nLa altura del triángulo es: {}\nEl área del triángulo es: {}".format(perimetro, altura, area))

ventana = tk.Tk()
ventana.title("Cálculo de Triángulo Equilátero")

lado_label = tk.Label(ventana, text="Ingrese el valor del lado del triángulo equilátero:")
lado_label.pack()

lado_entry = tk.Entry(ventana)
lado_entry.pack()

calcular_button = tk.Button(ventana, text="Calcular", command=calcular)
calcular_button.pack()

resultado_text = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_text)
resultado_label.pack()

ventana.mainloop()
