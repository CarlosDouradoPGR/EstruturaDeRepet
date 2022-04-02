n = int(input('Quantas notas deseja digitar '))
soma = 0
cont = 0
for m in range(1, n+1):
    numb = int(input(f'Digite a {m}º nota: '))
    soma += numb
    cont +=1
print(f'A média das notas é {soma/cont}')