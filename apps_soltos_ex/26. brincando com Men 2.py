from tkinter import *
from tkinter import messagebox, ttk
from tkinter import font


class DesenharBandeiraFranca:
    def __init__(self):
        self.janela1 = Tk()
        self.frame1 = Frame(self.janela1, bg="blue", height=200, width=80)
        self.frame2 = Frame(self.janela1, bg='white', height=200, width=80)
        self.frame3 = Frame(self.janela1, bg='red', height=200, width=80)
        self.frame1.pack(side="left")
        self.frame2.pack(side="left")
        self.frame3.pack(side="left")
        mainloop()

class DesenharBandeiraHolanda:
    def __init__(self):
        self.janela2 = Tk()
        self.fram1 = Frame(self.janela2, bg="red", height=80, width=200)
        self.fram2 = Frame(self.janela2, bg='white', height=80, width=200)
        self.fram3 = Frame(self.janela2, bg='blue', height=80, width=200)
        self.fram1.pack(side="top")
        self.fram2.pack(side="top")
        self.fram3.pack(side="top")
        mainloop()


root = Tk()
root.title("Menus")
largura = 500
altura = 300
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posicao_x = largura_screen/2 - largura/2
posicao_y = altura_screen/2 - altura/2
root.geometry("%dx%d+%d+%d" % (500, 300, ((root.winfo_screenwidth())/2 - 500/2), ((root.winfo_screenheight())/2 - 300/2)))
#root.iconbitmap("Imagens\_frutas\Alex-T-Minimal-Fruit-Pear.ico")
root.configure(background="#F0F8FF")

def testar_algo():
    print("Aqui printou o comando 'NOVO'")

def menu_sobre():
    print("A versão do Programa é a Beta 0.0.01")
    messagebox.showinfo("Versão", "A versão do Programa é a Beta 0.0.01")


meuMenu = Menu(root, background="#F0F8FF")

# Menu Arquivo 
menuArquivo = Menu(meuMenu, tearoff=0, background="#F0F8FF")
menuArquivo.add_command(label="Novo", command=testar_algo)
menuArquivo.add_command(label="Abrir", command=DesenharBandeiraFranca)
menuArquivo.add_command(label="Salvar", command=DesenharBandeiraHolanda)
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=root.quit)
meuMenu.add_cascade(label="Arquivo", menu=menuArquivo)

# Menu Editar
menuEditar = Menu(meuMenu, tearoff=0, background="#F0F8FF")
menuEditar.add_command(label="Copiar")
menuEditar.add_command(label="Colar")
menuEditar.add_command(label="Selecionar tudo")
meuMenu.add_cascade(label="Editar", menu=menuEditar)

# Menu Exibir
menuExibir = Menu(meuMenu, tearoff=0, background="#F0F8FF")
menuExibir.add_command(label="Pesquisar")
menuExibir.add_command(label="Aparência")
menuExibir.add_command(label="Executar")
meuMenu.add_cascade(label="Exibir", menu=menuExibir)

# Menu Sobre
menuSobre = Menu(meuMenu, tearoff=0, background="#F0F8FF")
menuSobre.add_command(label="Versão", command=menu_sobre)
menuSobre.add_separator()
menuSobre.add_command(label="Verificar Atualização")
meuMenu.add_cascade(label="Sobre", menu=menuSobre)

root.config(menu=meuMenu)

# CONTEUDO

# Frames
frame_1 = Frame(root, background="gold"); frame_1.grid(row=0, column=0)
frame_2 = Frame(root, background="gold"); frame_2.grid(row=0, column=1)
frame_3 = Frame(root, background="gold", highlightbackground="red", highlightcolor="red", highlightthickness=2, width=500, height=400); frame_3.grid(row=1, column=0)
frame_4 = Frame(root, background="gold"); frame_4.grid(row=2, column=0)

# Frame 1
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

# Frame 2
frame_2 = Frame(root, background="silver", padx=5, pady=5)
frame_2.grid(row=0, column=1, sticky=E)

'''
photo = PhotoImage(file="Imagens\_frutas\Apple-icon.png")
imgLabel = Label(frame_2, image=photo)
imgLabel.grid(row=0, column=0)'''

# Frame 3
label_5 = Label(frame_3, text="Aqui vai ficar os dados", font="Arial, 15")
label_5.grid(row=0, column=0)
label_5 = Label(frame_3, text="Aqui vai ficar os dados", font="Arial, 15")
label_5.grid(row=1, column=0)
label_5 = Label(frame_3, text="Aqui vai ficar os dados", font="Arial, 18")
label_5.grid(row=2, column=0)


# Frame 4
btn_exit = Button(root, text="SAIR", command=root.quit)
btn_exit.grid(row=4, columnspan=2)


root.mainloop()