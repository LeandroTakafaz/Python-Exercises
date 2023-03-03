"""
Exercício Python N°3:
Criar um programa que leia o preço de compra e o preço de venda de 100
mercadorias. O programa deverá imprimir quantas mercadorias
proporcionam:
a. lucro < 10%
b. 10% <= lucro <= 20%
c. lucro > 20%
"""

preco_compra = [0] * 100
preco_venda = [0] * 100
lucro_abaixo_10 = 0
lucro_10_20 = 0
lucro_acima_20 = 0

for i in range(100):
    preco_compra[i] = float(input(f"Digite o preço de compra da mercadoria {i+1}: "))
    preco_venda[i] = float(input(f"Digite o preço de venda da mercadoria {i+1}: "))

for i in range(100):
    lucro = (preco_venda[i] - preco_compra[i]) / preco_compra[i] * 100

    if lucro < 10:
        lucro_abaixo_10 += 1
    elif lucro >= 10 and lucro <= 20:
        lucro_10_20 += 1
    else:
        lucro_acima_20 += 1

print(f"Quantidade de mercadorias com lucro abaixo de 10%: {lucro_abaixo_10}")
print(f"Quantidade de mercadorias com lucro entre 10% e 20%: {lucro_10_20}")
print(f"Quantidade de mercadorias com lucro acima de 20%: {lucro_acima_20}")