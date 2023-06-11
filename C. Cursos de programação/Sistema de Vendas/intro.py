from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Splash:
    def __init__(self):
        self.splashmainw = Tk()
        self.splashmainw.title("CURSO DE VENDAS EM PYTHON TKINTER")
        width = 900
        height = 670
        self.splashmainw.config(bg = "green")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenheight()
        x = (tela_largura/2) - (width/2)
        y = (tela_altura/2) - (height/2)
        self.splashmainw.geometry("%dx%dx%dx%d" %width, height, x, y)
        self.splashmainw.resizable(0,0)
        path = "Imagens\_frutas\mango-icon.png"
        img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.splashmainw, width=890, height=560, background="snow", relief="sunken")
        main.place(x=55, y=70)
        fotoFrame = LabelFrame(main, width=420, height=440, background="snow", relief="raised")
        foto = Label(fotoFrame, image=img)
        foto.place(x=6, y=6)
        fotoFrame.place(x=10, y=100)

        # Aqui entras as mensagens de boas vindas
        self.splashmainw.mainloop()
