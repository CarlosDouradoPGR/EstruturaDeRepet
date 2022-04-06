wage = 1000
data0 = 1995
data1 = 2022
anos = data1 - data0
aumento = 1.5/100
juros = 1
liq = (aumento * wage)
for s in range(1, anos + 1):
    newage = wage + (liq * juros)
    juros *= 2

print(f'{newage:.2f}')
print(wage)



