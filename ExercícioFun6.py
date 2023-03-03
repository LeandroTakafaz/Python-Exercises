"""
Exercício Python N°6:
Entrar com números inteiros em um vetor A [50]. Gerar e imprimir o vetor B
onde cada elemento é o quadrado do elemento, na respectiva posição, do
vetor A.
"""

A = []
B = []

for i in range(50):
    num = int(input(f"Digite o número {i+1}: "))
    A.append(num)
    B.append(num**2)

print(f"Vetor A: {A}")
print(f"Vetor B: {B}")