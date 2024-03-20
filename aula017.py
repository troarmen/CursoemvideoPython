lanche = ['a', 'b', 'c', 'd']
"""lanche[2] = 'e'  #  Está substituindo o valor da chave 2, por 'e'
lanche.append('e')  #  Está adicionando o valor 'e' na lista
lanche.insert(2, 'e')  #  Está inserindo o valor 'e' na chave 2
del lanche[3]  #  Está deletando o elemento na chave 3
lanche.pop()    #  Se vc n indicar um índice ele apaga o último elemento da lista
lanche.pop(2)    #  Agr que eu indiquei ele faaz a mesma função do 'del' 
lanche.remove('a')  #  Existe o remove tamb;em que ao invés de vc indicar o índica vc indica o elemento


valores = list(range(4, 11))  #  Outra maneira de criar uma lista
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()  #  Organizando a lista do menor para o maior
valores.sort(reverse = True)  #  Oragnizando a lista do maior para o menor 
print(len(valores))  #  Está escrevendo na tela a quantidade de casas que tem na lista



valores = []  #  Uma lista vazia
valores.append(5)  #  Adicionei o valor 5 à lista ent valores = [5]
valores.append(9)  #  Adicionei o valor 9 à lista ent valores = [5, 9]
valores.append(4)  #  Adicionei o valor 4 à lista ent valores = [5, 9, 4]
for chave, valor in enumerate(valores):  #  Aq está mostrando a chave do elemento(onde se encontra) do lado do valor
    print(f'Na posição {chave} encontrei o valor {valor}')"""



valores = [1, 2, 3, 2]

while 2 in valores:
    valores.remove(2)
print(valores)

lista = ['ave', 'maria', 'doido', 'dx o like',
        'se inscreve', 'tmj']
for palavra in lista:
    print(palavra)
    for letra in palavra:
        print(letra)


numeros = []
for cont in range(1, 6):
    numeros.append(int(input('Digite um número: ')))
print(f'Essa é a lista {numeros}')
for posicao, valor in enumerate(numeros):
    print(f'Na posição {posicao} encontrei o valor {valor}')
