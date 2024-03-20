from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opcao = int(input('Qual é sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2}, é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produte de {n1} x {n2}, é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
            print(f'Entre {n1} e {n2}, o maior é {maior}')
        elif n1 == n2:
            print('Não tem maior, os dois números são iguais.')
    elif opcao == 4:
        print('Informe os números: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('FINALIZANDO...')
    else:
        print('Opção inválida... Tente novamente')
    sleep(2)
    print('=-='*10)
print('FIM do programa, volte sempre!')
