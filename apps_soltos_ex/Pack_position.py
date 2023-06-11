from tkinter import Label, Tk, RIGHT, BOTH, RAISED
from tkinter.constants import LEFT
from tkinter.ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Botões")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=2)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)
        
        # Eu adicionei 
        camada_label = Label(frame, text="Dentro da variável frame. Expand=True")
        camada_label.pack(expand=True)
        camada_label_2 = Label(frame, text="Dentro da variável frame. fill=BOTH, expand=True")
        camada_label_2.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Fechar", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK", command=self.destroy)
        okButton.pack(side=RIGHT, ipadx=5, ipady=5)
        outroButton = Button(self, text="outro",)
        outroButton.pack(side=LEFT)

        camada_label = Label(text="Fora de tudo, parece statusbar")
        camada_label.pack()


def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()