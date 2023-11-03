import requests
from bs4 import BeautifulSoup
import time 
import pandas as pd
testador = ''
listaPromos = []
listaDatas=[]
ListaGeral = []
for pagina in range(1,3000):
    url = 'https://www.hardmob.com.br/forums/407-Promocoes/page' + str(pagina)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}
    response = requests.get(url,headers=headers)
    content = response.content
    site = BeautifulSoup(content,'html.parser')
    promos = site.find_all('h3', attrs = {'class':'threadtitle'})
    datas = site.findAll('span', attrs = {'class':'time'})
    for promo in promos:
        titulo = promo.find('a', attrs = {'class': 'title'})
        listaPromos.append(titulo.text)
    for data in datas:
        testador = data.previous_element
        if testador == ',':
            
        listaDatas.append(testador)    
    for i in range (len(listaPromos)-2):
        ListaGeral.append([listaPromos[i+2],listaDatas[i+2]])
    listaPromos.clear()
    listaDatas.clear()
        
promocoes = pd.DataFrame(ListaGeral, columns=['Geral','ola'])
promocoes.to_excel('PromocoesHardmob.xlsx')
