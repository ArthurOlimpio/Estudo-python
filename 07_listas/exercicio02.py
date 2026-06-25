listanum = []

while True:

    numero = int(input("Digite um valor: "))
    if numero in listanum:

        print('Valor duplicado Não adicionado')

    else:
        listanum.append(numero)
        print("Valor adicionado com sucesso")

    continuar = input('Quer continuar? [S/N]: ')

    if continuar == 's' or continuar == 'S':
        continue

    if continuar == 'n'  or continuar == 'N':
        print('=-' * 30)
        listanum.sort()
        print(f'Você digitou os valores {listanum}')
        break
    
    else:
        print('Opção invalida')