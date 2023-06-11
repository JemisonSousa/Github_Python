from tkinter import *

root = Tk()
root.title("Menus")
root.iconbitmap("Imagens\_frutas\Alex-T-Minimal-Fruit-Pear.ico")

meuMenu = Menu(root)

# Menu Arquivo 
menuArquivo = Menu(meuMenu, tearoff=0, background="#FFEFD5")
menuArquivo.add_command(label="Novo")
menuArquivo.add_command(label="Abrir")
menuArquivo.add_command(label="Salvar")
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=root.quit)
meuMenu.add_cascade(label="Arquivo", menu=menuArquivo)

# Menu Editar
menuEditar = Menu(meuMenu, tearoff=0, background="#FFDAB9")
menuEditar.add_command(label="Copiar")
menuEditar.add_command(label="Colar")
menuEditar.add_command(label="Selecionar tudo")
meuMenu.add_cascade(label="Editar", menu=menuEditar)

# Menu Exibir
menuExibir = Menu(meuMenu, tearoff=0, background="#FFE4B5")
menuExibir.add_command(label="Pesquisar")
menuExibir.add_command(label="Aparência")
menuExibir.add_command(label="Executar")
meuMenu.add_cascade(label="Exibir", menu=menuExibir)

# Menu Sobre
menuSobre = Menu(meuMenu, tearoff=0, background="#FFE4E1")
menuSobre.add_command(label="Versão")
menuSobre.add_separator()
menuSobre.add_command(label="Verificar Atualização")
meuMenu.add_cascade(label="Sobre", menu=menuSobre)

root.config(menu=meuMenu)


root.mainloop()