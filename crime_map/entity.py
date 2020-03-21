import pandas as pd
import json
import googlemaps

class Entity:
    def __init__(self):
        self._context = None
        self._fname = None

    @property
    def context(self) -> str:
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    def new_file(self) -> str:
        return self._context + self._fname

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        return pd.read_excel(self.new_file(),encoding='UTF-8', usecols=usecols)

    def json_load(self) -> object:
        return json.load(open(self.new_file(),encoding='UTF-8'))

    def create_gmaps(self) -> object:
        return googlemaps.Client(key='AIzaSyBz9GRH0blpoiLp1co3O5V3hXgwT928jyY')
