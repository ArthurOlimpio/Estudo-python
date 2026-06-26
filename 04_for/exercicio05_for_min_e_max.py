precos = [12.50, 8.90, 45.00, 3.20, 67.80, 22.10, 5.50]

menor = precos[0]
maior = precos[0]


for i in range(len(precos)):
    
    if precos[i] > maior:
        maior = precos[i]

    elif precos[i] <menor:
        menor = precos[i]



print(f"O produto mais caro é R$ {maior:.2f}\n"
      f"O produto mais barato é R$ {menor:.2f}")
