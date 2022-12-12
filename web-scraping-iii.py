import requests #fazer a requisicao ao site
from bs4 import BeautifulSoup #pegar o resultado em html e converte-lo em um objeto do bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.add_argument('window-size=400,800')
navegador = webdriver.Firefox(options=options)

url = 'https://lista.mercadolivre.com.br/'
navegador.get(url)
sleep(3)
input_place = navegador.find_element(By.TAG_NAME,  'input')
input_place.send_keys('Caneta')
input_place.submit()


site = BeautifulSoup(navegador.page_source, 'html.parser')
print(site.prettify())