km = float(input('Quantos Kilômetros o carro percorreu?: '))
dias = int(input('Por quantos dias o carro foi alugado?: '))
pago= (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${pago}')