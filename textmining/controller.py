import nltk
from textmining.entity import Entity
from textmining.samsung_service import  SamsungService

class Controller:
    def __init__(self):
        pass
    def download_dictionary(self):
        nltk.download('all')#영어사전 전부 다같고 오는 것
    def data_analysis(self):
        entity = Entity()
        service = SamsungService()
        entity.fname = 'kr-Report_2018.txt'
        entity.context = './data/'
        service.extract_token(entity)  # 알고리즘 시작
        service.extract_hanguel()
        service.conversion_token()
        service.compound_noun()
        entity.fname = 'stopwords.txt'
        service.extract_stopword(entity)# 사용하지 않는 단어 빼기
        service.filtering_text_with_stopword()
        service.frequent_text()
        entity.fname = 'D2Coding.ttf'
        service.draw_worldcloud(entity)  # 알고리즘 끝