n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O maior valor é {n1} e o menor valor é {n2}')
elif n2 > n1:
    print(f'O maior valor é {n2}, e o menor valor é {n1}')
else:
    print('Não há valor maior, os dois são iguais.')