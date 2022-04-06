divida = int(input('Digite o valor da dívida: '))
print('Simulação de pagamento')

juros = 0
cont = 10
valorf = 0
parcelas = 0
for j in range(3,13,3):
    if j == 3:
        print(f'R${divida}       ---->       {juros}       ---->      1     ----->  R${divida}')
    juros = divida * cont / 100
    valorf = divida + juros
    parcelas = valorf/j
    print(f'R${valorf}     ---->     {juros}     ---->     {j:2}     ----->  R${parcelas:.2f}')
    cont += 5


