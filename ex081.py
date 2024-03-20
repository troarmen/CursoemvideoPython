lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print('-' * 30)
print(f'Você digitou {len(lista)} números')
print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
