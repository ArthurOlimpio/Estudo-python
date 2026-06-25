print("Calculadora de descontos")

valor_compra = float(input("Digite o valor da compra: "))

#condicionais apenas para mudarem o valor do desconto

if valor_compra < 100:
    percentual_desconto = 0
    
elif valor_compra <= 299.99:
    percentual_desconto = 5

elif valor_compra <= 499.99:
    percentual_desconto = 10

else:
    percentual_desconto = 15

#conta do desconto


valor_desconto = valor_compra * (percentual_desconto / 100)


valor_final = valor_compra - valor_desconto

print(f"\nValor original: R$ {valor_compra:.2f}\n"
    f"Desconto ({percentual_desconto:.0f}%): R$ {valor_desconto:.2f}\n"
    f"Valor final: R$ {valor_final:.2f}"
    )




