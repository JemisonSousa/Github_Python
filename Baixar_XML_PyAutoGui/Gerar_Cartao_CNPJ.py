from selenium import webdriver
import time
import pyautogui as p

cnpj = ' '

navegador = webdriver.Chrome()
navegador.get('https://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp')

# navegador.find_element_by_xpath('//*[@id="cnpj"]').send_keys('cnpj')
# navegador.find_element_by_xpath('//*[@id="checkbox"]').click()
# navegador.find_element_by_xpath('//*[@id="frmConsulta"]/div[3]/div/button[1]').click()
# navegador.find_element_by_xpath('//*[@id="print"]').click()
# navegador.find_element_by_xpath('/html/body/center/a/img').click()
# time.sleep(2)
# p.press('enter')
# time.sleep(2)
# p.press('enter')

p.press('tab')
time.sleep(2)
p.press('tab')
time.sleep(2)
p.press('tab')
time.sleep(2)
p.press('tab')
time.sleep(2)
p.write('02810540000166')
p.press('tab')
p.press('enter')
p.press('tab')
time.sleep(2)
p.press('tab')
time.sleep(2)
p.press('tab')
time.sleep(2)
p.press('tab')
time.sleep(2)
p.press('enter')



# navegador.close()