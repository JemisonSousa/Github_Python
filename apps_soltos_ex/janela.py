from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from turtle import pd, st

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def pegarConteudo(self):
        pass

    def initUI(self):
        self.master.title("Windows")
        # self.pack(fill=BOTH, expand=True)
        self.pack()

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Windows")
        lbl.grid(row=0, column=0, sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)
        
        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close", command=self.quit)
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Help", command=Example)
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK", command=clickOK)
        obtn.grid(row=5, column=3)

    

def clickOK():
    conteudoArea = Example.area
    print(conteudoArea)


def main():
    root = Tk()
    root.geometry("450x350+420+200")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()