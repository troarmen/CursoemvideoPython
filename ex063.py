print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
quantidade = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('~' * 30)
print(f'{termo1} < {termo2}', end='')
# Contador recebe 3 pois no começo você já mostra os 3 primeiros termos
contador = 3
while contador <= quantidade:
    termo3 = termo1 + termo2
    print(f' < {termo3}', end='') 
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' < FIM')
