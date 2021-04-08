from model import PokedexModel

class PokedexControl():
    def __init__(self):
        self.poke_model = PokedexModel()
        
    def request_type(self,metodos_encontro,type_file):
        conteudo = []
        if (type_file == 1): 
             conteudo = self.poke_model.solicitar_csv(metodos_encontro)
        elif (type_file == 2):
             conteudo = self.poke_model.solicitar_json(metodos_encontro)
        return conteudo
       