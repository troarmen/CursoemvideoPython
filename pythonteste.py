"""from pyautogui import position
import time

time.sleep(9)
print(position())
continuar = ' '
removidos = []
while continuar not in 'N':
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30] 

    opcao = int(input('Escolha um número entre 0 e 30 para remover da lista: '))
    print(f'Número {lista[opcao]} excluido com sucesso!')
    removidos.append(lista[opcao])
    if opcao in removidos:
        print(f'Esse número já foi excluído, tente outro')
        opcao = int(input('Escolha um número entre 0 e 30 para remover da lista: '))
    else:
        if opcao in lista:
            del lista[opcao]
        else:
            while opcao not in lista:
                opcao = int(input('Escolha um número entre 0 e 30 para remover da lista: '))
                del lista[opcao]
                break
            break
        break
    print(lista)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).upper()[0]

print(f'Os valores removidos foram {removidos}')
print(f'Os valores que sobraram foram {lista}')
from random import sample
jogos = []
a=sorted(sample(range(1, 61), 6))
jogos.append(a[:])
print(jogos)"""
from djitellopy import Tello
tello = Tello()

tello.connect()

print(tello.get_battery())