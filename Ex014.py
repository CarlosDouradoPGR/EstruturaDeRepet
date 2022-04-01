par = 0
impa = 0

for c in range(1,11):
    numb = int(input(f'Digite o {c}º número: '))
    if numb % 2 == 0:
        par += 1
    elif numb % 2 != 0:
        impa += 1
print(impa)
print(par)
