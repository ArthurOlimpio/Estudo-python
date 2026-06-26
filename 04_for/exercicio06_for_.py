alunos = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel"]
notas1 = [7.5, 4.2, 8.9, 3.1, 6.0, 9.2, 5.5]
notas2 = [6.0, 7.8, 5.5, 8.0, 4.5, 7.0, 9.1]

aprovados = 0
soma_notas = 0
reprovados = 0

indice_maior = 0
indice_menor = 0

#nota de corte é 5

for i in range(len(alunos)):

    media_notas = (notas1[i] + notas2[i]) / 2
    soma_notas += media_notas

    if media_notas > (notas1[indice_maior] + notas2[indice_maior]) / 2:
        indice_maior = i

    if media_notas < (notas1[indice_menor] + notas2[indice_menor]) / 2:
        indice_menor = i

    if media_notas < 5:
        
        print(f"{alunos[i]} → média {media_notas:.2f} X Reprovado")

        reprovados += 1

    else:
        print(f"{alunos[i]} → média {media_notas:.2f} ✓  Aprovado")

        aprovados += 1



menor = (notas1[indice_menor] + notas2[indice_menor]) / 2
maior = (notas1[indice_maior] + notas2[indice_maior]) / 2

total_alunos = len(alunos)
media = soma_notas / len(alunos)

print(f"\nTotal: {total_alunos} alunos\n"
      f"Aprovados: {aprovados} | Reprovados: {reprovados}\n"
      f"Melhor aluno: {alunos[indice_maior]} ({maior:.2f})\n"
      f"Pior aluno: {alunos[indice_menor]} ({menor:.2f})\n"
      f"Média da turma: {media:.2f}")

