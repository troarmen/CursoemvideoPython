from math import sqrt
co = float(input('Qual o comprimento do cateto oposto?: '))
ca = float(input('Qual o comprimento do cateto adjacente?: '))
hi = (co ** 2) + (ca ** 2)
raiz = sqrt(hi)
print(f'A hipotenusa vale {raiz:.2f}')
