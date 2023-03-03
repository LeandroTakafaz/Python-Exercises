"""
Exercício Python N°8:
Criar um programa que leia um vetor A de dez valores e 
construa outro vetor B, da seguinte forma: A 3 8 4 2...5. B 9 4 12 1...15
"""

# lê o vetor A
A = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor de A: "))
    A.append(valor)

# constrói o vetor B
B = []

for i in range(10):
    if i % 2 == 0: 
        valor = A[i] * 3
    else:
        valor = A[i] /2
    B.append(valor)

# exibe os vetores A e B
print("Vetor A:", A)
print("Vetor B:", B)