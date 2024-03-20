# Pedir 4 números
lista = []
maior = 0
menor = 0
for c in range(1, 5):
    num = int(input('Digite um número: '))
    lista.append(num)
    
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

# Mostrar os números digitados dentro de uma tupla
print(f'Os valores digtados foram{lista}')
# Quantas vezes apareceu  valor 9
print(f'O número 9 apareceu {lista.count(9)} vezes')
# Em que posição está o número 3
print(f'O número 3 está na {lista.index(3) + 1}ª posição')
# Mostrar os valores pares digitados
par = []
for n in lista:
    if n % 2 == 0:
        par.append(n)
print(f'Os valores pares digitados foram {par}')
