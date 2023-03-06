"""
Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por
7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.
"""

for num in range(5, 100):
    if (num % 7 == 0 and num % 5 != 0):
        print(num)