# Exercício 9 - Rendimento do Atleta

distancia_km = float(input("Distância percorrida (km): "))
tempo_min = float(input("Tempo gasto (minutos): "))

vel_kmh = distancia_km / (tempo_min / 60)
vel_ms = vel_kmh / 3.6

print("Velocidade média:", vel_kmh, "km/h")
print("Velocidade média:", vel_ms, "m/s")
