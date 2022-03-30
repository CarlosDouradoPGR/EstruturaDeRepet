while True:
    numb = int(input('Digite um número entre 0 e 10: '))
    if  not 0 <= numb <= 10 :
        print('Valor ínvalido tennte novamente.')
    else:
        break
print(f'O número digitado foi {numb}')

