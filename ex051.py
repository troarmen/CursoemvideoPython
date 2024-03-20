# Minha resolução:
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(10):
    print(primeiro + (razao * c), end=' ➙ ')
print('FIM')

# Resolução do Professor:
first = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth = first + (10 - 1) * reason
for c in range(first, tenth + reason, reason):
    print(f'{c} ', end='➙ ')
print('Acabou')
