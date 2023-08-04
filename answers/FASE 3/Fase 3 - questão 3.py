# QUESTÃO 3
N = int(input("Digite um número: "))
for i in range(2,N+1):
    abc = 0
    for j in range(2,i):
        if i%j == 0:
            abc = 1
            break
    if abc == 0:
        print(i)