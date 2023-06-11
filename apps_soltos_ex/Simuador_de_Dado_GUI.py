import random
from tkinter import *


class SimuladorDeDado:
    def __init__(self):
        
        self.jenela = Tk()
        self.jenela.geometry('400x300+300+200')

        def GerarValorDoDado():
            valor = random.randint(1, 6)
            print(valor)
            self.visor.config(text=valor)
        
        self.frame_principal = Frame(self.jenela)
        self.frame_principal.pack()

        self.label_texto_titulo = Label(self.frame_principal, text='GERADOR DE NÚMERO', font='Arial, 12', padx=10, pady=10)
        self.label_texto_titulo.pack()
        
        self.btn = Button(self.frame_principal, text='GERAR', command=GerarValorDoDado)
        self.btn.pack()
        
        self.visor = Label(self.frame_principal, text=0, font='Adobe, 80')
        #self.visor.config(font=GerarValorDoDado)
        self.visor.pack()

        #self.jenela.update
        self.jenela.mainloop()    

SimuladorDeDado()

