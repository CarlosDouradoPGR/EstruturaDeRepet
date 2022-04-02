jovem = 0
adulto = 0
idoso = 0
media = 0
cont = 0
soma = 0
while True:
    idade = int(input('Digite a idade(0 para encerrar): '))
    soma += idade
    cont += 1
    
    if 0 < idade < 26:
        print('Jovem')
        jovem += 1
    elif 26 <= idade < 60:
        print('Adulto')
        adulto += 1
    elif idade > 60: 
        print('Idoso')
        idoso += 1
    if idade == 0:
        break 
media = soma / cont
if 0 < media < 26:
    turma = 'Jovens'
elif 26 <= media < 60:
    turma = 'Adultos'
elif media > 60: 
    turma = 'Idosos'

print(f'A turm é formada em sua maiória por {turma}')