# QUESTÃO 8
preço = float(input('Informe o preço da compra: '))
grana = float(input('Informe o dinheiro dado pelo cliente: '))
if(preço<=grana):
    print(f'O troco será de {round(grana-preço, 2)}R$')
else:
    print('O dinheiro não é suficiente')