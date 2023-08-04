# QUESTÃO 1
senha = input('Crie uma senha: ')
p=0
while senha != p:
    p=input('Insira sua senha: ')
    if p!=senha:
        print('Você NÃO inseriu a senha correta!')
    else:
        print('Você logou corretamente!')
