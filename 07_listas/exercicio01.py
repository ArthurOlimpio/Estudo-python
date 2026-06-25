numeros = list()

for contagem in range(0,5):
    numeros.append(int(input(f"Digite um valor para a posição {contagem}: ")))
   

print(f'O maior valor dessa lista é o numero {max(numeros)}\n'
f'O menor valor dessa lista é o numero {min(numeros)}')

maior = max(numeros)
menor = min(numeros)

for posicao, valor in enumerate(numeros):
    if valor == maior:
        print(f'{maior} está na posição {posicao}')

    if valor == menor:
        print(f'{menor} está na posição {posicao}')