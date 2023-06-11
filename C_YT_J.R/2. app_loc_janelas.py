#python > from tkinter import * > dir(Tk)
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira Aplicação")

#dimensoes da janela
largura = 500
altura = 300

#resolucao do nosso sitema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

# posicao da janela
posicao_x = largura_screen/2 - largura/2
posicao_y = altura_screen/2 - altura/2

# definir a geometry
# menu_inicial.geometry(f"{posicao_x}x{posicao_y}+{largura}+{altura}")
menu_inicial.geometry("%dx%d+%d+%d" % (500, 300, ((menu_inicial.winfo_screenwidth())/2 - 500/2), ((menu_inicial.winfo_screenheight())/2 - 300/2)))
# menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posicao_x, posicao_y))



menu_inicial.mainloop()