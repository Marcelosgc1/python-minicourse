# QUESTÃO 1
N1 = int(input('Informe um número: '))
N2 = int(input('Informe um número: '))

for i in range(N1, N2):
    if(i%7==0):
        print(i, end=' ')