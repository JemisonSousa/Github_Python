from tkinter import *
from PIL import Image, ImageTk
from time import sleep
import random, os
os.system("cls")

num_usuario = ""
num_chutado = random.randint(0, 1000)
tentativas = 0

root = Tk()
root.title("Jogo do número aleatório")
largura = 350
altura = 400
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posicao_x = largura_screen/2 - largura/2
posicao_y = altura_screen/2 - altura/2
root.geometry("%dx%d+%d+%d" % (largura, altura, ((root.winfo_screenwidth())/2 - largura/2), ((root.winfo_screenheight())/2 - altura/2)))
root.iconbitmap("Ico-Fig-doc\Trevo_ICO.ico")
root.resizable(width=False, height=False)
# root.configure(background="#F0F8FF")

def pegarNum():
    global num_usuario
    global num_chutado
    global tentativas
    num_usuario = int(entry.get())
    while num_chutado != num_usuario:
        num_chutado = random.randint(0, 100)
        tentativas += 1
    print(num_chutado)
    print(num_usuario)


# FRAME imagem
frame_image = Frame(root)
frame_image.pack()

# imagem_Trevo = PhotoImage(file="Imagens\_frutas\pear-icon.png")
# label_imagem = Label(frame_image, image=imagem_Trevo)
# label_imagem.pack()

image = Image.open("Ico-Fig-doc\Trevo_PNG.png")
img = image.resize((150, 150))
my_img = ImageTk.PhotoImage(img)
label = Label(root, image=my_img)
label.pack()

# FRAME conteudo
frame_conteudo = Frame(root);
frame_conteudo.pack()

label_Texto = Label(frame_conteudo, text="JOGO DO NÚMERO ALEATÓRIO", font="Impact 17")
label_Texto.pack()

label_Descricao = Label(frame_conteudo, text="Digite um número entre 0 e 1000 e a máquina tentará acertar")
label_Descricao.pack()

entry = Entry(frame_conteudo, width=5)
entry.pack(padx=5, pady=5, ipadx=3, ipady=3)

def jogar():
    pass

btn_jogar = Button(frame_conteudo, text="JOGAR", padx=5, pady=5, background="#90EE90", command=pegarNum)
btn_jogar.pack(padx=10, pady=10)

# Fazendo a lógica do jogo

num = 222
msg = StringVar()
msg.set(f"A máquina acertou o número {num} em Y tentativas. {num_usuario}")
label_resultado = Label(frame_conteudo, textvariable=msg)
label_resultado.pack(padx=20, pady=20)







btn_sair = Button(frame_conteudo, text="SAIR", padx=5, pady=5, background="#FA8072", command=root.quit)
btn_sair.pack()

root.mainloop()