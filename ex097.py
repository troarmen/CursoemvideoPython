def escreva(texto):
    char = len(texto) + 4
    print('~' * char)
    print(f'{texto:^{char}}')
    print('~' * char)
    
    
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
