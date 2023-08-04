# QUESTÃO 3
aaa = -999999999
bbb = 999999999
while True:
    giosbfbned = input('Digite um número, se quiser parar digite "P": ')
    if giosbfbned == "P" or giosbfbned == "p":
        break
    if int(giosbfbned)>int(aaa):
        aaa = giosbfbned
    if int(giosbfbned)<int(bbb):
        bbb = giosbfbned
print(f'{aaa} é o maior dos números inseridos')
print(f'{bbb} é o menor dos números inseridos')
