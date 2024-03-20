número = int(input('Me diga um número qualquer: '))
if número % 2 == 0: #O sinal de porcentagem significa o resto da divisão. Nesse caso ele quer saber se  resto da divisão com 2 é 0?
    print(f'{número} é um número PAR')
else:
    print(f'{número} é um número ÍMPAR')