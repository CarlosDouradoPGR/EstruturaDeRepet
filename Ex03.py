while True:
    nome = str(input('Digite o nome: ')).strip()
    if len(nome) < 3:
        while len(nome) < 3:
            nome = str(input('O nome precisa ter mais que 3 caractéres!'))
    idade = int(input('Digite a idade: '))
    if not 0 < idade <150:
        while not 0 < idade <150: 
            idade = int(input('Digite um número entre 0 e 150: '))
    salario = int(input('Digite o salário: '))
    if salario <= 0:
        while salario <= 0:
            salario = int(input('Digite um salário maior que 0: '))
    sexo = str(input('Digite o sexo[M/F]')).strip().upper()
    if sexo not in 'FM':
        while sexo not in 'FM':
            sexo = str(input('Digite valores válidos: '))
print('Dados aceitos')

    