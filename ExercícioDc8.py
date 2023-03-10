"""
Exercício Python N°8:
Faça um programa que lê as duas notas parciais obtidas 
por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  O algoritmo deve mostrar na tela as notas, a média, o conceito 
  correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou 
  “REPROVADO” se o conceito for D ou E.
"""

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

média = nota1 + nota2
média = média / 2

if média >= 9.0 and média == 10:
    print('--Média de Aproveitamento--')
    print('Sua média é: ',média,' Nota A')
    print('Aprovado')

if média >= 7.5 and média < 9:
    print('--Média de Aproveitamento--')
    print('Sua média é: ',média,' Nota B')
    print('Aprovado')

if média >= 6.0 and média < 7.5:
    print('--Média de Aproveitamento--')
    print('Sua média é: ',média,' Nota C')
    print('Aprovado')

if média >= 4.0 and média < 6.0:
    print('--Média de Aproveitamento--')
    print('Sua média é: ',média,' Nota D')
    print('Reprovado')

if média < 4.0  and média >= 0:
    print('--Média de Aproveitamento--')
    print('Sua média é: ',média,' Nota E')
    print('Reprovado')

elif média < 0 or média > 10:
    print('O valor da nota é invalido')