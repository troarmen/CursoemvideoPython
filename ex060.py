# Resolução mais simples, porém não a tradicional pq nem todas as linguagens tem uma função para cálculo de fatorial
"""from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}')"""

# Resolução tradicional
numero = int(input('Digite um número para ver seu Fatorial: '))
contador = numero
fatorial = 1
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')

# Resolução com for
"""n1 = int(input('Digite um número inteiro qualquer: '))
acumulador = 1
for n1 in range(n1, 0, -1):
    acumulador *= n1
print('O produto de todos os números é {}'.format(acumulador))"""
