import requests
from bs4 import BeautifulSoup as bs

#-----------------------------HamkorBank---------------------------------------
link = requests.get('https://hamkorbank.uz/exchange-rate/')
soup = bs(link.content,'html.parser')

#Dollar Kursi $

dollar_ul = soup.find('ul',class_='body')
dollar_li = dollar_ul.find_all('li')
hamkorbank_dollar_olish = dollar_li[3].text
hamkorbank_dollar_sotish = dollar_li[4].text

#Euro kursi

euro_ul = soup.find_all('ul',class_='body')[1]
euro_li = euro_ul.find_all('li')
hamkorbank_euro_olish = euro_li[3].text
hamkorbank_euro_sotish = euro_li[4].text



#---------------Milliy Bank----------
api = requests.get("https://nbu.uz/uz/exchange-rates/")
msoup = bs(api.content,'html.parser')

d = msoup.find('div',class_='kursdata')
mbd = d.find_all('tr')
mbd.remove(mbd[0])
#Dollar
dollar = mbd[0]
td = dollar.find_all('td')
mdo = td[1].text
mdb = td[2].text

#Euro
euro = mbd[1]
td = euro.find_all('td')

meo = td[1].text
meb = td[2].text
print(meo)




#-------------------SQB-Bank------------------------

s_link = requests.get('https://sqb.uz/uz/exchange-rate/json/',headers={'Accept':'application/json'})
j = s_link.json()
dj = j[0]
ej = j[1]


#Dollar
sqb_db = dj.get('cell_price')
sqb_do = dj.get('buy_price')

#Euro
sqb_eb = ej.get('cell_price')
sqb_eo = ej.get('buy_price')
