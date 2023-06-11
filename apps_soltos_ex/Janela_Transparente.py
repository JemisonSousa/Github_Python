from tkinter import *
import time

from matplotlib.pyplot import twinx

def printarAlgo():
    print("O botão da função foi acionado")

class Login:
    def __init__(self) -> None:
                
        root = Tk()
        root.title("Janela transparente")
        root.resizable(0, 0)
        root.geometry('600x500+300+300')
        root.attributes('-alpha', 0.75)
        
                
        label_login = Label(root, text="Aqui fica algo", background="black", foreground="white")
        label_login.pack()

        botao_1 = Button(root, text="Clique aqui", command=printarAlgo)
        botao_1.pack()

        frame1 = LabelFrame(root, text="coisas velhas", background='green')
        frame1.pack(fill=BOTH, expand=True)

        label2 = Label(frame1, text="Dentro do label frema", )
        label2.pack()

        
        root.mainloop()
            
Login()
