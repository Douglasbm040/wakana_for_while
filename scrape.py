import pandas as pd
import requests
from bs4 import BeautifulSoup

link='https://www.google.com.br/maps/place/'
local = 'Espirito Santo'
pesquisa = link+local


req = requests.get(pesquisa)
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
print(soup)