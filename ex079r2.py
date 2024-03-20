listanum = []
while True:
    n = (int(input('Digite um número: ')))
    if listanum.count(n) == 0:
        print('Vaor adicionado com sucesso!')
        listanum.append(n)
    elif listanum.count(n) == 1:
        print('Valor duplicado! Não vou adicionar')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opcao in 'N':
        break
listanum.sort()
print(listanum)
