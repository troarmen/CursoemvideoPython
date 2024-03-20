print('-=-'*10, 'GERADOR DE PA', '-=-'*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro  # Aqui ele mostra o termo
cont = 1  # E aqui ele vai contar quantos termos foram
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}  <  ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos à mais, você quer mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados.')
