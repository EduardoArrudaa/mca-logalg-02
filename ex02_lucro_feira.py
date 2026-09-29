# Exercício 2 - Divisão de Lucro da Feira

total = float(input("Valor total arrecadado (R$): "))

guardado = total * 0.10
por_amigo = (total - guardado) / 3

print("Valor guardado para os limões: R$", guardado)
print("Cada amigo recebe: R$", por_amigo)
