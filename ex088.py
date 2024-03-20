from random import randint
from time import sleep

print('-' * 30)
print(f'{"MEGA SENA":^30}')
print('-' * 30)
lista = []
jogadas = []
totalj = 1
quan = int(input('Quantas jogadas você quer que eu sorteie? '))
while totalj <= quan:
    totaln = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            totaln += 1
        if totaln >= 6:
            break
    lista.sort()
    jogadas.append(lista[:])
    lista.clear()
    totalj += 1

for n, j in enumerate(jogadas):
    print(f'Jogo {n + 1}: {j}', end='\n')
    sleep(0.75)
print('-' * 30)
print(f'{"BOA SORTE":^30}')
