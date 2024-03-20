""" Com a funçao enumerate podemos ampliar as funcionalidades de 'for' facilmente.
Vejamos como imprimir uma lista, em que teremos o índice entre os colchetes 
e o valor a sua direita(sem o enumerate):"""
l = [5, 9, 13]
x = 0
for e in l:
    print(f'na posicao {x}, temos {e}')
    x += 1

#  Vejamos o mesmo programa utilizando a funcao enumerate:
lista = [5, 9, 13]
for x, e in enumerate(lista):
    print(f'Na posição {x} temos {e}')


#  Outro exemplo:
numeros = []
for cont in range(1, 6):
    numeros.append(int(input('Digite um número: ')))
print(f'Essa é a lista {numeros}')
for posicao, valor in enumerate(numeros):
    print(f'Na posição {posicao} encontrei o valor {valor}')

"""A funcao enumerate gera uma tupla em que o primeiro valor é o índice
e o segundo valor é um elemento da lista sendo enumerada.
Ao utilizarmos 'x, e' em 'for' indicamos que o primeiro valor da tupla deve 
ser colocado em x, e o segundo valor da tupla deve ser colocado em e.
Assim, na primeira iteração teremos a tupla (0,5), em que x = 0 e e = 5.
Isso  é possível porque o Python permite o desempacotamento de valores de uma tupla,
atribuindoo um elemento da tupla a cada variável em for.
O que temos a cada iteração for é equivalente a x, e = (0,5),
em que o gerador eumerate retorna cada vez uma nova tupla.
Os próximos valores retornados são (1, 9) e respectivamente (2, 13)"""
