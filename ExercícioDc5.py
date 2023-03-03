'''
Exercício Python N°5:
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

#solicita as notas do usuário
num1 = int(input('Informe a primeira nota: '))
num2 = int(input('Informe a segunda nota: '))

#calcula a média das notas
média = num1 + num2
média = média / 2

#Compara a média do resultado para aprovação
if média >= 7 and média < 10:
    print('Aprovado')

if média < 7:
    print('Reprovado')

if média == 10:
    print('Aprovado com Distinção') 