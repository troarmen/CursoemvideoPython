#Fatiamento = Range
frase = 'Curso em vídeo Python '
print(len(frase))
print(frase[9::3])

#Análise
print(frase.count('o', 0, 13))
print(frase.count, len )
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

#Divisão
print(frase.split())
print('-'.join(frase))

dividido = frase.split()
print(dividido[3])