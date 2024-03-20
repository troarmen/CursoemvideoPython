lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('Vou comer muito!')



"""a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c)
print(c.count(5))  # Conta quantas vezes o número 5 aparece na tupla 'c'
print(c.index(8))  # Diz a posiçao dO número 8 na tupla c
pessoa = 'Gustavo', 'M', 99.8
del(pessoa)  #  A funcao 'del' serve para apagar qualquer coisa em python, nesse caso foi a tupla"""
