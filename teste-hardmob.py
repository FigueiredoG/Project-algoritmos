import requests
from bs4 import BeautifulSoup
import time 
import pandas as pd

listaPromos = []
start_time = time.time()
for pagina in range(1,10):
    url = 'https://www.hardmob.com.br/forums/407-Promocoes/page' + str(pagina)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}
    response = requests.get(url,headers=headers)
    content = response.content
    site = BeautifulSoup(content,'html.parser')
    promos = site.find_all('h3', attrs = {'class':'threadtitle'})
    for promo in promos:
        titulo = promo.find('a', attrs = {'class': 'title'})
        listaPromos.append(titulo.text)
    print('.')
promocoes = pd.DataFrame(listaPromos, columns=['Geral'])
promocoes.to_excel('PromocoesHardmob.xlsx')

end_time = time.time()
execution_time = end_time - start_time

print(f"Tempo de execução: {execution_time} segundos")