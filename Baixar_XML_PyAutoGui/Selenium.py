from selenium import webdriver
import time
import pyautogui as p

navegador = webdriver.Chrome()
navegador.get('https://ananet.sgp.net.br/accounts/central/login')

navegador.find_element_by_xpath('//*[@id="cpfcnpj"]').send_keys('cpf')
navegador.find_element_by_xpath('/html/body/div/div/div/div/div/form/button').click()
p.press('f11')
time.sleep(5)
p.press('f11')
time.sleep(5)
navegador.close()


