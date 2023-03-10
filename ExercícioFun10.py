"""
Exercício Python N°10:
Criar um programa que leia os elementos de um vetor com 20 posições e escreva-o. Em 
seguida, troque o primeiro elemento pelo último, o segundo pelo penúltimo, o 
terceiro pelo antepenúltimo, e assim sucessivamente. Mostre o vetor depois das trocas.
"""

vetor = []

# lê os elementos do vetor
for i in range(20):
    valor = int(input("Digite um valor para a posição {}: ".format(i)))
    vetor.append(valor)

print("Vetor antes da troca:", vetor)

# realiza as trocas de posição
for i in range(len(vetor) // 2):
    temp = vetor[i]
    vetor[i] = vetor[-i-1]
    vetor[-i-1] = temp

print("Vetor após as trocas:", vetor)