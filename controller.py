from model import PokedexModel

class PokedexControl():
    def __init__(self):
        self.poke_model = PokedexModel()
        
    def request_type(self,name_pokemon,type_file):
       