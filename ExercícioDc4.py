'''
Exercício Python N°4:
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
# Solicita o valor para o usuário
valor = int(input('Digite um valor: '))

#testa se o valor é positivo ou negativo
if valor > 0:
    print('O valor', valor, 'é positivo')

else:
    print('O valor', valor, 'é negativo')