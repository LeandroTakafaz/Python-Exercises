'''
Exercício Python Nº3:
Faça um programa que peça dois números e imprima o maior deles.
'''

# Ler os números solicitados pelo usuário
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

# Teste para saber o número maior
if num1 > num2:
    print('O maior valor digitado é: ',num1)
    
if num1 == num2:
    print('os valores são iguais')

# Mensagem caso os números sejam iguais
else:
    print('O maior valor digitado é: ', num2)