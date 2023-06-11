from tkinter import *

root = Tk()
root.title("Scale")
root.iconbitmap("Imagens\_frutas\Alex-T-Minimal-Fruit-Pear.ico")
root.geometry("300x200")

def verValor(valor):
    print(valor)

slide_horizontal = Scale(root,
    command=verValor,
    width=10, 
    from_=0,
    to=10,
    background="green",
    highlightbackground="gold",
    highlightcolor="blue",
    activebackground="blue",
    foreground="gold",
    font="Arial, 10",
    orient="horizontal",
    resolution="0.5")
slide_horizontal.pack()

slide_vertical = Scale(root,
    width=10, 
    from_=0,
    to=100,
    background="red",
    highlightbackground="gold",
    highlightcolor="blue",
    activebackground="blue",
    foreground="gold",
    font="Arial, 10",
    orient="vertical")
slide_vertical.pack()

def verValor_2():
    print(slide_vertical.get())

cmd = Button(root, text="Ver valor", command=verValor_2)
cmd.pack()

root.mainloop()