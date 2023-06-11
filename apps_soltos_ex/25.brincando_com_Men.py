from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.title("Menus")
largura = 500
altura = 300
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posicao_x = largura_screen/2 - largura/2
posicao_y = altura_screen/2 - altura/2
root.geometry("%dx%d+%d+%d" % (500, 300, ((root.winfo_screenwidth())/2 - 500/2), ((root.winfo_screenheight())/2 - 300/2)))
#root.iconbitmap("VS_Code_GitHub\Exemplos\_bar-graph.ico")
root.configure(background="#BDB76B")


def testar_algo():
    print("Aqui printou o comando 'NOVO'")


def menu_sobre():
    print("A versão do Programa é a Beta 0.0.01")
    messagebox.showinfo("Versão", "A versão do Programa é a Beta 0.0.01")


meuMenu = Menu(root)

# Menu Arquivo 
menuArquivo = Menu(meuMenu, tearoff=0, background="#FFEFD5")
menuArquivo.add_command(label="Novo", command=testar_algo)
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
menuSobre.add_command(label="Versão", command=menu_sobre)
menuSobre.add_separator()
menuSobre.add_command(label="Verificar Atualização")
meuMenu.add_cascade(label="Sobre", menu=menuSobre)

root.config(menu=meuMenu)

# FRAME 0
frame_0 = Frame(root)
frame_0.grid(row=0)

label_0 = Label(frame_0, text="DADOS PESSOAIS", background="#BDB76B", foreground="#FFFAFA")
label_0.grid(row=1, column=0, sticky=E)

# FRAMES 1
frame_1 = Frame(root, background="#B8860B", padx=5, pady=20)
frame_1.grid(row=0, column=0, sticky=E)

label_1 = Label(frame_1, text="Nome:", background="#BDB76B", foreground="#FFFAFA")
label_1.grid(row=0, column=0, sticky=E)

entry_1 = ttk.Entry(frame_1, width=37)
entry_1.grid(row=0, column=1, padx=2, pady=2)

label_2 = Label(frame_1, text="Data de nascimento:", background="#BDB76B", foreground="#FFFAFA")
label_2.grid(row=1, column=0, sticky=E)

entry_2 = ttk.Entry(frame_1, width=37)
entry_2.grid(row=1, column=1, padx=2, pady=2)

label_3 = Label(frame_1, text="Cidade:", background="#BDB76B", foreground="#FFFAFA")
label_3.grid(row=2, column=0, sticky=E)

entry_3 = ttk.Entry(frame_1, width=37)
entry_3.grid(row=2, column=1, padx=2, pady=2)

label_4 = Label(frame_1, text="Estado:", background="#BDB76B", foreground="#FFFAFA")
label_4.grid(row=3, column=0, sticky=E)

entry_4 = ttk.Entry(frame_1, width=37)
entry_4.grid(row=3, column=1, padx=2, pady=2)

# FRAMES 2
frame_2 = Frame(root, background="silver", padx=5, pady=5)
frame_2.grid(row=0, column=1, sticky=E)

'''
photo = PhotoImage(file=".\Imagens\Ico-Fig-doc\Trevo_PNG(2).png")
imgLabel = Label(frame_2, image=photo)
imgLabel.grid(row=0, column=0)'''


btn_exit = Button(root, text="SAIR", command=root.quit)
btn_exit.grid(row=4, columnspan=2)

root.mainloop()