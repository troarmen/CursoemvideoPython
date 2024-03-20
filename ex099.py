from time import sleep

def mostraLinha():
    print('-=' * 30)


def analisar(* num):
    mostraLinha()
    print('Analisando os valores passados...')
    sleep(2)
    cont = maior = 0
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    mostraLinha()
        

analisar(2, 9, 4, 5, 7, 1)
analisar(4, 7, 0)
analisar(1, 2)
analisar(6)
analisar()
