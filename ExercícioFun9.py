"""
Exercício Python N°9:
Criar um programa que leia dois vetores A e B, contendo, cada um, 25
elementos inteiros. Intercale esses dois conjuntos (A[1] / B[1] / A[2] / B[2] /...),
formando um vetor V de 50 elementos. Imprima o vetor V.
"""

A = []
B = []
V = []

n = int(input("Digite o tamanho dos vetores A e B: "))

print("Digite os valores do vetor A:")
for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    A.append(num)

print("Digite os valores do vetor B:")
for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    B.append(num)

for i in range(n):
    V.append(A[i])
    V.append(B[i])

print("Vetor intercalado: ", V)