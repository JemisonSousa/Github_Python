#Bandeiras Aleatórias

# acho que não deu muito certo

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import sys

#funcao-sort
def sort():
    img = PhotoImage(file='VS_Code_GitHub\Imagens\_frutas\_botoes\download_PNG.png')
    IMAGE1['image'] = img
    IMAGE3['image'] = img
    
#end-func

#funcao-credits
def credits():
    credit = messagebox.showinfo(message='Feito por Nícholas André',title="Créditos")
#end-func
#funcao-quit
def quit():
    sys.exit(0)
#end-func

#definição da janela e do frame
window = Tk()
window.title("Bandeiras Aleatórias")
window.minsize(380,200)
frame = ttk.Frame(window, padding = "3 3 12 12")
frame.grid(column=0,row=0,padx=20)
#end

#label-title
title_font = font.Font(family='Helvetica', size=15, weight='bold')
L_TITLE = ttk.Label(frame, text="Bandeiras Aleatórias V0.1", font=title_font)
L_TITLE.grid(column=1,row=0)
#end

#images-labels
imgobj = PhotoImage(file='VS_Code_GitHub\Imagens\_frutas\_botoes\cross-cancel_PNG.png')


IMAGE1 = ttk.Label(frame, text="band1")
IMAGE1['image'] = imgobj
IMAGE1.grid(column=0,row=1)

IMAGE2 = ttk.Label(frame, text="band2")
IMAGE2['image'] = imgobj
IMAGE2.grid(column=1,row=1)

IMAGE3 = ttk.Label(frame, text="band3")
IMAGE3['image'] = imgobj
IMAGE3.grid(column=2,row=1)
#end

#image-labels
ttk.Label(frame, text="Bandeira 1").grid(column=0,row=3)
ttk.Label(frame, text="Bandeira 2").grid(column=1,row=3)
ttk.Label(frame, text="Bandeira 3").grid(column=2,row=3)
#end

#button-sortear
SORTEAR = ttk.Button(frame, text="Sortear", command=sort)
SORTEAR.grid(column=1,row=4,pady=10)
#end

#credits and quit button
ttk.Button(frame, text="Créditos",command=credits).grid(column=0,row=4,sticky=W)
ttk.Button(frame, text="Quit",command=quit).grid(column=2,row=4,sticky=E)
#end



window.mainloop()#"inicializa" a interface gráfica


