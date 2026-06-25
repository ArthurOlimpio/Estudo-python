print ("Calculadora de viagem")

destino = input("Digite o seu destino: ")
distancia_km = float(input(f"Digite a distancia em KM para {destino}: "))
consumo_km = float(input("Digite o consumo do carro por km/l: "))
preco_combustivel = float(input("Digite o preço do combustivel: "))

combustivel_necessario = distancia_km / consumo_km

custo_combustivel = combustivel_necessario * preco_combustivel

print(f"\nViagem: São Paulo -> {destino}\n"
     f"Distância: {distancia_km:.2f} km\n"
     f"Litros necessários: {combustivel_necessario:.2f} L\n" 
     f"Custo estimado: R$ {custo_combustivel:.2f}"
     )