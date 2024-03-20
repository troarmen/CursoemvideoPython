nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))
média = (nota1 + nota2) / 2
print(f'Sua média é de {média}')
if média < 5:
    print('Você está REPROVADO.')
elif 5 <= média <= 6.9:
    print('Você está de RECUPERAÇÃO.')
elif média >= 7:
    print('Parabéns, você está APROVADO.')
