
import tkinter as tk
from tkinter import messagebox

def main(args):
	root = tk.Tk()

	btn= tk.Button(root, text ="Click aqui", command = nada)
	btn.place(bordermode=tk.OUTSIDE, height=100, width=100)

	btn1= tk.Button(root, text ="Ou Click aqui", command = processaBtn1)
	btn1.place(bordermode=tk.OUTSIDE, height=100, width=100,x=100, y=100)

	root.mainloop()

	return 0

a = "Erro de execução"
b = "Erro de entrada"

def processaBtn():
   messagebox.showinfo( "OLá", "Você pressionou o botão certo!")
def nada():
   messagebox.showinfo( "ERRO", a)




def processaBtn1():
   messagebox.showinfo( "Ops!!!", "Você pressionou o botão errado!")

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))