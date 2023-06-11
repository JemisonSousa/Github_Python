import pyautogui as p
import time
import tkinter as tk

from tkinter import Label, Tk, RIGHT, BOTH, RAISED
from tkinter.constants import LEFT
from tkinter.ttk import Frame, Button, Style


class Main:
    def __init__(self):
        p.PAUSE = 0.5
        p.press('winleft')
        p.write('edge')
        p.press('enter')
        p.hotkey('ctrl', 'l')
        time.sleep(2)
        p.write('sped.rfb.gov.br/')
        p.press('enter')
                
    def baixarEFDContib():
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab');p.press('tab');p.press('tab')
        p.press('tab');p.press('tab');p.press('tab')
        p.press('enter')        

 
class Janela(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.master.title("Baixardor de XML")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=2)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)
        
        # Eu adicionei 
        camada_label_2 = Label(frame, text="O Programinha baixará de JAN/2017 a DEZ/2021.\nDeixe o navegador com o certificado\njá escolhido para empresa")
        camada_label_2.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Fechar", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        outroButton = Button(self, text="Iniciar", command=Main)
        outroButton.pack(side=LEFT)

        camada_label = Label(text="__-*_*-__")
        camada_label.pack()


def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Janela()
    root.mainloop()


if __name__ == '__main__':
    main()