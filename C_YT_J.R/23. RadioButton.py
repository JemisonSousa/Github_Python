from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Radiobutton")
root.iconbitmap("Imagens\_frutas\Alex-T-Minimal-Fruit-Pear.ico")
root.geometry("500x400")

frameA = Frame(root).pack()
frameB = Frame(root).pack()

valor_a = IntVar()
valor_b = IntVar()

ra_1 = Radiobutton(frameA, text="Opção A 1", variable=valor_a, value=1)
ra_2 = Radiobutton(frameA, text="Opção A 2", variable=valor_a, value=2)
ra_3 = Radiobutton(frameA, text="Opção A 3", variable=valor_a, value=3)
ra_1.pack()
ra_2.pack()
ra_3.pack()

ra_1.select()

def ver_radio():
    print(valor_a.get())

cmd = Button(root, text="Executar", command=ver_radio, background="#f1d5a1", fg="green", font="Consolas, 10", width=100)
cmd.pack()

# ---------------------------------------------------------------------------------
def ra_f1():
    print("Opcao 4")
def ra_f2():
    print("Opcao 5")
def ra_f3():
    print("Opcao 6")

ra_4 = Radiobutton(frameB, text="Opção B 1", variable=valor_b, value=4, command=ra_f1, indicatoron=0)
ra_5 = Radiobutton(frameB, text="Opção B 2", variable=valor_b, value=5, command=ra_f2, indicatoron=0)
ra_6 = Radiobutton(frameB, text="Opção B 3", variable=valor_b, value=6, command=ra_f3, indicatoron=0)
ra_4.pack()
ra_5.pack()
ra_6.pack()


sair = Button(root, text="Sair", command=root.quit, width=100, background='red').pack()
root.mainloop()