print("Validação")

while True:

    numero = float(input("Digite um número de 1 a 10: "))

    if numero <= 0 or numero > 10:
        print("Digite o um numero válido: ")
        continue
    
    print(f"Número válido: {numero:.1f}")
    break