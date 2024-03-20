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

# mostrar uma lista com os 5
print(f'Vovê digitou os números: {listanum}')
print('-' * 30)
# mostrar maior e suas posicoes
print(f'O maior número digitado foi {maior}, nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}...', end='')
# mostrar menor e suas posicoes
print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end='')
print(f'\n{"-" * 30}') # Tive que usar o format pois o ultimo indice é um end=''
                        # e por causa disso a linha tava indo junto
