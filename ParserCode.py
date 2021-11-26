from prettytable import PrettyTable
import unidecode
import random
import requests
from bs4 import BeautifulSoup as BS

a = random.randint(0,40)
x = PrettyTable()
Place = []
name = []
data = []

r = requests.get('https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU%3Aru')
html = BS(r.content, 'lxml')

x.add_column("     Местоположения     |     Все случаи заболевания     |     Новые случаи за 1дн.     |     Кол-во на млн ч.     |     Умерло     ",[Place])

tableCountries = html.find('tbody', class_ = 'ppcUXd').find_all('th') #Названия стран
tableData = html.find('tbody', class_ = 'ppcUXd').find_all('td') #Данные

for i in tableCountries:
    i_text = i.text
    name.append(i_text)

for j in tableData:
    j_text = j.text
    data.append([j_text])


resultData = [[e for sublist in data[i:i+5] for e in sublist] for i in range(0,len(data),5)]

nameStr = ''.join(name[a])
dataStr = ','.join(resultData[a])
dataStr = dataStr.replace(',,', ',')
dataStr = dataStr.replace(',', '               ')
dataStr = unidecode.unidecode(dataStr)
result = nameStr + '               ' + dataStr

Place.append(result)

print(x)
