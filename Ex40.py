maior_i = 0
menor_i = 9**14
maior_cy = ' '
menor_cy = ' '
cont = 0
contmenos2v = 0
somav = 0
somac = 0
somamenos2v = 0
for e in range(1, 4):
    city = str(input('Digite o nome da cidade: '))
    veic = int(input('Digite o número de veículos de passeio: '))
    acidentes = int(input('Digite o número de acidente com vítimas: '))
    indice = veic/acidentes
    somav += veic
    cont = 1
    if indice > maior_i:
        maior_cy = city
        maior_i = indice
    if indice < menor_i:
        menor_cy = city
        menor_i = indice
    if veic <= 2000:
        somamenos2v += veic
        contmenos2v += 1
mediav = somav/cont
mediamenos2v = somamenos2v/contmenos2v
print(f'A cidade que possui o maior índice de acidentes é {maior_cy} que corresponde a {maior_i:.2f}')
print(f'A cidade que possui o menor índice de acidentes é {menor_cy} que corresponde a {menor_i:.2f}')
print(f'A média de veiculos entre as cidades é {mediav:.2f}')
print(f'A média de veiculos entre as cidadede com menos de 2000 veiculos é {mediamenos2v:.2f}')

