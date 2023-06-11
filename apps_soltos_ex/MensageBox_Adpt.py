import tkinter as tk
from tkinter import Frame, messagebox, ttk
from tkinter.constants import BOTTOM

root= tk.Tk()
root.geometry('300x200')

def SairDoApp():
    MsgBox = messagebox.askyesno('Sair do App','Deseja realmente sair?', icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Ufa!','Obrigado por ficar\nBem-vindo novamente')

def MudarCorDeFundo_root():
    Pergunta = messagebox.askyesno("Mudar fundo", "Deseja mudar a cor de fundo da tela?")
    if Pergunta == "yes":
        root.configure(background="black")
    else:
        root.configure(background="prink")


frame_1 = Frame(root, background="black")
frame_1.pack()

botao_1 = ttk.Button (root, text='Sair do App',command=SairDoApp)
botao_1.pack()

botao_2 = ttk.Button (root, text='Mudar',command=MudarCorDeFundo_root)
botao_2.pack(side=BOTTOM)


  
root.mainloop()