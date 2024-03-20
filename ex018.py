from math import sin, radians, cos, tan
ângulo = float(input('Digite um  número: '))
seno   = sin(radians(ângulo))
print(f'O ângulo de {ângulo}, tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo}, tem o COSSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo}, tem a TANGENTE de {tangente:.2f}')

