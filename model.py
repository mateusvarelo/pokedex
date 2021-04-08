from requests import get 
import pandas as pd 

class PokedexModel():
    def __init__(self):
        self.url ="https://pokeapi.co/api/v2/"
        self.recurso_pokemon ="encounter-method"

    def solicitar_json(self,metodos_encontro):
        response = self.requisitar(metodos_encontro)
        return response.json()

    def solicitar_csv(self, metodos_encontro):
        response = self.requisitar(metodos_encontro)
        return self.convert_csv(response.content)


    