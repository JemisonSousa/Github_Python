from selenium import webdriver
import time
import pyautogui as pg

navegador = navegador = webdriver.Chrome()


def avancar_3x():
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')

def avancar_7x():
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')

def avancar_8x():
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')

def voltar_data_inicial():
    pg.hotkey("shift", "tab")
    pg.hotkey("shift", "tab")
    pg.hotkey("shift", "tab")
    pg.hotkey("shift", "tab")

def voltar_destinatario():
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)


def mudar_tipo_para_NFE():
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.press('tab')
    pg.press('up')
    pg.press('up')
    pg.press('enter')

def mudar_tipo_para_NFC_E():
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.press('tab')
    pg.press('down')
    pg.press('down')
    pg.press('enter')
           
pg.PAUSE = 0.3
pg.FAILSAFE = False

# Abrindo o EDGE
pg.press("winleft")
pg.write("edge")
pg.press("enter")
time.sleep(2)
pg.hotkey('ctrl', 'l')
# pg.write("https://www2.agencianet.fazenda.df.gov.br/Inicio/Restrita#/")
pg.write('http://www2.agencianet.fazenda.df.gov.br/')
pg.press("enter")
time.sleep(5)
pg.press("f11")
time.sleep(2)

# Abrindo a parte de XML
pg.moveTo(x=153, y=170)             #clicando em "SERVIÇOS"
pg.click()
pg.sleep(2)
pg.moveTo(x=50, y=481)              #clicando em "OUTROS"
pg.click()  
pg.sleep(2)
pg.moveTo(x=413, y=391)             #clicando em "Chaves de acesso"
pg.click()
pg.sleep(7)                       


# Copiando o CNPJ
# pg.moveTo(x=753, y=199)             #seleciona o começo do CNPJ
# pg.mouseDown()                      #clica e segura botão esquerdo do mouse
# pg.moveTo(x=859, y=199)             #vai para o fim do CNPJ         
# pg.mouseUp()                        #solta o botão esquerdo
# pg.hotkey("ctrl", "c")              #copia o conteúdo

# Colando o CNPJ no campo CNPJ
pg.moveTo(190, 309)             #Vai para o campo CNPJ
pg.click()
# pg.hotkey("ctrl", "v")              #Cola o CNPJ no campo
pg.write('  ')  


class Ano_2019():
    
                                       # JAN - FEB
    #  NFC-E - Emitente
    pg.press('tab')
    pg.press('space')
    pg.press('down')
    pg.press('down')
    pg.press('enter')
    avancar_3x()
    pg.write("01012019")
    pg.press('tab')
    pg.write("28022019")
    avancar_3x()
    pg.press('enter')
    time.sleep(3)

    #  NFC-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')
    time.sleep(5)

    #  NF-E - Emitente
    mudar_tipo_para_NFE()
    time.sleep(1)
    avancar_7x()
    pg.press('enter')
    time.sleep(1)

#  NF-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')

                                       # MAR - ABR
    #  NFC-E - Emitente
    time.sleep(3)
    mudar_tipo_para_NFC_E()
    avancar_3x()
    pg.write("01032019")
    pg.press('tab')
    pg.write("30042019")
    avancar_3x()
    pg.press('enter')
    time.sleep(3)

    #  NFC-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')
    time.sleep(5)

    #  NF-E - Emitente
    mudar_tipo_para_NFE()
    time.sleep(1)
    avancar_7x()
    pg.press('enter')
    time.sleep(1)

    #  NF-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')

                                       # MAI - JUN
    #  NFC-E - Emitente
    time.sleep(3)
    mudar_tipo_para_NFC_E()
    avancar_3x()
    pg.write("01052019")
    pg.press('tab')
    pg.write("30062019")
    avancar_3x()
    pg.press('enter')
    time.sleep(3)

    #  NFC-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')
    time.sleep(5)

    #  NF-E - Emitente
    mudar_tipo_para_NFE()
    time.sleep(1)
    avancar_7x()
    pg.press('enter'    )
    time.sleep(1)

    #  NF-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')

                                   # JUL - AGO
    #  NFC-E - Emitente
    time.sleep(3)
    mudar_tipo_para_NFC_E()
    avancar_3x()
    pg.write("01072019")
    pg.press('tab')
    pg.write("31082019")
    avancar_3x()
    pg.press('enter')
    time.sleep(3)

    #  NFC-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')
    time.sleep(5)

    #  NF-E - Emitente
    mudar_tipo_para_NFE()
    time.sleep(1)
    avancar_7x()
    pg.press('enter'    )
    time.sleep(1)

    #  NF-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')

                                      # SET - OUT
    #  NFC-E - Emitente
    time.sleep(3)
    mudar_tipo_para_NFC_E()
    avancar_3x()
    pg.write("01092019")
    pg.press('tab')
    pg.write("31102019")
    avancar_3x()
    pg.press('enter')
    time.sleep(3)

    #  NFC-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')
    time.sleep(5)

    #  NF-E - Emitente
    mudar_tipo_para_NFE()
    time.sleep(1)
    avancar_7x()
    pg.press('enter'    )
    time.sleep(1)

    #  NF-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')

                                  # NOV - DEZ
    #  NFC-E - Emitente
    time.sleep(3)
    mudar_tipo_para_NFC_E()
    avancar_3x()
    pg.write("01112019")
    pg.press('tab')
    pg.write("31122019")
    avancar_3x()
    pg.press('enter')
    time.sleep(3)

    #  NFC-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')
    time.sleep(5)

    #  NF-E - Emitente
    mudar_tipo_para_NFE()
    time.sleep(1)
    avancar_7x()
    pg.press('enter'    )
    time.sleep(1)

    #  NF-E - Destinatário
    voltar_destinatario()
    avancar_8x()
    pg.press('enter')


'''

class BaixarItens():
    # baixando item 1
    pg.moveTo(1277, 295)
    pg.click()
    pg.moveTo(1119, 109)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')

    # baixando item 2
    pg.moveTo(1276, 366)
    pg.click()
    pg.moveTo(1119, 109)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')

    # baixando item 3
    pg.moveTo(1276, 432)
    pg.click()
    pg.moveTo(1119, 109)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')
    
    # baixando item 4
    pg.moveTo(1275, 566)
    pg.click()
    pg.moveTo(1119, 109)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')

    # baixando item 5
    pg.moveTo(1277, 570)
    pg.click()
    pg.moveTo(1119, 109)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')

    # baixando item 6
    pg.moveTo(1279, 633)
    pg.click()
    pg.moveTo(1119, 109)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')

class ApagarItens():
    vezes = 5
    cont = 0
    while (cont != vezes):
        pg.moveTo(1252, 292)
        pg.click()
        time.sleep(2)
        cont += 1
'''
