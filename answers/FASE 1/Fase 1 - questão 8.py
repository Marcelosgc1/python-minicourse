# QUESTÃO Nº 8
P1 = int(input("Quantos pokemons da regiao de Kanto estao registrados na pokedex? "))
P2 = int(input("Quantos pokemons da regiao de Johto estao registrados na pokedex? "))
P3 = int(input("Quantos pokemons da regiao de Hoenn estao registrados na pokedex? "))
D1 = int(input("Quantos pokemons novos da regiao de Kanto foram descobertos? "))
D2 = int(input("Quantos pokemons novos da regiao de Johto foram descobertos? "))
D3 = int(input("Quantos pokemons novos da regiao de Hoenn foram descobertos? "))

K = P1+D1
J = P2+D2
H = P3+D3

print(f"Estao registrados {K} pokemons em Kanto!")
print(f"Estao registrados {J} pokemons em Johto!")
print(f"Estao registrados {H} pokemons em Hoenn!")

