import time, tkinter
from tkinter import Entry, Label, Tk, ttk
import pyautogui as p



class Avancar:
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


class ExecutarPyAutoGUI:
    def __init__(self):
        time.sleep(2)
        p.hotkey('winleft', 'd'); time.sleep(2)
        p.moveTo(752, 746, 2)
        # p.click(); time.sleep(0.5)
        # p.moveTo(1188, 188, 2); time.sleep(0.5)
        # p.click()
        # p.moveTo(599, 236, 2); time.sleep(0.5)
        # p.click()
        # p.moveTo(775, 398, 2); time.sleep(0.5)
        # p.click()
        # time.sleep(5)
        # p.moveTo(156, 276, 2); time.sleep(0.5)
        # p.click()
        # p.moveTo(50, 578, 2); time.sleep(0.5)
        # p.click()
        # p.moveTo(413, 496, 2); time.sleep(0.5)
        # p.click()
        # time.sleep(6)
        # p.moveTo(186, 411, 2); time.sleep(0.5)
        # p.click()
        # p.write('21196222000100', 0.095)      
        # p.moveTo(451, 480, 2); time.sleep(0.5)
        # p.click()
        # p.write('01012017', 0.095)
        # p.moveTo(694, 480, 2); time.sleep(0.5)
        # p.click()
        # p.write('28022017', 0.095)
        # p.moveTo(614, 569, 2); time.sleep(0.5)
        # p.click()







class Janela:
    root = Tk()
    root.title("XML Downloader")
    # root.iconbitmap("Ico-Fig-doc\Icon001.ico")
    root.geometry("390x200")

    Texto_1 = Label(root, text="Programa baixador dos XML dos anos 2017 a 2021\n Program em construção ainda", font=(6)).pack()
    
    Texto_2 = Label(root, text="Insira o CNPJ (sem pontos)").pack(pady=10)

    cnpj = Entry(root)
    cnpj.pack(ipadx=2, ipady=2, padx=10, pady=10)

    btn_baixar = ttk.Button(root, text="Baixar", command=ExecutarPyAutoGUI).pack(side='left', padx=50)
    btn_fechar = ttk.Button(root, text="Fechar", command=root.quit).pack(side='right', padx=50)

    root.mainloop()

