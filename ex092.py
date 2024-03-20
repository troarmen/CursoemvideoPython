from datetime import datetime
dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dicionario['idade'] = datetime.now().year - ano_nasc
dicionario['cpts'] = int(input('Carteira de trabalho(0 não tem): '))
if dicionario['cpts'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: R$ '))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dicionario.items():
    print(f'{k.capitalize()} tem valor {v}.')
