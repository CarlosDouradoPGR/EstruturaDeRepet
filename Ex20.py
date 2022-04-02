
while True:
    st = str(input('Digite um número interio, positivo e menor que 16 para saber o seu fatorial: '))
    intei = st.isnumeric()
    if intei == True:
        n = int(st)
    mult = 1
    cont = 0
    if st == 'sair':
        break
    elif n > 16:
        print('Valor maior que 16!!')
        print('Tente Novamente!!')
    elif intei == False:
        print('Não é um número inteiro!!')
        print('Tente novamente!!')
   
    if n <=16 and intei == True:
        for f in range(1,n+1):
            numb = f * (f-cont)
            cont += 1
            mult *= numb
            print(mult)
    print('Digite "sair" para encerrar')