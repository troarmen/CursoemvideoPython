# Esse fatiamento no upper, pega só a primeira letra. Então se a pessoa escrever "masculino" ou "feminino", só a inicial
sexo = str(input('Por favor informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
