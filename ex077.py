tupla = ('aprender', 'programar', 'linguagem', 'python',
        'curso', 'gratis', 'estudar', 'praticar',
        'trabalhar','mercado', 'programador', 'futuro')
        
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos, ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
