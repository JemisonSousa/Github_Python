 #python > from tkinter import * > dir(Tk)
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira Aplicação")
menu_inicial.geometry("500x500")
menu_inicial.geometry("%dx%d+%d+%d" % (500, 500, ((menu_inicial.winfo_screenwidth())/2 - 500/2), ((menu_inicial.winfo_screenheight())/2 - 500/2)))

label_1 = Label(
    menu_inicial,
    text="frase de teste",
    font="Arial 20",
    borderwidth=1,
    relief="solid",
    padx=50,
    pady=50)
label_1.pack()

label_2 = Label(
    menu_inicial,
    text="frase de teste\nAqui é outra frase",
    font="Arial 10",
    borderwidth=1,
    relief="solid",
    padx=5,
    pady=5,
    justify=CENTER)
label_2.pack()

label_3 = Label(
    menu_inicial,
    text="Frase de teste\nAqui é outra frase",
    font="Arial 20",
    borderwidth=1,
    relief="solid",
    width=30,
    height=5,
    justify=LEFT,
    anchor=W)
label_3.pack()

menu_inicial.mainloop()