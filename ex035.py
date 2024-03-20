print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Será possivel formar um triângulo coms os seguintes SEGUIMENTOS')
else:
    print('NÃO será possivel formar um triângulo com os seguintes SEGUIMENTOS')