dicio = dict()
gols = list()
dicio['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
cont = 0
while cont < partidas:
    gols.append(int(input(f'    Quantos gols na partida {cont}? ')))
    cont += 1
dicio['gols'] = gols
dicio['total'] = sum(gols)
print('-=' * 30)
print(dicio)
print('-=' * 30)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'{dicio["nome"]} jogou {partidas} partidas')
for ic, va in enumerate(gols):
    print(f'    Na partida {ic}, {dicio["nome"]} fez {va} gols')
print(f'Foi um total de {dicio["total"]} gols')
