#instalar o pyttsx3
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root = Tk()
root.title("Leitor de texto")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")


engine = pyttsx3.init()

def falarAgora():
    text = text_area.get(1.0, END)
    genero = genero_combobox.get()
    velocidade = velocidade_combobox.get()
    vozes = engine.getProperty("voices")

    def mudarVoz():
        if (genero == "Masculino"):
            engine.setProperty("voice", vozes[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice", vozes[1].id)
            engine.say(text)
            engine.runAndWait()
            
    if (text):
        if (velocidade == "Rápido"):
            engine.setProperty("rate", 250)
            mudarVoz()
        elif (velocidade == "Normal"):
            engine.setProperty("rate", 150)
            mudarVoz()
        else:
            engine.setProperty("rate", 60)
            mudarVoz()
        
            
def download():
    text = text_area.get(1.0, END)
    genero = genero_combobox.get()
    velocidade = velocidade_combobox.get()
    vozes = engine.getProperty("voices")

    def mudarVoz():
        if (genero == "Masculino"):
            engine.setProperty("voice", vozes[0].id)
            caminho = filedialog.askdirectory()
            os.chdir(caminho)
            engine.save_to_file(text, "texto.mp3")
            engine.runAndWait()
        else:
            engine.setProperty("voice", vozes[1].id)
            caminho = filedialog.askdirectory()
            os.chdir(caminho)
            engine.save_to_file(text, "texto.mp3")
            engine.runAndWait()
            
    if (text):
        if (velocidade == "Rápido"):
            engine.setProperty("rate", 250)
            mudarVoz()
        elif (velocidade == "Normal"):
            engine.setProperty("rate", 150)
            mudarVoz()
        else:
            engine.setProperty("rate", 60)
            mudarVoz()
        


#ICON
#icon = PhotoImage(file="VS_Code_GitHub\PYTHON\Projetos\Speech\Speak-app.png") #Caminho relativo
icon = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Speech\\Speak-app.png") #Caminho relativo
root.iconphoto(True, icon)

#FRAME SUPERIOR
top_frame = Frame(root, bg="white", width=900, height=100)
top_frame.place(x=0, y=0)

#logo = PhotoImage(file="VS_Code_GitHub\PYTHON\Projetos\Speech\Speak-app.png")
logo = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Speech\\Speak-app.png")
Label(top_frame, image=logo, bg="white").place(x=10, y=10)

Label(top_frame,
      text="LEITOR DE TEXTO",
      font="arial 20 bold",
      bg="white", fg="black").place(x=100, y=30)


#########################################################################################
text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)


Label(root, text="VOZES",
      font="arial 15 bold",
      bg="#305065",
      fg="white").place(x=580, y=160)

Label(root, text="VELOCIDADE",
      font="arial 15 bold",
      bg="#305065",
      fg="white").place(x=730, y=160)


genero_combobox = Combobox(root,
                           values=["Masculino", "Feminino"],
                           font="arial 14", state="r",
                           width=10)
genero_combobox.place(x=550, y=200)
genero_combobox.set("Masculino")


velocidade_combobox = Combobox(root,
                           values=["Rápido", "Normal", "Lento"],
                           font="arial 14", state="r",
                           width=10)
velocidade_combobox.place(x=730, y=200)
velocidade_combobox.set("Normal")


#imageicon = PhotoImage(file="VS_Code_GitHub\PYTHON\Projetos\Speech\Speak-icon.png")
imageicon = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Speech\\Speak-icon.png")
btn = Button(root,
             text="Falar", compound=LEFT, image=imageicon,
             width=130, font="arial 14 bold", command=falarAgora)
btn.place(x=550, y=280)

#imageicon2 = PhotoImage(file="VS_Code_GitHub\PYTHON\Projetos\Speech\Download-icon.png")
imageicon2 = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Speech\\Download-icon.png")
save = Button(root,
             text="Salvar", compound=LEFT, image=imageicon2,
             width=130, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=730, y=280)


root.mainloop()

