"""contador = ('zero', 'um', 'dois', 'três', 'quatro', 
            'cinco', 'seis', 'sete', 'oito', 
            'nove', 'dez', 'onze', 'doze', 
            'treze', 'quatorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 
            'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
print(f'Você digitou o número {contador[numero]'}"""

"""Para o python saber qual é o número certo que deve ser usado da tupla
usamos o nome da tupla e pedimos na posição "numero".
Por ex.: Se o número escolhido for zero, o python retira a palavra que está na posição zero e assim sucessivamente"""

extensos = ('zero', 'um', 'dois', 'três', 'quatro', 
            'cinco', 'seis', 'sete', 'oito', 
            'nove', 'dez', 'onze', 'doze', 
            'treze', 'quatorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 
            'dezenove', 'vinte')

#  Ler algum número entre 0 e 20
while True:
    numero = int(input('Digite um número entre 0 e 20: '))   
    if 0 <= numero <= 20:
        break
    print('Tente novamente.', end=' ')
# Mostrá-lo por extenso
print(f'Você digitou o número {extensos[numero]}')
