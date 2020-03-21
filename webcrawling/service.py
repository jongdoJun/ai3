from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

class Service:
    def __init__(self):
        pass

    def bugs_music(self, payload):
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name = 'p', attrs=({'class' : 'title'})):
            n_title += 1
            print(str(n_title) + '위')
            print('노래제목: '+i.text)
        for i in soup.find_all(name = 'p', attrs=({'class' : 'artist'})):
            n_artist += 1
            print(str(n_artist) + '위')
            print('아티스트: ' + i.find('a').text)

    def naver_movie(self, payload):
        driver = webdriver.Chrome(payload.path)
        driver.get(payload.url)
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        print(soup.prettify())

