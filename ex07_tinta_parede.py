# Exercício 7 - Tinta para Pintura de Parede

largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))

area = largura * altura
litros = area / 3

print("Área da parede:", area, "m²")
print("Tinta necessária:", litros, "litro(s)")
