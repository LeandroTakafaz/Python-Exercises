"""
Exercício Python N°1:
Criar um programa que armazene números em dois vetores inteiros de cinco
elementos cada. Gere e imprima o vetor soma.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

lista_soma = [lista1[i] + lista2[i] for i in range(5)]

print(lista_soma)