lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A lista comleta é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
