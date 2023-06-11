from selenium import webdriver
import time
import pyautogui as p

navegador = webdriver.Chrome()
navegador.get('http://consultatributos.com.br/tributacao/')

time.sleep(1)
navegador.find_element_by_xpath('//*[@id="email_login"]').send_keys('...........')
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="senha_login"]').send_keys('........')
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="login_button"]').click()              #botão OK
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="busca_estado"]/option[8]').click()    #Estado 
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="campo_Busca"]/option[3]').click()     #Campo NCM
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="buscar"]').send_keys('33011990')      #Campo inserir NCM
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="btn_buscar"]/button').click()         #Pesquisar
time.sleep(1)

navegador.find_element_by_xpath('//*[@id="busca_estado"]/option[1]').click()    #Estado DF
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="btn_buscar"]/button').click()         #Pesquisar

# uf = navegador.find_element_by_xpath('//*[@id="linha7898907333931"]/td[1]/span').text
# codigo = navegador.find_element_by_xpath('//*[@id="linha7898907333931"]/td[2]/span').text
# tabela = navegador.find_element_by_xpath('//*[@id="linha7898907333931"]').text
# print(uf)
# print(codigo)
# print(tabela)

# Descricao
# NCM
# CEST
# CST_PIS_COFINS_Entrada
# CST_PIS_COFINS_Saída
# Natureza_Receita_Isenta
# Cód_ANP
# Aliq_IPI
# CST_ICMS
# Aliq_ICMS
# Aliq_ICMS_PDV_Reduzida
# IVA
# Red_BC_ICMS
# Isento_ICMS
# FCP
# Cód_Benef
# ICMS_Anteci
# ICMS_Desone
# Difer


