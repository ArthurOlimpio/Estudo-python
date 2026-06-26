temperaturas = [23, 31, 18, 29, 15, 34, 22]

temperatura_media = 0
quente = 0
soma_dias = 0

for i in range(len(temperaturas)):
    soma_dias += temperaturas[i]

    if temperaturas[i] > 25:
        quente += 1

temperatura_media = soma_dias / len(temperaturas)
    
print(f"Dias quentes: {quente}\n"
      f"Média semanal: {temperatura_media:.2f}ºC")        