start = str(input('Pressione qualquer tecla para ver a tabela: '))


price = 1.99
soma = 0
for c in range(1, 51):
    soma += price
    print(f' [{c}]itens R$ {soma:.2f}')
