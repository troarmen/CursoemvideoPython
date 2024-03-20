print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
total = mais1000 = menor = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço do produto: R$'))
    contador += 1
    total += valor
    if valor > 1000:
        mais1000 += 1 
    if contador == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
    print('-'*30)
print('-'*15, 'FIM DO PROGRAMA', '-'*15)
print(f'O valor total da compra foi: R${total:.2f}')
print(f'Temos {mais1000} produtos que custam mais de R$1000,00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')