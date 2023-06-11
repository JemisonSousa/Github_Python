from tkinter import *

class MudarLinhaColuna():
    def __init__(self, linhas=0, colunas=0):
        self.linhas = linhas
        self.colunas = colunas
    def mudarLinha(self, a):
        self.linhas = a
    def mudarColuna(self, b):
        self.colunas = b
    
def adicionarNome():  #Função não funciona direito, ela add as label em cima da outras, cada vez que é clicado
    nome = entry.get()
    nova_label = Label(root, text=nome)
    nova_label.grid(row=MudarLinhaColuna.self.linha+1, column=0)

root = Tk()
root.title("Adicionando label por função")
root.geometry("500x300")

label = Label(root, text="Digite o nome a ser adicionado: ")
entry = Entry(root)
botao = Button(root, text="Adicionar", command=adicionarNome)

#não dando certo fazer as linhas/colunas serem dinamicas
label.grid(MudarLinhaColuna.self.linhas, column=MudarLinhaColuna.self.colunas)
entry.grid(MudarLinhaColuna.self.linhas, column=MudarLinhaColuna.self.linhas+1)
botao.grid(MudarLinhaColuna.self.linhas, column=MudarLinhaColuna.self.linhas+2)

root.mainloop()