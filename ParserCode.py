from prettytable import PrettyTable
import random

import requests
from bs4 import BeautifulSoup as BS

x = PrettyTable()

Place = []
Сases = []


x.add_column("Местоположения",[Place])
x.add_column("Все случаи заболевания   Новые случаи за 1дн.   Умерло", [Сases])


r = requests.get('https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU%3Aru')

html = BS(r.content, 'lxml')

lis = []


table = html.find('tbody', class_ = 'ppcUXd').find_all('tr') #Полная Таблица


for item in table:
	item_text = item.text
	print(item_text)

table2 = html.find('tbody', class_ = 'ppcUXd').find_all('th') #Таблица названий стран


for item in table2:
	item_text = item.text
	Place.append(item_text)
