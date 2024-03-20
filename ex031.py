distância = float(input('Qual a a distância da viagem? '))
valor = 0.50 * distância
oferta = 0.45 * distância
print(f'Você está prestes a começar uma viagem de {distância}Km. ')
if distância <= 200:
    print(f'O preço de sua passagem será  de R${valor:.2f}')
else:
    print(f'O preço de sua passagem será R${oferta:.2f}')
