print("Programa de troco")

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input(f"Digite o preço do {nome_produto}: "))
valor_pago = float(input(f"Digite o valor pago pelo cliente: "))

troco = valor_pago - preco_produto

print("=-"*30)

print("Troco a ser devolvido\n"
f"Produto: {nome_produto}\n"
f"Valor pago: R${valor_pago:.2f}\n"
f"Troco: R${troco:.2f}\n")
