print(25 * '-')
print('CAIXA REGISTRADORA')
print(25 * '-')
soma = 0
cont = 0


while True:
    prd = float(input('Digite o valor do produto: '))
    print('Digte [0] para somar e encerrar a nota)')
    soma += prd
    if prd == 0:
        print('O valor total foi: R${:.2f}'.format(soma))
        break
mny = float(input('Dinheiro: R$ '))
print('Troco: {:.2f}'.format(mny - soma))
    

