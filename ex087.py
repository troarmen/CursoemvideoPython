matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
somaColuna = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha, coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()
for linha in range(0, 3):
    somaColuna += matriz[linha][2]
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print('-'* 30)

print(f'A soma dos pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
print(f'O maior valor da segunda linha é {maior}')
