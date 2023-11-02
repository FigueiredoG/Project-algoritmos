import requests
from bs4 import BeautifulSoup
import pandas as pd
listaPromos = []
url = requests.get('https://gatry.com')
content = url.content
site = BeautifulSoup(content,'html.parser')
promos = site.findAll('div', attrs={'class':'description'})

for promo in promos:
    titulos = promo.find('a',attrs={'target':'_blank'})
    precos = promo.find('p', attrs={'class':'price'})
    links = promo.find('a')['href']
    listaPromos.append([titulos.text,precos.text,links])
    
promocoes = pd.DataFrame(listaPromos, columns=['Título','Preço','links'])
promocoes.to_csv('Promocoes.xsls',index=False)
