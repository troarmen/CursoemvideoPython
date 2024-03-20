times = ('INTERNACIONAL', 'FLAMENGO', 'ATLÉTICO-MG',	
        'SÃO PAULO', 'FLUMINENSE', 'GRÊMIO', 
        'PALMEIRAS', 'CORINTHIANS', 'BRAGANTINO',
        'SANTOS', 'ATHLETICO', 'ATHLETICO - GO', 
        'CEARÁ', 'SPORT', 'FORTALEZA',
        'BAHIA', 'VASCO', 'GOIÁS',
        'CORITIBA', 'CHAPECOENSE')

#  5 primeiros times
print('-' * 20)
print('CINCO PRIMEIROS TIMES')
print(times[:5])
print('-' * 20)
#  4 últimos times

print('QUATRO ÚLTIMOS TIMES')
print(times[-4:])
print('-' * 20)
#  Times em ordem alfabética
print('EM ORDEM ALFABÉTICA')
print(sorted(times))
print('-' * 20)
#   Em que posição está o time da Chapecoense
print('POSIÇÃO CHAPECOENSE')
print(f'Está na {times.index("CHAPECOENSE")} posição')
print('-' * 20)
