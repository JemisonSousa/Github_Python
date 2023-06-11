from functools import total_ordering
from select import select
from tkinter import *
from tkinter import ttk

class Nova_Janela:
    def __init__(self):
        self.root = Tk()
        self.nova_janela = Criar_Frame(self.root)
        self.btn_sair = ttk.Button(self.root, text="Sair", command=self.root.quit).grid()
        self.root.mainloop()

class Criar_Frame:
    def  __init__(self, pai, coluna=0, linha=0, cor_frame=None, cor_label=None):
        super().__init__()
        self.pai = pai
        self.coluna = coluna
        self.linha = linha
        self.cor_frame = cor_frame
        self.cor_label = cor_label
        self.ini_frame()

    def ini_frame(self):
        frame = Frame(self.pai, background=self.cor_frame)
        frame.grid()
        labal_texto = Label(frame, text="Nome", background=self.cor_label)
        labal_texto.grid(column=self.coluna, row=self.linha)
        entry_texto = Entry(frame)
        entry_texto.grid(column=self.coluna + 1, row=self.linha)


root = Tk()
root.geometry("%dx%d" % (200, 200))
f1 = Criar_Frame(root)
f2 = Criar_Frame(root, 1, 0, "red", "blue")
f3 = Criar_Frame(root, 2, 0, "red", "blue")
f2 = Criar_Frame(root, 1, 1, "red", "blue")
f3 = Criar_Frame(root, 1, 2, "red", "blue")
f2 = Criar_Frame(root, 2, 0, "red", "blue")
f3 = Criar_Frame(root, 2, 1, "red", "blue")

btn = ttk.Button(root, text="Abrir nova canela", command=Nova_Janela)
btn.grid()

root.mainloop()