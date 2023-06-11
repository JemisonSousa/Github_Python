from tkinter import *


class Janela():
    def __dir__(self, Toplevel):
        self.frame = Frame(Toplevel)
        self.frame.pack()
        self.texto = Label(self.frame, text="Clique aqui para ficar amarelo")
        self.texto["width"] = 26
        self.texto["height"] = 3
        self.texto.pack()
        self.botaoVerde = Button(self.frame, text="Clique")
        self.botaoVerde["background"] = "green"
        self.botaoVerde.bind("<Button-1>", self.mudarCor())
        self.botaoVerde.pack()

    def mudarCor(self, event):
        if self.botaoVerde["background"] == "green":
            self.botaoVerde["background"] = "yellow"
            self.texto["text"] = "Clique aqui para ficar verde"
        else:
            self.botaoVerde["background"] = "green"
            self.texto["text"] = "Clique aqui para ficar amarelo"


raiz = Tk()
#app = Janela()
Janela()

raiz.mainloop()
