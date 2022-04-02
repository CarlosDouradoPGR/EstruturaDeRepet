numb = int(input('Digite um número para saber se ele é primo: '))
cont = 0

for p in range(1, numb + 1):
    if numb % p == 0:
        lst += [p]
        cont += 1 
if cont == 2:
    print('É primo')
else:
    print('Não é primo')