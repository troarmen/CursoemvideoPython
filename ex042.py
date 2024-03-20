r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Será possível formar um triângulo com os seguintes segmentos', end='')
    if r1 == r2 == r3:
        print('EQULÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima não formam um triângulo')
# No primeiro if eu adiconei DENTRO DELE mais um if, umm elife um else. Pois eu tenho duas opço~es apenas,
# se formar triângulo ou não. E se caso formar eu tenho tais alternativas. Dúvidas assistir aula do ex042 do curso em
# video.
