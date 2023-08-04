# QUESTÃO 4
numero = int(input('Insira o número do qual você quer a tabuada: '))
primeiro = int(input('Insira o valor inicial: '))
segundo = int(input('Insira o valor final: '))
while True:
    print(f'{numero} X {primeiro} = {numero*primeiro}')
    primeiro+=1
    if primeiro==segundo+1:
        break