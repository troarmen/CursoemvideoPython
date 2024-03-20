peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('PARABÉNS. Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está SOBREPESO. Seu grau de obesidade é 1.')
elif 30 <= imc < 40:
    print('Você é considerada uma pessoa OBESA. Seu grau de obesidade é 2.')
else: # ou poderia ter feito asssim elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA. Seu grau de obesidade é 3.')
