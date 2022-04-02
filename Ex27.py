qturmas = int(input('Digite a quantidade de turmas: '))
soma = 0
cont = 0

for t in range(1, qturmas + 1 ):
    alunos = int(input(f'Digite a quantidade de alunos da {t}º turma: '))
    if alunos <= 40:
        soma += alunos
        cont += 1
    else:
        print('Valor excede o número de alunos de uma turma')

print('A média de alunos por turma deve ser de {}'.format(soma//cont))