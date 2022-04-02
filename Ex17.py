n = int(input('Digite um número para saber o seu fatorial: '))
mult = 1
cont = 0

 
for f in range(1 ,n+1):
    numb = f * (f-cont)
    cont += 1
    mult *= numb
    print(mult)