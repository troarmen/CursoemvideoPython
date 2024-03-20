from random import randint

print('-'*10, 'PAR ou ÍMPAR', '-'*10)
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR[P/I]: ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}', end='  ')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você venceu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você ganhou {vitorias} vezes')
