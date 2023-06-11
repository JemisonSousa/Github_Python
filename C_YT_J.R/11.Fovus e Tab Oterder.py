from tkinter import *

def executar():
    l1["text"] = "O texto digitado foi: " + t1.get()
    l2["text"] = "O texto digitado foi: " + t2.get()
    l3["text"] = "O texto digitado foi: " + t3.get()

app = Tk()
app.title("Cadastrador")

t1 = Entry (app, width=30)
t2 = Entry (app, width=30)
t3 = Entry (app, width=30)
t1.grid(row=0, padx=5, pady=0.5)
t2.grid(row=1, padx=5, pady=0.5)
t3.grid(row=2, padx=5, pady=0.5)

t1.focus()

l1 = Label(app, text="")
l2 = Label(app, text="")
l3 = Label(app, text="")
l1.grid(row=3)
l2.grid(row=4)
l3.grid(row=5)

b1 = Button(app, text=" Executar ", command=executar)
b1.grid(row=6)

app.mainloop()
