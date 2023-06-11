 #python > from tkinter import * > dir(Tk)
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira Aplicação")
menu_inicial.geometry("500x500")
menu_inicial.geometry("%dx%d+%d+%d" % (500, 500, ((menu_inicial.winfo_screenwidth())/2 - 500/2), ((menu_inicial.winfo_screenheight())/2 - 500/2)))

# label_1 = Label(
#     menu_inicial,
#     text="Frase1\n\nfrase2",
#     font="Arial 20",
#     borderwidth=5,
#     relief="solid")
# label_1.pack()

border = 5

label_2 = Label(
    menu_inicial,
    text="solid",
    font="Arial 20",
    borderwidth=border,
    relief="solid",
    width=25,
    height=4,
    anchor=CENTER)
label_2.pack()

label_2 = Label(
    menu_inicial,
    text="groove",
    font="Arial 20",
    borderwidth=border,
    relief="groove")
label_2.pack()

label_2 = Label(
    menu_inicial,
    text="flat",
    font="Arial 20",
    borderwidth=border,
    relief="flat")
label_2.pack()

label_2 = Label(
    menu_inicial,
    text="raised",
    font="Arial 20",
    borderwidth=border,
    relief="raised")
label_2.pack()

label_2 = Label(
    menu_inicial,
    text="sunken",
    font="Arial 20",
    borderwidth=border,
    relief="sunken")
label_2.pack()

label_2 = Label(
    menu_inicial,
    text="ridge",
    font="Arial 20",
    borderwidth=border,
    relief="ridge")
label_2.pack()


menu_inicial.mainloop()