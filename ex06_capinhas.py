# Exercício 6 - Fabricação de Capinhas de Celular

quantidade = int(input("Quantidade de capinhas produzidas: "))
preco_venda = float(input("Preço de venda unitário (R$): "))

custo_total = quantidade * 5.80
lucro = quantidade * preco_venda - custo_total

print("Custo total de produção: R$", custo_total)
print("Lucro líquido do lote: R$", lucro)
