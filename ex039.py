from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} já tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    alistamento = 18 - idade
    ano = atual + alistamento
    print(f'Ainda faltam {alistamento} anos para seu alistamento.')
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    alistamento = idade - 18
    ano = atual - alistamento
    print(f'Já deveria ter se alistado há {alistamento} anos ')
    print(f'Seu alistamento foi em {ano}')
