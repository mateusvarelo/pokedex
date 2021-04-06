from requests import get 
import pandas as pd 

class PokedexModel():
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/pokemon/'

    def solicitar_json(self, name_pokemon):
        response = self.requisitar(name_pokemon)
        return response.json()

    def solicitar_csv(self, name_pokemon):
        response = self.requisitar(name_pokemon)
        return self.converter_csv(response.content)

    def requisitar(self, name_pokemon):
        return get(f'{self.url}{name_pokemon}')

    def converter_csv(self, json):
        f = pd.read_json(json)
        return f.to_csv() 

    