from controller import PokedexControl

class PokedexView():
    def __init__(self):
        self.controller = PokedexControl()

    def pesquisar_pokemon(self,metodos_encontro, type_file):
        self.metodos_encontro = metodos_encontro
        self.type_file = type_file 

    def resposta(self):
        return self.controller.request_type(self.metodos_encontro, self.type_file)
