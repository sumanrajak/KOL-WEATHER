import pandas  as pd
import requests
from bs4 import BeautifulSoup

page=requests.get('https://weather.com/en-IN/weather/today/l/22.57,88.36?par=google&temp=c')
soup = BeautifulSoup(page.content , 'html.parser')
total = soup.find_all(id="LookingAhead")
d=total[0].find_all(class_="today-daypart-content")
day = [item.find(class_="today-daypart-content").get_text() for item in total]
day1 = [item.find(class_="today-daypart-temp").get_text() for item in d]
day2 = [item.find(class_="today-daypart-title").get_text() for item in d]
day3 = [item.find(class_="today-daypart-wxphrase").get_text() for item in d]
day4 = [item.find(class_="today-daypart-precip").get_text() for item in d]



weather=pd.DataFrame({'DAY':day2,'TEMP':day1,'DESCRIPTION':day3 ,'PRICIP': day4})
print(weather)

