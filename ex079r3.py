listanum = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in listanum:
        listanum.append(n)
        print(f'Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado! Não vou adicionar.')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opcao in 'N':
        break
listanum.sort()
print(listanum)