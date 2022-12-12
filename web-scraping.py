import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content
site = BeautifulSoup(content, 'html.parser')

#HTML da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    #Titulo da noticia
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    #print(titulo.text)
    #print(titulo['href']) #link da noticia

    #Subtitulo da noticia
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    #if (subtitulo):
        #print(subtitulo.text)
    #Lista
    if (subtitulo):
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])
#print(lista_noticias)
dataframe_noticias = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])
dataframe_noticias.to_excel('noticias.xlsx', index=False)
print(dataframe_noticias)
