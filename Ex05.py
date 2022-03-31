paisA = int(input('Digite o número de habitantes do 1º país: '))
taxaA = float(input('Digite a taxa de crescimento do 1º país: '))
paisB = int(input('Digite o número de habitantes do 2º país: '))
taxaB = float(input('Digite a taxa de crescimento do 2º país: '))
cont = 0
while paisA <= paisB:
    paisA += paisA * (3/100)
    paisB += paisB * (1.5/100)
    cont += 1
    
print(f' serão nessesários {cont} anos para a população de habitantes se igualar')