from tkinter import *

app = Tk()
app.title("Alterar Propriedades")
app.geometry("500x500")
app.geometry("%dx%d+%d+%d" % (500, 500, ((app.winfo_screenwidth())/2 - 500/2), ((app.winfo_screenheight())/2 - 500/2)))
app.iconbitmap("Ico-Fig-doc\carOfic.ico")

label_1 = Label(
    app,
    text="texto",
    font="Arial 20",
    bd=1,
    relief="solid"
)
label_1.pack()

label_2 = Label(app)
label_2["text"] = "Texto do label 2"
label_2["font"] = "Arial 20"
label_2["bd"] = 1
label_2["relief"] = "solid"

label_2.pack()

print(label_2["text"])
label_2["text"] = "Aqui é um novo texto"

app.mainloop()