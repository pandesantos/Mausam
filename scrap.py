import requests
from bs4 import BeautifulSoup, Tag
import pandas as pd

url = "https://www.accuweather.com/en/np/nepal-weather"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


weather_list = soup.find('div', class_='condition-table').findAll('a')
tempr_list= soup.find('div', class_='condition-table').findAll('span')

data = []
for item in weather_list:
	data.append(item.text.strip())

data = list(data)

#some_list[start:stop:step]

places = data[0::2]
del places[20:] # remove last element

temperatures = data[1::2]

A = range(len(temperatures))

df = pd.DataFrame()

df['Places'] = places
df['Temperatures in F'] = temperatures 

print df # print dataframe data
