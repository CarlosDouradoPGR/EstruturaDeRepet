cds = int(input("Quantos CD's foram comprados: "))
cont = 0
soma = 0

for c in range(1, cds + 1):
    price = float(input("Qual valor gasto no {}º CD's: R$ ".format(c)))
    cont += 1
    soma += price 

print(f'O valor médio gasto em cada CD foi R$ {soma/cont:.2f} e o valor total do investimento foi de R$ {soma:.2f}')