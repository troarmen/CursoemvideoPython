cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')


n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma entre os números equivale a {s}')

# Essa última resolução usa o 'break'. Já que o 999 é o meu flag(Ponto de parada), ele não deve contar(ser incluído na soma)
# Então nessse caso eu criei um loop infinito para que o flag n se inclua na variável 's'. Se n for igual a 999 ele sai do loop automaticamente