print('-'*30)
print('BANCO TAK')
print('-'*30)
valor = int(input('Quanto você quer sacar? R$'))
total = valor
cedula = 50
totalcedula = 0 
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('-'*30)
print('Muito obrigado por optar pelo BANCO TAK. Volte sempre!')
