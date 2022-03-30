while True:
    nome = str(input('Digite o nome de usuário:\n'))
    senha = str(input('Digite sua senha:\n'))
    if nome == senha:
        print('nome idêntico a senha, tente novamente')
    else:
        break
print('Bem vindo!')