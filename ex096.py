valores = [1, 2, 3, 4, 5, 6, 7, 8, 9,
           10, 11, 12, 13, 14, 15, 16]
tamanho = int(len(valores))
def mostraLinha(txt):
    print('-' * 30)
    print(f'{txt:^tamanho}')
    print('-' * 30)
    
    
def area(l, c):
    area = l * c
    print(f'A área de um terreno de {l}x{c} é igual a {area}m²')

mostraLinha('CONTROLE DE TERRENOS')
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)
