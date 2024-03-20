aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
print('-' * 30)
for c, v in aluno.items():
    print(f'-{c} é igual a {v}')
