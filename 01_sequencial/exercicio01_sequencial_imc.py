print("Calculadora de IMC")

nome = input("Digite seu nome: ")
peso = float(input(f"{nome}, Digite seu peso: "))
altura = float(input(f"{nome}, Digite sua altura: "))

imc = peso / altura ** 2

print(f"{nome}, seu IMC é {imc:.2f}")