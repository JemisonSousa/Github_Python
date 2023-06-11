#python > from tkinter import * > dir(Tk)
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira Aplicação")
menu_inicial.geometry("500x400")

label_1 = Label(menu_inicial,
                text="Este é o label 1",
                font="times 20")
label_1.pack()

label_2 = Label(menu_inicial,
                text="Este é o label 2",
                font="Arial 20 bold italic")
label_2.pack()

label_3 = Label(menu_inicial,
                text="Este é o label 3",
                font="Verdana 42 bold",
                fg="#aaaaaa")
label_3.pack()

menu_inicial.mainloop()