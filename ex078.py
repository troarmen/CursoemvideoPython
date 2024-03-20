# pedir 5 números
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    elif listanum[c] > maior:
        maior = listanum[c]
    elif listanum[c] < menor:
        menor = listanum[c]

print(f'Vovê digitou os números: {listanum}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}...', end='')
print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end='')
print(f'\n{"-" * 30}')