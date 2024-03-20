lista = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append((str(input('Nome: '))))
    pessoas.append((float(input('Peso: '))))
    if len(lista) == 0:
        maior = menor = pessoas[1]
    elif pessoas[1] > maior:
        maior = pessoas[1]
    elif pessoas[1] < menor:
        menor = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break

print('-=' * 30)
print(f'O total de pessoas é de {len(lista)}')
print(f'O maior peso é de {maior}. Peso de ', end='')
for elemento in lista:
    if elemento[1] == maior:
        print(f'[{elemento[0]}]', end=' ')
print(f'\nO menor peso é de {menor}. Peso de ', end='')
for e in lista:
    if e[1] == menor:
        print(f'[{e[0]}]', end='')
