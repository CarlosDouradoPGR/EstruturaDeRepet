paisA = 80000
paisB = 200000
cont = 0
while paisA <= paisB:
    paisA += paisA * (3/100)
    paisB += paisB * (1.5/100)
    cont += 1
    
print(f' serãp nessesários {cont} para a população de habitantes se igualar')