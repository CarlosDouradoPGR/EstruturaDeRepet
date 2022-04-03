lstg = []
lsta = []
lstcod = []
while True:
    print(15*'=', 'Digite novos dados', 15*'=')
    cod = int(input('Digite seu código de 4 números: '))
    if cod >= 9999:
        print('Valor inválido!!')
        cod = int(input('Digite o código novamente: '))
    lstcod += [cod]
    altura = int(input('Digite sua altura em cm: '))
    lsta += [altura]
    peso = float(input('Digite seu peso em Kg: '))
    lstg += [peso]
    ch = str(input('Deseja continuar? [S/N]: ')).upper()
    if ch not in 'SN':
        while ch not in 'SN':
            ch = str(input('Valor inválido, tente novamente[S/N]: ')).upper()
    if ch == 'N':
        break
    elif ch == 'S':
        continue
print(30*'-=')
print(f'O codigo dos cliente que participaram do senso é {lstcod} ')
print(f'O cliente mais gordo possui Kg {max(lstg):.2f}\n'
      f'O cliente mais magro possui Kg {min(lstg):.2f}')
print(f'O maior cliente possui {max(lsta)/100} metros\n'
      f'O menor cliente possui {min(lsta)/100} metros')
print(30*'-=')
print(f'A média de altura entre os clients em metro é {((sum(lsta) / len(lsta))/100):.2f}')
print(f'A média de peso entre os clientes é Kg{(sum(lstg) / len(lstg)):.2f}')
