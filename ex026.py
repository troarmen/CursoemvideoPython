frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "a", aparece {frase.count("A")} vezes na frase.')
print(f'A primeira vez que ela aparece, está na posição {frase.find("A") + 1}')
print(f'E  a última vez que ela aparece, está na posição {frase.rfind("A") + 1}')
