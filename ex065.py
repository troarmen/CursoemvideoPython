resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1 
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar?[S/N] ')).upper().strip()
media = soma / quantidade
print(f'Você digitou {quantidade} números, e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')
