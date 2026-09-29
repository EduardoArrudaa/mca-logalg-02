# Exercício 4 - Painel Solar e Economia

paineis = int(input("Quantidade de painéis instalados: "))
preco_kwh = float(input("Valor do kWh (R$): "))

kwh_mes = paineis * 1.2 * 30
economia = kwh_mes * preco_kwh

print("Energia gerada em 30 dias:", kwh_mes, "kWh")
print("Economia no mês: R$", economia)
