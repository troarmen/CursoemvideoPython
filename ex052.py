number = int(input('Digite um número para ver se é primo: '))
total = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {number}, foi dividido {total} vezes')
if total == 2:
    print(f'{number} é um número primo')
else:
    print(f'{number} não é um número primo')

