"""
Exercício Python N°7:
Entrar com números reais para dois vetores A e B de dez elementos cada.
Gerar e imprimir o vetor diferença.
"""

A = []
B = []
diferenca = []

print("Digite os números do vetor A:")
for i in range(10):
    num = float(input(f"Digite o número {i+1}: "))
    A.append(num)

print("Digite os números do vetor B:")
for i in range(10):
    num = float(input(f"Digite o número {i+1}: "))
    B.append(num)

for i in range(10):
    dif = B[i] - A[i]
    diferenca.append(dif)

print(diferenca)