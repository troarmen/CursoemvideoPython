listanum = []
while True:
    listanum.append(int(input('Digite um número: ')))
    if listanum.count(listanum[-1]) == 1:
        print('Valor adicionado com sucesso!')
    elif listanum.count(listanum[-1]) == 2:
        print('Valor duplicado! Não vou adicionar.')
        del listanum[-1]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opcao in 'N':
        break
listanum.sort()
print(listanum)
