expressao = str(input('Digite a expressão: '))
contadorA = expressao.count('(')
contadorB = expressao.count(')')
if contadorA == contadorB:
    print('Sua expressão é válida!')
elif contadorA != contadorB:
    print('Sua expressão está errada!')
