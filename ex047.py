print('-=-' * 10, 'NÚMERO PARES ENTRE 1 E 50', '-=-' * 10)
for p in range(2, 51, 2):
    print(p, end=' ')
# A primeira resolução é mais prática e gasta menos do processador. Pois eu apenas digo para o computador
# ir do número 2 até o 50 pulando de 2 em 2, ou seja só fiz um loop/laço de 25 vezes.
# A segunda resolução o computador fazia o laço/loop(ou seja dividia por 2) e se não fosse par, ele não mostrava na tela
# Isso faz com que eu acabasse fazendo o dobro de laços e pesaria mais no precesador.

'''for p in range(1, 51):
    if p % 2 == 0:
        print(p , end='  ')
print('Acabou')'''