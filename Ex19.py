
soma = 0




while True:
    numb = float(input('Digite um numéro para ser somado: '))
    soma += numb
    ch = str(input('Deseja continuar?[S/N]: ')).lower()
    if ch == 's':
        continue
    elif ch == 'n':
        break
    elif ch not in 'sn':
        while ch not in 'sn':
            ch = str(input('Alnternativa inválida tente novamente: '))
        if ch == 'n': 
            break    
    
print(f'A soma dos número digitado é {soma}')