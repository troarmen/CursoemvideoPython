nome = str(input('Digite seu nome completo: ')).strip()
divisão = nome.split()
print('Prazer em te conhecer!')
print(f'Seu primeiro nome é,  {divisão[0]}')
print(f'Seu último nome é,  {divisão[-1]}')
'''A função len() conta elementos por isso ela inicia do 1...
Já as posições na lista iniciam do
0. Por isso vc tem que adequar o valor retornado por len().
Ex:
A = ['a', 'b', 'c']
Posições dos elementos
'a' posição 0
'b' posição 1
'c' posição 2
Função len(A)
3 <- número de elementos presentes na lista.
Então se vc quer encontrar o 'c' posição 2, basta fazer len(A) que é 3, len(A) - 1 = posição 2'''
