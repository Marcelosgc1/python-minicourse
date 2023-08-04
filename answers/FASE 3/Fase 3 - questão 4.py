# QUESTÃO 4
YI = int(input('Informe o nível de poder de Yuji Itadori, entre 1 e 10: '))
MF = int(input('Informe o nível de poder de Megumi Fushiguro, entre 1 e 10: '))

for i in range(10):
    MF-=1
    if(MF==0) and YI!=0:
        print("Yuji Itadori venceu")
    YI-=1
    if(YI==0) and MF!=0:
        print("Megumi Fushiguro venceu")
