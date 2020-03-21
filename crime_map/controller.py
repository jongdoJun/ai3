from crime_map.service import Service
from crime_map.entity import Entity
class Controller:
    def __init__(self):
        self.e = Entity()
        self.s = Service()

    def convert_df(self):
        e = self.e
        s = self.s
        e.context = './data/'
        e.fname = 'crime_in_seoul.csv'
        s.fetch_crime(e)
        e.fname = 'cctv_in_seoul.csv'
        s.fetch_cctv(e)
        e.fname = 'pop_in_seoul.xls'
        s.fetch_pop(e)

    def modeling(self):
        e = self.e
        s = self.s
        s.save_police(e)
        s.save_cctv_pop()
        e.context = './saved_data/'
        e.fname = 'police.csv'
        s.fetch_police(e)
        s.fetch_police_norm()
        e.fname = 'cctv_pop.csv'
        s.save_police_norm(e)

