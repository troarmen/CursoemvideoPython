from time import sleep


def mostraLinha():
    print('-=' * 25)
def contador(i, f, s):
    if s < 0:
        s *= -1
    elif s == 0:
        s = 1

    mostraLinha()
    print(f'Contagem de {i} até {f} de {s} em {s}')
    mostraLinha()
    sleep(2)
    
    cont = i
    if cont <= f:
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += s
        print('FIM!')
        mostraLinha()
    elif cont >= f:
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= s
        print('FIM!')
        mostraLinha()


contador(1, 10, 1)
contador(20, 10, 2)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
