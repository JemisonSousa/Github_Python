from tkinter import *
from tkinter import ttk

# pyinstaller --onefile -w --ico nome.ico Arquivo.py


root = Tk()
root.title("Sistema Qualker®")
root.geometry('600x400+5+300')
# root.iconbitmap(default='VS_Code_GitHub\Imagens\_frutas\_botoes\_jpg_bar-graph.ico')
icon = PhotoImage(file="VS_Code_GitHub\Imagens\_frutas\_botoes\_btn_ONOFF_MEIO.png")
root.iconphoto(True, icon)

Label(root, text="O icone foi mudado para um arquivo PNG").pack()

root.mainloop()
