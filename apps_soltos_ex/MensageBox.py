import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import BOTTOM

root= tk.Tk()
root.geometry('300x200')

def SairDoApp():
    MsgBox = messagebox.askquestion ('Sair do App','Deseja realmente sair?', icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Ufa!','Obrigado por ficar\nBem-vindo novamente')
        
buttonEg = ttk.Button (root, text='Sair do App',command=SairDoApp)
buttonEg.pack()
  
root.mainloop()