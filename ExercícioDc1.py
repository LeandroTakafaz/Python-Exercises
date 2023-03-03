'''
Exercício Python N°1: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais 
velho e quantas mulheres têm menos de 20 anos.
'''

soma = 0
cont_F = 0
media = 0
maior = 0
nome_velho = ''

for cont in range(1,5):

    nome = input('Digite seu nome: ')
    sexo = input('Masculino ou Feminino?  [M/F]').upper()[0]
    idade = int(input('Digite sua idade:'))
    print('-'*20)

    soma = soma + idade
    media = soma / cont

    if sexo == 'M' and idade > maior:
        maior = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        cont_F += 1

    print('Média das idades é de {:.2f} '.format(media))
    print('Nome do mais velho é {} '.format(nome_velho))
    
    if cont_F == 0:
        print('Não temos mulheres no grupo!')

    else:
        print('Temos um total de {} mulheres com menos de 20 anos'.format(cont_F))