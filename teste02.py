continuar = ' '
removidos = []
while continuar not in 'N':
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30] 

    opcao = int(input('Escolha um número entre 0 e 30 para remover da lista: '))
    print(f'Número {lista[opcao]} excluido com sucesso!')
    if opcao in removidos:
        print(f'Esse número já foi excluído, tente outro')
        opcao = int(input('Escolha um número entre 0 e 30 para remover da lista: '))
    else:
        if opcao in lista:
            lista.remove(lista[opcao] + 1)
        else:
            while opcao not in lista:
                opcao = int(input('Escolha um número entre 0 e 30 para remover da lista: '))
                lista.remove(lista[opcao] + 1)
                break
            break
    removidos.append(lista[opcao])
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).upper()[0]

print(f'Os valores removidos foram {removidos}')
print(f'Os valores que sobraram foram {lista}')
