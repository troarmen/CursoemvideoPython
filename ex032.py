from datetime import date
ano = int(input('Digite o ano que quer analisar: Coloque 0 se quiser analizar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano BISSEXTO.')
else:
    print(f'{ano} NÃO é um ano BISSEXTO.')
#Ocorre a de 4 em 4 anos. Ao em vez do ano ter 365 dias, te, 366. Para descobrir se o ano é bissexto basta ver se ele é multiplo de 4
#exceto anos que são múltiplo de 100 mas que não são múltiplos de 400