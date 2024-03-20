total18 = totalh = totalM20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo in 'M':
        totalh += 1
    if sexo in 'F' and idade < 20:
        totalM20 += 1
    resposta = ' '
    print('-'*30)
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    print('-'*30)
    if resposta in 'N':
        break
print(f'No total temos {total18} pessoas maiores de idade')
print(f'Ao todo temos {totalh} homens cadastrados')
print(f'No total temos {totalM20} mulheres abaixo de 20 anos')
