print("Acumulador\n")

numero = 0
soma_numero = 0
quantidade = 0

while True:

    numero = float(input("Digite um número (0 para sair): "))

    if numero != 0:

        soma_numero += numero
        quantidade += 1
        continue

    print(f"números digitados: {quantidade}\n"
    f"Soma total: {soma_numero}")
    break