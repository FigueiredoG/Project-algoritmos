import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta
import pandas as pd
listaPromos = []
listaDatas=[]
ListaGeral = []
DataAtual= date.today()
DataCorrigida = DataAtual.strftime('%d/%m/%Y')
Ontem = DataAtual - timedelta(days = 1)
DataOntem = Ontem.strftime('%d/%m/%Y')

for pagina in range(1,2000):
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
        Datas = data.previous_element
        Datas = Datas.replace(",", " ")
        Datas = Datas.replace(" ", "")
        Datas = Datas.replace("-", "/")
        if Datas == 'Hoje':
            Datas = str(DataCorrigida)
        elif Datas == 'Ontem':
            Datas=DataOntem
        listaDatas.append(Datas)    
        
    for i in range (len(listaPromos)-2):
        try:
            ListaGeral.append([listaPromos[i+2],listaDatas[i+2]])
        except:
            break
    listaPromos.clear()
    listaDatas.clear()
        
promocoes = pd.DataFrame(ListaGeral, columns=['Geral','Datas'])
promocoes.to_excel('PromocoesHardmobAtualizado.xlsx')
