from prettytable import PrettyTable
import random

import requests
from bs4 import BeautifulSoup as BS

x = PrettyTable()

Place = []
lis = []

x.add_column("Местоположения   Все случаи заболевания   Новые случаи за 1дн.   Умерло",[Place])

r = requests.get('https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU%3Aru')

html = BS(r.content, 'lxml')

table = html.find('tbody', class_ = 'ppcUXd').find_all('tr') #Полная Таблица


for item in table:
	item_text = item.text
	lis.append(item_text)


Place.append(random.choice(lis))

print(x)
