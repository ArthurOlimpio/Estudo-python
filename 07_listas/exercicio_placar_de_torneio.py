print("Placar de torneio")
nomes = []
pontuacoes = []

for c in range (5):
    nomes.append(str(input("Digite o nome do jogador: ")))
    pontuacoes.append(int(input(f"Digite a pontução do jogador: ")))

for nome, pontuacao in nomes, pontuacoes:
    print(f"{nome}, {pontuacao}")


maior = max(pontuacoes)
menor = min(pontuacoes)


for posicao, valor in enumerate(pontuacoes):
    if valor == maior:
        print(f'{nomes[posicao]} foi o que mais marcou com {maior} pontos')

    if valor == menor:
         print(f'{nomes[posicao]} foi o que menos marcou com {menor} pontos')


