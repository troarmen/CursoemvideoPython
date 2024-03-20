lista = []
continuar = ' '
while continuar not in 'N':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar?[S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).upper()[0]
    
print(f'{"No.":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, d in enumerate(lista):
    print(f'{i:<4}{d[0]:<10}{d[2]:>8}')
print('-' * 25)
while True:
    opcao = int(input('Mostrar notas de qual aluno?(999 interrompe) '))
    if opcao == 999:
        break
    if opcao <= len(lista) - 1:
        print(f'Notas de {lista[opcao][0]}, são {lista[opcao][1]}')
