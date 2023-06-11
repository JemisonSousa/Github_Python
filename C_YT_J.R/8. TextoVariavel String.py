from tkinter import *

app = Tk()
app.title("LABEL TEXTVARIABLE E STRINGVAR")
app.geometry("500x500")
app.geometry("%dx%d+%d+%d" % (500, 500, ((app.winfo_screenwidth())/2 - 500/2), ((app.winfo_screenheight())/2 - 500/2)))
app.iconbitmap("Ico-Fig-doc\carOfic.ico")

texto = StringVar()
texto.set ("Aqui é o texto da variável Texto")

label_1 = Label(app,
    font = "Arial 20",
    bg = "red",
    fg = "white",
    textvariable = texto
)
label_1.pack()

label_2 = Label(app,
    font = "Arial 20",
    bg = "red",
    fg = "white",
    textvariable = texto
)
label_2.pack()

texto.set("Testinho")

app,mainloop()