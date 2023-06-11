#python > from tkinter import * > dir(Tk)
from tkinter import *
from tkinter import ttk

menu_inicial = Tk()
menu_inicial.title("Primeira Aplicação")
menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True, True) #Aceita (True, True)
menu_inicial.minsize(width=500, height=250)   #Aceita (500, 250)
menu_inicial.maxsize(width=1000, height=500) 
# menu_inicial.state("zoomed") #iconic -> iniciar minimizado #zoomed -> inicia maximizado
menu_inicial.iconbitmap('VS_Code_GitHub\Ico-Fig-doc\Brasil.ico')


def cmd_Click(mensagem):
    print(mensagem)

cmd1 = Button(menu_inicial, text="Executar", command=lambda: cmd_Click("Nova mensagem"))
cmd1.pack()

cmd2 = Button(menu_inicial, text="Clicar", command=lambda: print("OK"))
cmd2.pack()



menu_inicial.mainloop()