"""
Exercício Python N°6:
Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

#solicita o valor dos produtos para o usuário.
prod1 = float(input('Informe o valor do primeiro produto: '))
prod2 = float(input('Informe o valor do segundo produto: '))
prod3 = float(input('Informe o valor do terceiro produto: '))

#confere qual dos produtos tem o menor valor.
if prod1 < prod2 and prod1 < prod3:
    print('Você deve comprar o primeiro produto no valor de', prod1)

if prod2 < prod1 and prod2 < prod3:
    print('Você deve comprar o segundo produto no valor de', prod2)

if prod3 < prod2 and prod3 < prod1:
    print('Você deve comprar o terceiro produto no valor de', prod3)

if prod1 == prod2 and prod1 == prod3:
    print('Os três produtos possuem o mesmo valor, compre qual preferir')
