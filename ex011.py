a = int(input('Quantos metros de altura tem a parede de seu quarto? '))
b = int(input('Quantos metros de largura tem a parede de seu quarto? '))
c = a * b
#considerando que c é igual a 40 metros quadrados e que a cada 2m quadrados é necessário 1l de tinta, então:
d = c/2
print(f'Já que sua parede tem {a}m de altura e {b}m de largura, sua área é {c}m quadrados ')
print(f'Então para pintar a parede, serão necessários {d} litros de tinta')