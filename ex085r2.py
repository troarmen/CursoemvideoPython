lista = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)

print('-=' * 30)
print(f'Os números pares digtados foram: {sorted(lista[0])}')
print(f'Os números ímpares digitados foram: {sorted(lista[1])}')
