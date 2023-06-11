from tkinter import *

# pyinstaller --onefile -w --ico nome.ico Arquivo.py

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x300+300+300')
        self.label1 = Label(self.root, text="Sou a janela principal.")
        self.button = Button(self.root, text="segunda janela", command=self.command)
        self.button2 = Button(self.root, text="Sair", command=self.root.quit)
        self.label1.pack()
        self.button.pack()
        self.button2.pack()
    def command(self):
        self.root.iconify()
        self.top = Toplevel(self.root)
        self.top.geometry('200x200+300+300')
        self.label2 = Label(self.top, text="Eu sou a segunda janela")
        self.label2.pack()
        self.top.protocol("WM_DELETE_WINDOW", self.close) # para quando o X de fechar a janela for apertado
        self.button3 = Button(self.top, text="Voltar", command=self.close)
        self.button3.pack()
    def close(self):
        self.top.destroy()
        self.root.deiconify()

root = Tk()
App(root)
root.mainloop()
