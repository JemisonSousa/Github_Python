from tkinter import *
from tkinter import ttk, messagebox
from random import randint

def gerarNumeros(numJogos, numMin, numMax):
    qtd_num = numJogos
    num_min = numMin
    num_max = numMax
    lista = []
    i = 0
    '''while i < qtd_num:
        n = randint(num_min, num_max)          
        if n in lista:
            n = randint(num_min, num_max)
            lista.append(n)
        else:
            lista.append(n)
        i += 1
    return sorted(lista)'''
    
    while i < qtd_num:
        n = randint(num_min, num_max)
        while n in lista:
            n = randint(num_min, num_max)
        lista.append(n)
        i += 1
    return sorted(lista)              


class MontarFrame:
    def megaSena():
        
        def gerar():
            texto.delete(1.0, END)
            lista = gerarNumeros(int(combobox_megasena.get()), 1, 60)
            texto.insert(END, lista)
        
        frame_mega = LabelFrame(app, text="MEGA-SENA", width=377, height=305, background="#FFDAB9", font="arial 10 bold")
        frame_mega.place(x=10, y=160)
        
        label_mega = Label(frame_mega, text="Escolha a quantidade de números:", background="#FFDAB9")
        label_mega.place(x=1, y=0)
        
        combobox_megasena = ttk.Combobox(frame_mega, values=[6, 7, 8, 9], width=3)
        combobox_megasena.place(x=200, y=0)
        combobox_megasena.set(6)
                
        btn_gerar = Button(frame_mega, text="GERAR", width=8, font="Arial 10 bold", command=gerar)
        btn_gerar.place(x=150, y=60)
        
        texto = Text(frame_mega, width=24, height=2, font="Arial 20 bold")     
        texto.place(x=4, y=120)
            
            
    def lotofacil():
            
        def gerar():
            texto.delete(1.0, END)
            lista= gerarNumeros(int(combobox_lotofacil.get()), 1, 25)
            texto.insert(END, lista)
        
        frame_lotofacil = LabelFrame(app, text="LOTOFÁCIL", width=377, height=305, background="#FFDAB9", font="arial 10 bold")
        frame_lotofacil.place(x=10, y=160)
        
        label_lotofacil = Label(frame_lotofacil, text="Escolha a quantidade de números:", background="#FFDAB9")
        label_lotofacil.place(x=1, y=0)
        
        combobox_lotofacil = ttk.Combobox(frame_lotofacil, values=[15, 16, 17, 18], width=3)
        combobox_lotofacil.place(x=200, y=0)
        combobox_lotofacil.set(15)
        
        btn_gerar = Button(frame_lotofacil, text="GERAR", width=8, font="Arial 10 bold", command=gerar)
        btn_gerar.place(x=150, y=60)
        
        texto = Text(frame_lotofacil, width=27, height=2, font="Arial 18 bold")     
        texto.place(x=4, y=120)


    def lotomania():

        def gerar():
            texto.delete(1.0, END)
            lista = gerarNumeros(int(combobox_lotomania.get()), 0, 99)
            texto.insert(END, lista)
        
        frame_lotomania = LabelFrame(app, text="LOTOMANIA", width=377, height=305, background="#FFDAB9", font="arial 10 bold")
        frame_lotomania.place(x=10, y=160)
        
        label_lotomania = Label(frame_lotomania, text="Escolha a quantidade de números:", background="#FFDAB9")
        label_lotomania.place(x=1, y=0)
        
        combobox_lotomania = ttk.Combobox(frame_lotomania, values=[50], width=3)
        combobox_lotomania.place(x=200, y=0)
        combobox_lotomania.set(50)
        
        btn_gerar = Button(frame_lotomania, text="GERAR", width=9, font="Arial 10 bold", command=gerar)
        btn_gerar.place(x=150, y=60)
        
        texto = Text(frame_lotomania, width=40, height=4, font="Arial 12 bold")     
        texto.place(x=4, y=110)
    


app = Tk()
app.title("JOGO LOTERIAS")
app.geometry("400x500+600+300")
app.resizable(False, False)
app.configure(bg="#FFDAB9")

icon = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Loteria\\ico-trevo.png")
app.iconphoto(True, icon)

top_frame = Frame(app, bg="white", width=400, height=110)
top_frame.place(x=0, y=0)

logo = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Loteria\\Logo-Loterias.png")
Label(top_frame, image=logo, bg="white").place(x=95, y=5)

logo_megaSena = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\Projetos\\Loteria\MegaSena.png")
btn_MegaSena = Button(app, text="MEGA-SENA", image=logo_megaSena, command=MontarFrame.megaSena)
btn_MegaSena.place(x=10, y=120)

logo_lotofacil = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Loteria\\lotofacil.png")
btn_Lotofacil = Button(app, text="LOTOFÁCIL", image=logo_lotofacil, command=MontarFrame.lotofacil)
btn_Lotofacil.place(x=145, y=120)

logo_lotomania = PhotoImage(file="C:\\Users\\jemis\\Documents\\Python Scripts\\VS_Code_GitHub\\PYTHON\\Projetos\\Loteria\\Lotominia.png")
btn_Lotomania = Button(app, text="LOTOFÁCIL", image=logo_lotomania, command=MontarFrame.lotomania)
btn_Lotomania.place(x=280, y=120)

label_noticia_escolha_jogo = Label(app, text="Escolha o jogo acima", background="#FFDAB9")
label_noticia_escolha_jogo.place(x=135, y=290)

def sair():
    messagebox.askokcancel(title="Sair do programa", message="Você está tentando sair do programa?")

btn_Sair = Button(app, text=" SAIR ", bg="#191970", fg="white", command=sair)
btn_Sair.place(x=155, y=470)

def sobre():
    messagebox.showinfo("Sobre o programa", "Programa feito para testar a lógica de programação.\nSei que tudo isso é feito Online.\n\nFeito por Jemison Sousa \o/")

btn_sobre = Button(app, text=" Sobre ", bg="#F5DEB3", fg="black", command=sobre)
btn_sobre.place(x=205, y=470)

app.update()
app.mainloop()