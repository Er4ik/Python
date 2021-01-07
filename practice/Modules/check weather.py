import requests
from bs4 import BeautifulSoup

url = "https://weather.i.ua/"
sourse = requests.get(url)
text = sourse.text
soup = BeautifulSoup(text)
temp = soup.find("span", {"class" : "icon-xl i_rain"})
weath = soup.find("li", {"class" : "summary_item col-description"})
temp = temp.text
weath  = weath.text
print(f"Погода в Киеве {temp}\nОжидается {weath}")
