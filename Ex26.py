print('Digite A para votar no cadidato Armando')
print('Digite C para votar no candidato Carlos')
print('Digte F para votar no candidato Felipe')

eleit = int(input('Digite a quantidade de eleitores: '))
contA = 0
contC = 0
contF = 0
nulo = 0

for c in range(1, eleit + 1):
    cand = str(input('Digite em qual candidato deseja votar[A/C/F]:  ')).upper()
    if cand == 'A':
        contA += 1
    elif cand =='C':
        contC += 1
    elif cand == 'F':
        contF += 1
    elif len(cand) > 0 or cand not in 'ACF' :
        print('Voto foi considerado nulo')
        nulo += 1
print(f'A quantidade de eleitores do candidado A foi {contA}')
print(f'A quantidade de eleitores do candidado C foi {contC}')
print(f'A quantidade de eleitores do candidato F foi {contF}')
print(f'A quantidade de votos nulos {nulo} foi')