from model import PokedexControl

class PkedexView():
    def __init__(self):
        self.controller = PokedexControl()
        
    def pesquisar_pokemon(self, name_pokemon, type_pokemon):
        self.name_pokemon = name_pokemon
        self.type_pokemon = type_pokemon
    
    def resposta(self):
        return self.controller.request(self.name_pokemon, self.type_pokemon)
