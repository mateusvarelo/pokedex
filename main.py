from view import PokedexView

print("Digite um nome de um pokémon.")
print("Ou se preferir digite um número entre 1 é 1118 que corresponde a um pokémon.")
nome_numero = input()
print("Qual tipo de arquivo (CSV)ou(JSON):")
tipo = input()
pokemon = PokedexView()
pokemon.pesquisar(nome_numero,tipo)

print(pokemon.resposta())