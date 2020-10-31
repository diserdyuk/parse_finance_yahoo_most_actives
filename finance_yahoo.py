import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):    # requests and response from url
    r = requests.get(url)
    
    if r.ok:    # catch 
        return r.text
    print(r.status_code)
    

def write_csv(d):    # function write data to csv
    with open('finance_yahoo.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((d['symbol'],
                        d['price'],
                        d['url']))


def get_data(html):    # func.parse html code
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')    # find tags for parse data

    cnt = 0
    for tr in trs:
        cnt += 1
        tds = tr.find_all('td')
        
        try:     # parse symbol from page
            symbol = tds[0].find('a').text
        except:
            symbol = ''    # if info none, catche exception
            
        try:    # parse price from page
            price = tds[2].find('span').text 
        except:
            price = ''

        try:    # parse url from page
            url = 'https://finance.yahoo.com' + tds[0].find('a').get('href')
        except:
            url = ''

        data = {'symbol': symbol,    # packing parse data in dict
                'price': price,
                'url': url}
        
        write_csv(data)    # write parse data in csv


def main():    # hub all functions
    url = 'https://finance.yahoo.com/most-active?count=25&offset=0'
     
    cnt_symbol = 0 
    cnt_page = 0   # count pages, +25 
    while True:    # cycle for parse each page        
        get_data(get_html(url))
        cnt_page += 25 

        soup = BeautifulSoup(get_html(url), 'lxml')
        trs = soup.find('table').find('tbody').find_all('tr')
        
        for tr in trs:   # cycle for stop parser
            cnt_symbol += 1
            print(cnt_symbol)
        
        if cnt_symbol == 223:
            break

        try:    # if page none, catche except 
            url = 'https://finance.yahoo.com/most-active?count=25&offset=' + str(cnt_page)    # 2nd var can use method format
        except:
            break 
       


if __name__ == '__main__':
    main()

