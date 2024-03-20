"""dicio = {'titulo' : 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'}
dicio2 = {'titulo' : 'Sla',
        'ano': 1977,
        'diretor': 'George Lucas'}
lista = [ ]
lista.append(dicio)
lista.append(dicio2)
print(lista[1]['titulo'])

pessoas = {'nome': 'Trô', 'sexo': 'M', 'idade': 14}
pessoas['peso'] = 98.5
a = type(pessoas['peso'])
print(a)
for k , v in pessoas.items():
        print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0].values())"""

brasil = []
estado = {}
cont = 0
for c in range(0, 3):
        estado['uf'] = str(input('Unidade Federativa: '))
        estado['sigla'] = str(input('Sigla do estado: '))
        brasil.append(estado.copy())
print('-' * 30)
"""for cont in range(0, 3):
        for e, s in brasil[cont].items():
                print(f'{e} = {s}')"""

"""for e in brasil:
        for chave, valor in e.items():
                print(f'{chave} = {valor}')"""
for e in brasil:
        for valor in e.values():
                print(valor, end=' ')
        print()

