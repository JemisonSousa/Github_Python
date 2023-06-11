from tkinter import Entry, Label, Tk, ttk
import pyautogui as p
import time

p.PAUSE = 0.2
p.FAILSAFE = False
cnpj = "    "

class Avancar:
    def x3():
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x5():
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x7():
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x8():
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')                                          
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x10():
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x12():
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x20():
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')
        p.press('tab')

class Mudar_para_NFCE:
    p.press('tab')
    p.press('space')
    p.press('down')
    p.press('down')
    p.press('enter')

class Mudar_para_NFE:
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.press('space')
    p.press('up')
    p.press('up')
    p.press('enter')

def voltar_data_inicial():
    p.hotkey("shift", "tab")
    p.hotkey("shift", "tab")
    p.hotkey("shift", "tab")
    p.hotkey("shift", "tab")

def voltar_destinatario():
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    time.sleep(1)
    p.press('space')
    time.sleep(1)

class Principal:
    def __init__(self):
        p.hotkey('alt', 'tab')
        time.sleep(1)
        p.press("f11")   
        time.sleep(2)
        p.moveTo(143, 168, 1)   #serviçoshy
        p.click()
        time.sleep(1)
        p.moveTo(53, 477, 1)    #outros
        p.click()
        time.sleep(1)
        p.moveTo(454, 393, 1)   #chave XML
        p.click()

        time.sleep(6)
        p.moveTo(191, 308, 1)   #campo CNPJ
        p.click()
        p.write(cnpj)

        Mudar_para_NFCE
        Avancar.x3()

        p.write('01012020')     #JANEIRO
        p.press('tab')
        p.write('29022020')     #FEVEREIRO

        Avancar.x3()
        p.press('enter')
        time.sleep(2)

        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        Mudar_para_NFE

        Avancar.x7()
        p.press('enter')
        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        # mudando para o próximo mes
        Mudar_para_NFCE
        Avancar.x3()

        p.write('01032020')     #MARÇO
        p.press('tab')
        p.write('30042020')     #ABRIL

        Avancar.x3()
        p.press('enter')
        time.sleep(2)

        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        Mudar_para_NFE

        Avancar.x7()
        p.press('enter')
        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        # mudando para o próximo mes
        Mudar_para_NFCE
        Avancar.x3()

        p.write('01052020')     #MAIO
        p.press('tab')
        p.write('30062020')     #JUNHO

        Avancar.x3()
        p.press('enter')
        time.sleep(2)

        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        Mudar_para_NFE

        Avancar.x7()
        p.press('enter')
        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        # mudando para o próximo mes
        Mudar_para_NFCE
        Avancar.x3()

        p.write('01072020')     #JULHO
        p.press('tab')
        p.write('31082020')     #AGOSTO

        Avancar.x3()
        p.press('enter')
        time.sleep(2)

        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        Mudar_para_NFE

        Avancar.x7()
        p.press('enter')
        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        # mudando para o próximo mes
        Mudar_para_NFCE
        Avancar.x3()

        p.write('01092020')     #SETEMBRO
        p.press('tab')
        p.write('31102020')     #OUTRUBRO

        Avancar.x3()
        p.press('enter')
        time.sleep(2)

        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        Mudar_para_NFE

        Avancar.x7()
        p.press('enter')
        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        # mudando para o próximo mes
        Mudar_para_NFCE
        Avancar.x3()

        p.write('01112020')     #NOVEMBRO
        p.press('tab')
        p.write('31122020')     #DEZEMBRO

        Avancar.x3()
        p.press('enter')
        time.sleep(2)

        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)

        Mudar_para_NFE

        Avancar.x7()
        p.press('enter')
        voltar_destinatario()
        Avancar.x8()
        p.press('enter')
        time.sleep(2)


     
class Janela:
    root = Tk()
    root.title("XML Downloader")
    root.iconbitmap("Ico-Fig-doc\Icon001.ico")
    root.geometry("390x200")

    Texto_1 = Label(root, text="Programa baixador dos XML dos anos 2017 a 2021\n Program em construção ainda", font=(6)).pack()
    
    Texto_2 = Label(root, text="Insira o CNPJ (sem pontos)").pack(pady=10)

    cnpj = Entry(root)
    cnpj.pack(ipadx=2, ipady=2, padx=10, pady=10)

    btn_baixar = ttk.Button(root, text="Baixar", command=Principal).pack(side='left', padx=50)
    btn_fechar = ttk.Button(root, text="Fechar", command=root.quit).pack(side='right', padx=50)
    
    root.mainloop()
