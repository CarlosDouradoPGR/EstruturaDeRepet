
cont025 = 0
cont2650 = 0
cont5175 = 0
cont76100 = 0


while True:
    numb = int(input('Digite um número entro 0 e 100: '))
    print('Números fora do intervalo irão encerrar o programa')
    if 0 < numb <= 25:
        cont025 += 1
    elif 25 < numb <= 50:
        cont2650 += 1
    elif 50 < numb <= 75:
        cont5175 += 1
    elif 75 < numb <= 100:
        cont76100 += 1
    elif numb > 100 or numb <0 :
        print('Valor fora do intervalo!!\n'
              'O programa será encerrado!!')
        break
print(f'{cont025} número estão entre o intervalo [0-25]\n'
      f'{cont2650} números estão entre o intervalo [26-50]\n'
      f'{cont5175} números estão entre o intervalo [51-75]\n'
      f'{cont76100} número estão entre o intervalo [76-100]')

