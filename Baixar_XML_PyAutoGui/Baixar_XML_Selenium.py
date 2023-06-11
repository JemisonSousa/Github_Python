from selenium import webdriver
import time
import pyautogui as p

navegador = webdriver.Chrome()
navegador.get('http://www2.agencianet.fazenda.df.gov.br/')


time.sleep(1)
varUM = navegador.find_element_by_xpath('//*[@id="boxMainMenu"]/ul/li[2]/a').text
navegador.find_element_by_xpath('//*[@id="boxMainMenu"]/ul/li[2]/a').click()

time.sleep(5)
varDOIS = navegador.find_element_by_xpath('//*[@id="coluna1"]/ul/li[9]/a').text
navegador.find_element_by_xpath('//*[@id="coluna1"]/ul/li[9]/a').click()

time.sleep(2)
varTRES = navegador.find_element_by_xpath('//*[@id="coluna2"]/ul/li[5]/span/a/span[1]').text
navegador.find_element_by_xpath('//*[@id="coluna2"]/ul/li[5]/span/a/span[1]').click()

time.sleep(2)
navegador.find_element_by_xpath('//*[@id="CpfCnpj"]').send_keys('02810540000166')

time.sleep(2)
navegador.find_element_by_xpath('//*[@id="DataInicio"]').send_keys('01012020') #01/01/2020

time.sleep(2)
navegador.find_element_by_xpath('//*[@id="DataFim"]').send_keys('01012020') #28/02/2020

time.sleep(2)
navegador.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div/div[2]/form/div[7]/div/button[2]').click()



print('---')
print(varUM)
print(varDOIS)
print(varTRES)
print('---')
