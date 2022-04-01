bse = int(input('Digite a base: '))
exp = int(input('Digite o expoente: '))
mult = 1
for p in range(1,exp+1):
    mult = mult * bse
    print(mult)