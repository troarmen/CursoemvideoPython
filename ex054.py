from datetime import date
atual = date.today().year
totmaior = 0  # Total de maiores de idade
totmenor = 0  # Total de menores de idade
for pessoa in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu?: '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1  # Se a idade for maior ou igual a 21, temos mais uma pessoa maior de idade.
    else:
        totmenor += 1  # Caso contrário temos mais uma pessoa menor de idade
print(f'Ao todo tivemos {totmaior} pessoas maior de idade.')
print(f'E também tivemos {totmenor} pessoas menor de idade.')
