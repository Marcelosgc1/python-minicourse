# QUESTÃO 9
horas = int(input('Horas trabalhadas: '))
if(horas <= 40):
    print(f'Seu salário será {horas*8}R$')
else:
    print(f'seu salário será {320+(horas-40)*12}R$')