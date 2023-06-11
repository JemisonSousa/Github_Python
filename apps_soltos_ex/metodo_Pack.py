from tkinter import *
from tkinter import ttk

cor = "{vazia}"
listaA = ["Vermelho", "Verde", "Azul", "Preto"]

root = Tk()
root.iconbitmap('Ico-Fig-doc\Icon001.ico') #muda o icone do programa
root.title("Meu primeiro programa")
root.geometry("300x200")
root.configure(background="#B0C4DE")

frame = Frame(root, background="#f1f1f1", padx=10)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

botao_vermelho = Button(frame, text="Red", fg="red")
botao_vermelho.pack( side = LEFT)

botao_verde = Button(frame, text="Green", fg="green")
botao_verde.pack( side = RIGHT )

botao_azul = Button(frame, text="Blue", fg="blue")
botao_azul.pack( side = LEFT )

combobox = ttk.Combobox(root, text=listaA)


label = ttk.Label(root, text="A cor vai ser " + cor)
label.pack( side = TOP )


botao_preto = Button(bottomframe, text="Balck", fg="black")
botao_preto.pack( side = BOTTOM)

botao_sair = Button(bottomframe, text="SAIR", fg="black", command=root.quit)
botao_sair.pack()




root.mainloop()