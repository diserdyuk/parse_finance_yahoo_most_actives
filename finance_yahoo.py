import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):    # запрос и полчение кода страницы
    r = requests.get(url)
    
    if r.ok:
        return r.text
    print(r.status_code)
    

def write_csv(d):
    with open('finance_yahoo.csv', 'a') as f:
        write = csv.writer(f)
        pass


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')

    cnt = 0
    for tr in trs:
        cnt += 1
        tds = tr.find_all('td')
        
        try:
            symbol = tds[0].find('a').text
        except:
            symbol = ''
            
        try:
            price = tds[2].find('span').text 
        except:
            price = ''

        try:
            url = 'https://finance.yahoo.com' + tds[0].find('a').get('href')
        except:
            url = ''




def main():
    url = 'https://finance.yahoo.com/most-active'
    get_data(get_html(url))
    # pass




if __name__ == '__main__':
    main()