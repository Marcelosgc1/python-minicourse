# QUESTÃO 10
escala = input('Informe em que escala está a temperatura [C para Celsius e F para Fahrenheit]: ').upper()
temp = float(input('Informe a temperatura: '))
if(escala == 'C'):
    print(f'em Fahrenheit a temperatura é de {round((temp*9/5)+32, 2)} graus')
elif(escala == 'F'):
    print(f'em Celsius a temperatura é de {round((temp-32)*5/9, 2)} graus')
else:
    print('Por favor, use "C" ou "F" para indicar a escala da temperatura')