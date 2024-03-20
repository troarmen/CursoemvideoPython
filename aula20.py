"""def linha():
    print('-' * 30)


def mensagem(b):
    linha()
    print(b)
    linha()


for c in range(0, 3):
    a = input('Digite uma frase: ')
    mensagem(a)
"""


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B é igual a {s}')


soma(4, 5)
soma(8, 9)


def multiplique(a, b):
    print(a * b)


multiplique(45656645, 3123123123)


def contador(*num):
    print(num)
    print(type(num))  # Retorna o tipo da variável(no caso é uma tupla)
    
    
""" Ao criar a funcao contador nomeei o parâmetro como num.
Mas antes do num tem um astrísco. Oq esse asterísco significa?
Quando eu uso o asterísco eu digo ao python que eu não sei quantos
elementos o usuário vai passar. O usuário pode dar 1 valor ou 10000 valores,
o python vai simplesmente armazenar tudo dentro dessa variável composta(num, no caso).
Obs: O formato em que num fica é uma tupla."""
contador('Zaven', 'Trô', 'Murilo')


valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos += 1
        

dobra(valores)
print(valores)
