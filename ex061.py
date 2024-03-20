print('-=-'*10, 'GERADOR DE PA', '-=-'*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro  # Aqui ele mostra o termo
cont = 1  # E aqui ele vai contar quantos termos foram
while cont <= 10:
    print(f'{termo}  <  ', end='')
    termo += razao
    cont += 1
print('FIM')
