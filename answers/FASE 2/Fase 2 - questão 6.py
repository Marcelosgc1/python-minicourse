# QUESTÃO 6
carrinho = float(input('Digite o valor total da compra: '))
if(carrinho>199):
    print(f'Com a promoção, o valor final a ser pago será de {round(carrinho-(carrinho/20), 2)}R$')
else:
    print(f'Infelizmente, a promoção não se aplica em sua compra, o valor final será de {carrinho}R$')