lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or lista[-1] < num:
        lista.append(num)
    else:
        posicao = 0  #  Variável criada para varrer o vetor inteiro, posicao por posicao
        while posicao <= len(lista):  # Indica que vai fazer o loop até que posicao seja igual ao tamanho da lista
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1
print(lista)
