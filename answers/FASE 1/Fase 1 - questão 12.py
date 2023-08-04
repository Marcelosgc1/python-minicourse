# QUESTÃO Nº 12
import math

vida = int(input("Digite o total de HP do monstro: "))
dado1 = int(input("Digite o valor tirado no primeiro D20: "))
dado2 = int(input("Digite o valor tirado no segundo D20: "))
dano = math.floor(math.sqrt(5*dado1)+math.pi**(dado2/3))

print(f"A vida restante do monstro é {vida-dano}!")
