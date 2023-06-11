from selenium import webdriver
import time

navegador = webdriver.Chrome()
# navegador = webdriver.Edge()

# navegador.get('https://casadosdados.com.br/')
navegador.get('https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada')
navegador.find_element_by_xpath('//*[@id="navbarBasicExample"]/div/a[2]').click()
navegador.find_element_by_xpath('//*[@id="navbarBasicExample"]/div/a[2]')
# navegador.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/section/div[3]/div[2]/div/div/div/div/div[2]/div/a[1]').click()
# navegador.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/section/div[3]/div[2]/div/div/div/div/div[1]/input').send_keys('D')




