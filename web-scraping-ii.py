import requests #fazer a requisicao ao site
from bs4 import BeautifulSoup #pegar o resultado em html e converte-lo em um objeto do bs

url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = str(input('Qual produto você deseja procurar? '))
ntot = 0

site = requests.get(url_base + produto_nome) #print(site.text)
site_html = BeautifulSoup(site.text, 'html.parser') #print(site_html.prettify())
produto_info = site_html.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default andes-card--animated'})

for produto in produto_info:
    nome = produto.find('div', attrs={'class': 'ui-search-item__group ui-search-item__group--title shops__items-group'})
    cifra = produto.find('span', attrs={'class': 'price-tag-symbol'})
    valor_reais = produto.find('span', attrs={'class': 'price-tag-fraction'})
    valor_centavos = produto.find('span', attrs={'class': 'price-tag-cents'})
    link = produto.find('a', attrs={'class': 'ui-search-result__content ui-search-link'})
    ntot = ntot + 1
    print(f'Nome: {nome.text}')
    if (valor_centavos):
        print(f'Valor: {cifra.text + valor_reais.text},{valor_centavos.text}')
    else:
        print(f'Valor: {cifra.text + valor_reais.text}')
    print(f'Link: {link["href"]}')
    print('\n\n')
    print(f'Total de itens buscados: {ntot}.')