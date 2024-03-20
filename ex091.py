from random import randint
from operator import itemgetter

jogadores = {}
ranking = list()
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"-=" * 10}', end='')
print(f'{"RANKING DOS JOGADORES":^20}', end='')
print(f'{"-=" * 10:>20}')
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}')
