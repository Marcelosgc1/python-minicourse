# QUESTÃO 3
aaa = -999999999
bbb = 999999999
while True:
    numero = input('Digite um número, se quiser parar digite "P": ')
    if numero == "P" or numero == "p":
        break
    if int(numero)>int(aaa):
        aaa = numero
    if int(numero)<int(bbb):
        bbb = numero
print(f'{aaa} é o maior dos números inseridos')
print(f'{bbb} é o menor dos números inseridos')
