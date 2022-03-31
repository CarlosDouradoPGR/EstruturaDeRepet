lst = []
for n in range(1,6):
    numb = int(input('Digite o {} número: '.format(n)))
    lst += [numb]
print(f'o maior número é {max(lst)}')


