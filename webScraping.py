import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

request = requests.get('https://opentender.eu/start')
soupData = BeautifulSoup(request.content, 'html5lib')
s = soupData.find('ul', class_='portal-links')

countries = []
Tenderscount = []

for link in s.find_all('a'):
    
    countries.append(link.text)
for link in s.find_all('div'):
     
    Tenderscount.append(link.text)

data_list = []
count = 1
for x, y in zip(countries, Tenderscount):
    d = {}
    d['S.No'] = f'country {count}'
    d['Country'] = x
    d['No. of Tenders'] = y
    count += 1
    data_list.append(d)


import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

request = requests.get('https://opentender.eu/start')
soupData = BeautifulSoup(request.content, 'html5lib')
s = soupData.find('ul', class_='portal-links')

countries = []
Tenderscount = []

for link in s.find_all('a'):
    print(link.text) 
    countries.append(link.text)
for link in s.find_all('div'):
    print(link.text) 
    Tenderscount.append(link.text)

data_list = []
count = 1
for x, y in zip(countries, Tenderscount):
    d = {}
    d['S.No'] = f'country {count}'
    d['Country'] = x
    d['No. of Tenders'] = y
    count += 1
    data_list.append(d)
print(data_list)

plt.bar(countries, Tenderscount, color = 'g',width = 0.72, label = "Tenders")
plt.xticks(rotation = 52)
plt.xlabel('Countries')
plt.ylabel('No. of Tenders')
plt.title(' Opentender PORTALS ')
plt.legend()
plt.show()

filename = 'webScraping.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['S.No','Country','No. of Tenders'])
    w.writeheader()

filename = 'webScraping.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['S.No','Country','No. of Tenders'])
    w.writeheader()