from tkinter import *
from tkinter import  ttk

corBotao = "green"
conteudo = "Clique aqui para ficar amarelo"

if corBotao == "green":
    corBotao = "yellow"
    conteudo = "Clique aqui para ficar amarelo"
else:
    corBotao = "green"
    conteudo = "Clique aqui para ficar amarelo"

app = Tk()

frame = Frame(app)
frame.pack()

texto = Label(frame, text=conteudo)
texto.pack()

botaoVerde = Button(frame, text="Clique", bg=corBotao)
botaoVerde.pack()

mudar = Entry(app, background="gold")
mudar.pack()
mudar = ttk.Entry(app, background="gold", ip)
mudar.pack()


app.mainloop()
