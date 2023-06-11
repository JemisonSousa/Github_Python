import time, tkinter
from tkinter import Entry, Label, Tk, ttk
import pyautogui as p

p.PAUSE = 0.2
p.FAILSAFE = False
cnpj = " "

class Avancar:
    def x3():
        p.press('tab')
        p.press('tab')
        p.press('tab')

    def x4():
        p.press('tab')
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
    p.press('tab')
    time.sleep(1)


def mudar_tipo_para_NFE():
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.press('tab')
    p.press('up')
    p.press('up')
    p.press('enter')

def mudar_tipo_para_NFC_E():
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.hotkey('shift', 'tab')
    p.press('tab')
    p.press('down')
    p.press('down')
    p.press('enter')


class Principal:
    def __init__(self):
        # Abrindo o EDGE
        p.press("winleft")
        p.write("chrome")
        p.press("enter")
        time.sleep(1)
        p.hotkey('ctrl', 'l')
        p.write('http://www2.agencianet.fazenda.df.gov.br/')
        p.press("enter")
        time.sleep(1)
        p.press("f11")
        Avancar.x10()
        p.press('enter')
        time.sleep(1)

        Avancar.x4()
        p.press('enter')

        p.moveTo(50, 476)
        p.click()
        Avancar.x5()
        p.press('enter')
        Avancar.x20()
        p.write(cnpj)
        p.press('tab'); p.press('space'); p.press('down'); p.press('down'); p.press('enter')
        Avancar.x3
        p.write('01012020')
        p.press('tab')
        p.write('29022020')
        Avancar.x3
        p.press('enter')











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
