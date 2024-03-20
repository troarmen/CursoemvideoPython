lista = []
total = []
pares = []
impares = []
for c in range(1, 8):
    total.append(int(input(f'Digite o {c} valor: ')))

for numero in total:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

lista.append(total[:])
lista.append(pares[:])
lista.append(impares[:])

print('-=' * 30)
print(f'Os números pares digtados foram: {sorted(lista[1])}')
print(f'Os números ímpares digitados foram: {sorted(lista[2])}')
