from tkinter import Entry, Label, Tk, ttk

class Janela():
    root = Tk()
    root.title("XML Downloader")
    root.iconbitmap("Ico-Fig-doc\Icon001.ico")
    root.geometry("390x200")

    Texto_1 = Label(root, text="Programa baixador dos XML dos anos 2017 a 2021\n Program em construção ainda", font=(6)).pack()
    
    Texto_2 = Label(root, text="Insira o CNPJ (sem pontos)").pack(pady=10)

    cnpj = Entry(root)
    cnpj.pack(ipadx=2, ipady=2, padx=10, pady=10)

    btn_baixar = ttk.Button(root, text="Baixar", command=None).pack(side='left', padx=50)
    btn_fechar = ttk.Button(root, text="Fechar", command=root.quit).pack(side='right', padx=50)

    root.mainloop()