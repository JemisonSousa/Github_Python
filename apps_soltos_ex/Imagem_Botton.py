from tkinter import *
from tkinter import ttk
import time, sys

# pyinstaller --onefile -w --ico nome.ico Arquivo.py

class Windows:
    def __init__(self):
        self.root = Tk()
        self.root.title('Button em imagem')
        # self.root.iconbitmap('VS_Code_GitHub\Imagens\_frutas\_botoes\jpg_powe_ICO.ico')

        self.root.geometry('400x400+20+500')
        self.root.minsize(380,300)
        
        self.login_btn_ON   = PhotoImage(file='VS_Code_GitHub\Imagens\_frutas\_botoes\_btn_ONOFF_ON.png')
        self.login_btn_OFF  = PhotoImage(file='VS_Code_GitHub\Imagens\_frutas\_botoes\_btn_ONOFF_OFF.png')
        self.login_btn_MEIO = PhotoImage(file='VS_Code_GitHub\Imagens\_frutas\_botoes\_btn_ONOFF_MEIO.png')
        
        self.corFundoTela       =   'gray'
        self.status_FundoTela   =   'black'
        self.status_texto       =   'ligou'             
        self.status_img_btn     =   self.login_btn_ON
        self.status_btn_clicado =   ''



        def comandoBotao():
            # texto
            texto_informativo.config(text='Você ' + self.status_texto, background=self.status_FundoTela, foreground='white')
            if self.status_texto == 'ligou':
                self.status_texto = 'desligou'
            else:
                self.status_texto = 'ligou'

            # imgagem btn
            botao_imagem.config(image=self.status_img_btn, background=self.status_FundoTela)
            if self.status_img_btn == self.login_btn_ON:
                self.status_img_btn = self.login_btn_OFF
            else:
                self.status_img_btn = self.login_btn_ON
            
            # cor do fundo
            self.root.config(background=self.status_FundoTela)
            if self.status_FundoTela == 'black':
                self.status_FundoTela = 'gray'
            else:
                self.status_FundoTela = 'black'
                
            # botão clicado
            # botao_imagem.config(highlightbackground=self.corFundoTela,
            #                     highlightthickness=self.corFundoTela,
            #                     highlightcolor=self.corFundoTela,
            #                     insertbackground=5,
            #                     insertborderwidth=2)









        botao_imagem = Button(self.root,
                              image=self.login_btn_OFF, 
                              borderwidth=0, 
                              background=self.corFundoTela,
                              command=comandoBotao, 
                              )
        botao_imagem.pack(pady=20)

        texto_informativo = Label(self.root, text='Desligado', background='gray', foreground='white')
        texto_informativo.pack(pady=20)
        
        def sair_app():
            sys.exit(0)
            
        btn_exit = ttk.Button(self.root, text='Sair', command=sair_app)
        btn_exit.pack(side='bottom')




        self.root.config(background=self.corFundoTela)  
        mainloop()


Windows()
