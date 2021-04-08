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

    def requisitar(self, metodos_encontro):
        return get(f"{self.url}{self.recurso_pokemon}/{metodos_encontro}")
    
    def convert_csv(self, dados_request):
        f = pd.read_json(dados_request)
        return f.to_csv()