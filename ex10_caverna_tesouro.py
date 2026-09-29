# Exercício 10 - Caverna do Tesouro (Divisão de Saque)

moedas = int(input("Total de moedas de ouro: "))
exploradores = int(input("Número de exploradores: "))

por_explorador = moedas // exploradores
sobra_lider = moedas % exploradores

print("Cada explorador recebe:", por_explorador, "moedas")
print("Bônus do líder:", sobra_lider, "moedas")
