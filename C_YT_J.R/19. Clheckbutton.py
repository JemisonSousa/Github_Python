from tabnanny import check
from tkinter import *

def apresentar():
    print(valor_check.get())

root = Tk()

valor_check = IntVar()

check1 = Checkbutton(root, text="Esta é uma checkbox", variable=valor_check, command=apresentar).pack()
check2 = Checkbutton(root, text="Esta é uma checkbox").pack()
check3 = Checkbutton(root, text="Esta é uma checkbox").pack()
check4 = Checkbutton(root, text="Esta é uma checkbox").pack()


root.mainloop()