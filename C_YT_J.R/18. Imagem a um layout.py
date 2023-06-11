''' https://iconarchive.com/ '''

from tkinter import *

root = Tk()
root.title("Imagens")
root.iconbitmap("Imagens\_frutas\Alex-T-Minimal-Fruit-Apple.ico")

var_imagem_1 = PhotoImage(file="Imagens\_frutas\orange-icon.png")
var_imagem_2 = PhotoImage(file="Imagens\_frutas\Apple-icon.png")

label_image_1 = Label(root, image=var_imagem_1).grid(row=0, column=0)
label_image_2 = Label(root, image=var_imagem_2).grid(row=0, column=1)


root.mainloop()