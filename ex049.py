from time import sleep
número = int(input('Digite um número para ver sua tabuada: '))
print('Calma aí po to calculando... Se você não consegue fazer a conta, IMAGINA EU!')
sleep(5)
for c in range(1, 11):
    print(f'{número} x {c} = {número * c}')
print('Pronto, ta aí a cola da sua prova de mat. Tira um 10 pelo menos e dá orgulho pra sua mãe')
