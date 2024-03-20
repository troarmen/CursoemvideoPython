dicio = dict()
lista = list()
mulheres = []
maiores = []
idades = 0
continuar = ' '
while continuar not in 'N': 
    dicio['nome'] = str(input('Nome: '))
    dicio['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
    while dicio['sexo'] not in 'MF':
        print('ERRO! Digite apenas M ou F')
        dicio['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
    dicio['idade'] = int(input('Idade: '))
    lista.append(dicio.copy())
    dicio.clear()
    continuar = str(input('Deseja continuar[S/N]? ')).upper()[0]
    while continuar not in 'SN':
        print('ERRO! Digite apenas S ou N')
        continuar = str(input('Deseja continuar[S/N]? ')).upper()[0]
# Calculando a idade média entre as pessoas
for idade in range(0, len(lista)):
    idades += lista[idade]["idade"]
media = idades / len(lista)
# Calculando as mulheres
for mu in lista:
    if mu['sexo'] == 'F':
        mulheres.append(lista[mu]['nome'])
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média entre as idades é {media}')
print(f'C) As mulheres cadastradas foram:', end=' ')
for mulher in mulheres:
    print(mulher.capitalize(), end=', ')

for idadem in range(0, len(lista)):
    if lista[idadem]['idade'] > media:
        maiores.append(lista[idadem])

print('D) Lista das pessoas que estão acima da média: ')
cont = 0
for p in range(0, len(maiores)):
    print('   ', end=' ')
    for k, v in maiores[p].items():
        print(f'{k} = {v};', end=' ')
        cont += 1
        if cont == 3:
            print()
