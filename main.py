from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    d = dict()
    k = int()
    text = str()
    url = 'https://m.imdb.com/chart/top/?ref_=nv_mv_250' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    soup.get_text(strip=True)
    #print(soup)
    mydivs = soup.find_all("span", {"class": "media-body media-vertical-align"})
    for data in mydivs:
        k+=1
        text = data.text.strip()
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        text = text.replace("    ", " Рейтинг: ")
        d[k]=text
        print(d[k])
        #print("След")

if __name__ == '__main__':
    parse()