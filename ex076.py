tupla = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)

print('-' * 39)
print(f'{"MATERIAIS ESCOLARES":^39}')
print('-' * 39)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R${tupla[pos]:.2f}', end='\n')
print('-' * 39)
