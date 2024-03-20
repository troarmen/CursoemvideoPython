velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Você está multado! Você excedeu o limite de 80KM/h')
    multa = (velocidade - 80) * 7 #Velocidade menos o limite(80), multiplicados por 7 é o valor da multa. Ou seja 7 reais por cada KM ultrpassado
    print(f'Você deverá pagar uma multa de R${multa:.2f}')
else:
    print('Tenha um bom dia, e dirija conscientemente.')