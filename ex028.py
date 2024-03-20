from random import randrange
from time import sleep
numero_secreto = randrange(0,5) # Faz o computador sortear um número de 0 a 5
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-'*20)
a = int(input('Diga que número eu pensei e direi se você acertou!: ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if a == numero_secreto:
    print(f'Parabéns você acertou o número secreto, era {numero_secreto}')
else:
    print(f'Infelizmente você perdeu... A resposta era {numero_secreto}')