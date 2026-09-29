# Exercício 5 - Conversor de Tempo de Maratonista

total_segundos = int(input("Tempo total de treino (em segundos): "))

horas = total_segundos // 3600
minutos = total_segundos % 3600 // 60
segundos = total_segundos % 60

print(horas, "hora(s),", minutos, "minuto(s) e", segundos, "segundo(s)")
