import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup
def real_time_price(stock_code):
    url = 'https://finance.yahoo.com/quote/' + stock_code +('.HE?p=') + stock_code + ('.HE&.tsrc=fin-srch')
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', {'class' : 'My(6px) Pos(r) smartphone_Mt(6px)' })
    content = web_content.find('span').text
    return content

#web_content = real_time_price('KNEBV')
#print(web_content)

stocks = ['FORTUM', 'KNEBV']
for step in range(1, 101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    for osake in stocks:
        price.append(real_time_price(osake))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real time stock data.csv', mode='a', header=False)
    print(col)

