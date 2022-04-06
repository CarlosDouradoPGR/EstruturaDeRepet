aluno_maior = ' '
alt_maior = 0
aluno_menor = ' '
alt_menor = 1000
for a in range(1, 11):
    nome = str(input('Digite o nome do aluno: '))
    altura = int(input('Digite a altura em centimetros: '))

    if altura > alt_maior:
        alt_maior = altura
        aluno_maior = nome
    if altura < alt_menor:
        alt_menor = altura
        aluno_menor = nome
print(f'O aluno com a maior altura possui {alt_maior}cm e se chama {aluno_maior}')
print(f'O aluno com a menor altura possui {alt_menor}cm e se chama {aluno_menor}')


