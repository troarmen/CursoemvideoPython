# Faça um programa que calcule a soma entre todos os
# números que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for k in range(1, 501, 2):
    if k % 3 == 0:
        soma += k  # É a mesma coisa que s = s + k
        cont += 1  # É  a mesma coisa que cont = cont + 1
print(f'A soma entre todos os {cont} valores solicitados é {soma}')