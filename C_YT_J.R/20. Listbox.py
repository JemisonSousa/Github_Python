from tkinter import *

root = Tk()
root.title("Listbox")
root.iconbitmap("Imagens\_frutas\Alex-T-Minimal-Fruit-Pear.ico")

lista = Listbox(root).pack()

# Inserir uma item de cada vez
'''
lista.insert(0, "Segundo item da lista")
lista.insert(1, "Segundo item da lista")
lista.insert(END, "Terceiro item da lista")
lista.insert(END, "Quarto item da lista")
'''

# inserir vário itens a partir de uma lista
nomes = ["João", "Ana", "Carlos"]
for nome in nomes:
    lista.insert(END, nome)

lista.delete(0,END) #apaga todos
lista.delete(1,1) #apaga só um segundo

def executar():
    print(lista.get(ACTIVE))

cmd = Button(root, text="Clique", command=executar)

root.mainloop()
