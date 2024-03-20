# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual é o valor da casa? R$'))
salário = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos a casa será financiada? '))
mínimo = salário * 30 / 100
financiamento = valor / (anos * 12)  # Ao multiplicar os anos por 12, descobrimos os meses em que a casa será financiada. Depois dividimos o total e descobrimos o valor mensal
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${financiamento:.2f} ')
if financiamento <= mínimo:
    print('Infelizmente o empréstimo foi NEGADO.')
else:
    print( 'Parabéns, seu empréstimo foi aprovado! ')
