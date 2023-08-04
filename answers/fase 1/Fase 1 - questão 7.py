# QUESTÃO Nº 7
A = int(input("O numero de naves no quadrante e: "))
B = int(input("O numero de naves amigas a frente e: "))
C = int(input("O numero de naves amigas a direita e: "))
D = int(input("O numero de naves amigas a esquerda e: "))
E = int(input("O numero de naves amigas atras e: "))

aliados = B+C+D+E
inimigos = A-aliados
print(f"o numero de naves inimigas e {inimigos}")
