"""teste = []
teste.append("Gustavo")
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 19
galera.append(teste)
print(galera)"""

"""pessoas = [["João", 19], ["Maria", 22], ["Pedro", 30]]

for pessoa in pessoas:
    print(pessoa[0])"""

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        totmai += 1
        if totmai == 0:
            print("Não há maiores de idade.")
    else:
        print(f"{pessoa[0]} é menor de idade.")
        totmen += 1
        if totmen == 0:
            print("Não há menores de idade.")

print(f"Existem {totmai} maiores de idade e {totmen} menores de idade.")
