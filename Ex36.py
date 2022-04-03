m1 = int(input('Digite onde a tabuada inicia: '))
m2 = int(input('Digite onde a tabuada termina: '))
numb = int(input('Digite um número para saber a tabuada: '))
for t in range(m1, m2 + 1):
    print(f'{numb:2} X {t:2} = {t*numb:2}')