"""
Exercício Python N°5:
Ler um vetor vet de 10 elementos e obter um vetor w cujos componentes são
os fatoriais dos respectivos componentes de vet.
"""

import math

vet = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
w = []

for n in vet:
    w.append(math.factorial(n))

print(w)