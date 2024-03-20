maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input(f'Peso da {pessoas}ª pessoa: '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso  # Se o peso so segundo ou maior laço for maior que o primeiro. Então ele passa a ser o maior.
        if peso < menor:
            menor = peso
print(f'O(A) mais BALEIA dessa lista pesa {maior}Kg')
print(f'O(A) mais lombriga dessa lista pesa {menor}Kg')
