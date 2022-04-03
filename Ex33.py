import numpy as np

soma = 0
cont = 0
lst = []
while True:
    temp = float(input(f'Digite a temperatura em C '))
    ch = str(input('Deseja continuar?[S/N]: ')).upper()
    lst += [temp]
    cont += 1
    soma += temp
    if ch == 'S':
        continue
    elif ch == 'N':
        break
    elif ch not in 'SN':
        while ch not in 'SN':
            print('Valor inválido!')
            ch = str(input('Tente novamente: ')).upper()
print(f'A maior temperatura foi {max(lst)}')
print(f'A menor temperatura foi {min(lst)}')
print(f'A média entre as temperaturas foi {soma / cont}')
