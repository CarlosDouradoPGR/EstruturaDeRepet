n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = 0
for t in range(n1,n2+1):
    print(t, end='->') 
    soma += 1
print(f' a soma entre todos os números é {soma}')