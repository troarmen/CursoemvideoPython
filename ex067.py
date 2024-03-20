while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-' * 15)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 15)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')