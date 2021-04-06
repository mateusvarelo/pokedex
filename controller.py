from model import PokedexModel

class PokedexControl():
    def __init__(self):
        self.poke_model = PokedexModel()
        
    def request_type(self,name_pokemon,type_file):
        type_file = []
        if (type_file == "csv"):
            type_file = self.poke_model.request_csv(name_pokemon) 
        
        elif (type_file == "json"):
            type_file = self.poke_model.request_json(name_pokemon)  
            
              
              
       