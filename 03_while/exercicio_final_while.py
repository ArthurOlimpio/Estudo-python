
saldo = 1000

while True:
    menu = int(input("\n=== Banco PyBank ===\n"
    f"Saldo atual: R$ {saldo:.2f}\n"
    "1. Sacar\n"
    "2. Depositar\n"
    "3. Ver saldo\n"
    "4. Sair\n"
    "Escolha uma opção: "))

    if menu == 1:
    
        saque = float(input(f"\nSeu saldo é de R$ {saldo:.2f}, digite o quanto deseja sacar: "))
        

        if saque > saldo:
            print ("Não é possível sacar uma quantia maior que o saldo")
            continue

        elif saque <= 0:
            print("Digite um valor válido para o saque")
            continue

        else:
            print(f"Saque de R$ {saque:.2f} realizado")
            saldo -= saque
        
    elif menu == 2:
        
        deposito = float(input(f"\nSeu saldo é de R$ {saldo:.2f}, digite o quanto deseja depositar: "))

        if deposito <= 0:
            print(f"Digite um valor válido para deposito")
            continue

        else:
            saldo += deposito
            print(f"Deposito de R$ {deposito:.2f} realizado")
    
    elif menu == 3:
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}")

    elif menu == 4:
        print(f"Obrigado por utilizar PyBank como seu banco\n seu saldo atual é de {saldo:.2f}")
        break

    else:
        print("Digite uma opção valida")

