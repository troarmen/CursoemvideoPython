from random import randint
computador = randint(0, 10)
print('-='*20, 'Jogo da adivinhação', '-='*20)
print('Vou pensar em um número de 0 a 10, tente adivinhar...')
acertou = False  # A variável recebe falso porque a pergunta ainda não foi feita, então você ainda não acertou
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} palpites')
