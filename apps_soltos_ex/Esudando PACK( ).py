from tkinter import * 
from tkinter.constants import *

'''
>>>> pack = configure = config = pack_configure  <<<<
objeto.pack() = objeto.configure = objeto.config = objeto.pack_configure

expand [True/False ou 1/0]
    -> expande o widget se o tamanho do pai aumentar

fill [X ou Y ou BOTH]
    -> preencher widget se o widget crescer

ipadx [número inteiro]
    -> adicione preenchimento interno na direção x

ipady [número inteiro]
    -> adicionar preenchimento interno na direção y

padx = [número inteiro]
    -> adicionar preenchimento na direção x

pady = [número inteiro]
    -> adicionar preenchimento na direção y

side [TOP(topo) ou BOTTOM(inferior) ou LEFT ou RIGHT] 
    ->  onde adicionar este widget

'''
class MontarFrame:
    def __init__(self, pai):
        self.pai = pai
        self.frame = Frame(self.pai, relief=RIDGE, borderwidth=5, bg="#fff")
        self.label = Label(self.frame, text="Hello, World", bg="gold")
        self.button = Button(self.frame,text="Exit",command=self.pai.destroy)

        self.frame.pack(fill=BOTH, expand=True, side=LEFT)
        self.label.pack(fill=BOTH, expand=1)
        self.button.pack(side=BOTTOM)

        self.frame_2 = Frame(self.pai, relief=RIDGE, borderwidth=5, bg="#FFFFF0")
        self.label_2 = Label(self.frame_2, text="Aqui é o outro label", bg="silver")
        self.button_2 = Button(self.frame_2, text="Exit2", command=self.pai.quit)

        self.frame_2.pack(fill=BOTH, expand=True, side=LEFT)
        self.label_2.pack(fill=BOTH, expand=1)
        self.button_2.pack(side=BOTTOM)

tk = Tk()
f1 = MontarFrame(frame1)
f1.pack()

tk.mainloop()





