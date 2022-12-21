import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

product_info_list = []

#configura o navegador
options = Options()
options.add_argument('window-size=400,800')
navegador = webdriver.Firefox(options=options)

#pega o conteúdo da página inicial
url = 'https://lista.mercadolivre.com.br/'
navegador.get(url)
sleep(3)

#busca
input_place = navegador.find_element(By.TAG_NAME,  'input')
busca = str(input('O que você quer procurar? '))
input_place.send_keys(busca)
input_place.submit()
sleep(3)

raw_content = navegador.page_source
html_content = BeautifulSoup(raw_content, 'html.parser')
#busca info de todos os produtos da página atual
product_info = html_content.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default andes-card--animated'})

while True:
    for i in product_info: #pra cada info/produto dentro de product_info:
        nome = i.find('div', attrs={'class': 'ui-search-item__group ui-search-item__group--title shops__items-group'})
        cifra = i.find('span', attrs={'class': 'price-tag-symbol'})
        reais = i.find('span', attrs={'class': 'price-tag-fraction'})
        centavos = i.find('span', attrs={'class': 'price-tag-cents'})
        if (centavos):
            preço = cifra.text+reais.text+','+centavos.text
        else:
            preço = cifra.text+reais.text
        link = i.find('a', attrs={'class': 'ui-search-result__content ui-search-link'})
        
        product_info_list.append([nome.text, preço, link['href']])
        product_info_df = pd.DataFrame(product_info_list, columns=['Nome', 'Preço', 'Link'])
        print(product_info_df)
        product_info_df.to_excel('Produtos-do-ML.xlsx', index=False)

    continuar = str(input('Continuar? [S/N]')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida. Informe se deseja continuar [S/N]: '))
    if continuar in 'N':
        break
    
    #esconde o banner de cookies
    cookie_banner = navegador.find_element(By.CLASS_NAME, 'cookie-consent-banner-opt-out')
    navegador.execute_script("arguments[0].style.visibility='hidden'", cookie_banner)

    #procura e clica no botão next
    next_button = navegador.find_element(By.CLASS_NAME,'andes-pagination__arrow-title')
    next_button.click()
    sleep(3)