lst = []
soma = 0
for n in range(1,6):
    numb = int(input('Digite o {} número: '.format(n)))
    lst += [numb]
    soma = numb + soma
print(f'o maior número é {max(lst)}')
print(f'A média entre os números é {soma/5}')