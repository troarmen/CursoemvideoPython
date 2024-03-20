from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classifcação: INFANTIL')
elif idade <= 19:
    print('Classifcação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('Classificação: MASTER.')
