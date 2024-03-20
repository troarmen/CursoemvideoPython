#  Pedir 4 números
num =  (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))

#  Armazená-los em um tupla e mostrá-los
print(f'Você digitou os números {num}')
#  Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {num.count(9)} vezes')
#  Em que posição foi digitado o primeiro valor 3
if 3 in num:
    print(f'O número 3 está na {num.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posicão')
#  Quais são os números pares
print('Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
