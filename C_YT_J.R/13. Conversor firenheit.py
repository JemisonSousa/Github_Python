from tkinter import *

def calcular():
    fahrenheit = float(entre_texto.get())
    celsius = (fahrenheit - 32) * 5/9
    final.set(str(round(celsius, 1)) + " graus Celsius")

root = Tk()
root.title("Conversor")
root.geometry("300x300")

final = StringVar()

label_texto = Label(root, text="Insira os dados em Graus Fahrenheit:")
entre_texto = Entry(root)
botao = Button(root, text="Calcular", command=calcular)
label_resultado = Label(root, textvariable=final, font="Arial, 12")

label_texto.grid(row=0, column=0)
entre_texto.grid(row=0, column=1)
botao.grid(row=1, column=1)
label_resultado.grid(row=1, column=0)




root.mainloop()