"""
Exercício Python N°1:
Faça um programa em linguagem Python, que lê um 
número n e imprime os n primeiros números da sequência de Fibonacci.
"""

print('\t ---- Sequência de Fibonacci---- ')
termos = int(input("Digite a quantidade de termos para calcular : "))

#começando com 0 e 1
num1, num2 = 0, 1
contador = 0

while contador < termos:
    num3 = num1 + num2
    # Atualizando valores
    num1 = num2
    num2 = num3
    contador += 1
    print(num1)
