print('Clinica de saude')
nomes = []
idades = []
while True:

    opcao = int(input('' \
    '1 - Cadastrar paciente\n' \
    '2 - Listar pacientes\n' \
    '0 - Sair\n' \
    'Selecione uma opção: '))

    
    if opcao == 1:
        nome = input('Digite o nome do paciente: ')
        idade = int(input(f'Digite a idade do paciente {nome}: '))
        

        while idade < 0 or idade > 120:
            idade = int(input('Digite uma idade valida:'))
            

        print('\nPaciente cadastrado com sucesso\n')
        nomes.append(nome)
        idades.append(idade)

    elif opcao == 2:
        if not nomes:
            print('\nNenhum paciente cadastrado\n')

        else:
            for i in range(len(nomes)):
                print(nomes[i], idades[i])
                print(f'Total de pacientes: {len(nomes)}')

    elif opcao == 0:
        break

    else:
        print('Digite uma opção valida')
    

