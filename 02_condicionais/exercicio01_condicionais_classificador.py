print("Classificação de idade")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <= 12:
    print(f"{nome} tem {idade} anos e é Criança")

elif idade <= 17:
    print(f"{nome} tem {idade} anos e é Adolescente")

elif idade <= 64:
    print(f"{nome} tem {idade} anos e é Adulto")

else:
    print(f"{nome} tem {idade} anos e é Idoso")