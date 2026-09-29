# Exercício 3 - Consumo de Ração do Pet

saco_kg = float(input("Peso do saco de ração (kg): "))
consumo_g = float(input("Consumo diário do cão (g): "))

sobra_g = saco_kg * 1000 - consumo_g * 5

print("Ração restante após 5 dias:", sobra_g, "g")
