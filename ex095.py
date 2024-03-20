jogador = dict()
time = list()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
       continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print(f'cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 45)
for cod, ele in enumerate(time):
    print(f'{cod:>3}', end=' ')
    elementospl = 0
    for v in ele.values():
        print(f'{v} ', end='    ')
        elementospl += 1
        if elementospl == 3:
            print()
print('-' * 45)
while True:
    leitura = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    print('-' * 45)
    if leitura == 999:
        break
    if leitura >= len(time):
        print(f'ERRO! Tente novamente.')
    else:
        print(f' --Levantamento do {time[leitura]["nome"].upper()}')
        for i, g in enumerate(time[leitura]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
        print('-' * 45)
print('<< VOLTE SEMPRE >>')
