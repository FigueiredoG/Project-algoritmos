import requests
from bs4 import BeautifulSoup
import time 
import pandas as pd

listapromos = {}
listadatas = {}
for pagina in range(1,3):
    url = 'https://www.hardmob.com.br/forums/407-Promocoes/page' + str(pagina)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}
    response = requests.get(url,headers=headers)
    content = response.content
    site = BeautifulSoup(content,'html.parser')
    promos = site.find_all('h3', attrs = {'class':'threadtitle'})

    for promo in promos:
        titulo = promo.find('a', attrs = {'class': 'title'})
        listapromos['promocao'] = titulo.text + ' 1 '

    datas = site.find_all('d1', attrs = {'class': 'threadlastpost td'})
    for data in datas:
        date = data.find('span', attrs = {'class':'time'})
        listadatas['datas'] = date.text
 
listageral = []
listageral.append(listapromos)
listageral.append(listadatas)

promocoes = pd.DataFrame(listapromos, columns=['Titulo', 'Data'])
promocoes.to_excel('PromocoesHardmob.xlsx')