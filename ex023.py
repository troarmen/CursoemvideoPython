# Essa forma de declarar a variável como str não era a melhor a ser usada no momento
'''num = int(input('Informe um número entre 0 9999: '))
n = str(num)
print(f'Analisando o número {num}')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')'''

# Essa é a resolução matemática, sem ter que converter a variável inteira para string
num = int(input('Informe um número: '))
u = num // 1 % 10  # O sinal de porcentagem siginifica o resto da divisão. Nesse caso ele divide por 10 e pega o resto
# da divisão.
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Cenetena: {c}')
print(f'Milhar: {m}')
