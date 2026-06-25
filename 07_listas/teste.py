produtos = ["Arroz", "Feijão", "Macarrão", "Azeite"]
precos = [5.90, 8.50, 3.20, 22.00]

menor = min(precos)
maior = max(precos)

for i in range(len(produtos)):

    if precos[i] >= maior:
        print(f"O produto mais caro: {produtos[i]} - R${precos[i]:.2f}")

    else:
        print("")