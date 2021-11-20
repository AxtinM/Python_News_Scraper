from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
global url 
url = 'http://www.isitcom.rnu.tn/'



def get_data(url):
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_news(soup):
    news_list = soup.find_all('a', {'class': 'home-article-title'})
    for _ in range(len(news_list)):
        if news_list[_].find('img'):
            print(f'NEW ARTICLE {_ + 1}: {str(news_list[_].text)}')
            ext = str(news_list[_].get('href'))
            print(f'URL({_ + 1}) : {url+ext}\n')


soup = get_data(url)

if __name__ == '__main__':
    get_news(soup)