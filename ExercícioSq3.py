'''
Exercício Python N°3:
Faça um programa em Python que leia um valor inteiro 
e mostre a tabuada de 1 a 10 do valor lido.
'''

num = int(input('Informe o valor inteiro: '))

for cont in range(1,11):
    print('resultado de',num,'*',cont,'=',num*cont)
    print('-'*20)