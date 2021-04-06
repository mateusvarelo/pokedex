from requests import get 
import pandas as pd 

class PokedexModel():
    def init(self):
        self.url = 'https://pokeapi.co/api/v2/pokemon/'

    