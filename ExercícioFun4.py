"""
Exercício Python N°4:
Criar o programa que deixe entrar com nome e idade de 20 pessoas e
armazene em um vetor todos os nomes que comecem pela letra do intervalo
L - S.
"""

nomes = []
idades = []

for i in range(5):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    if nome[0].lower() >= 'l' and nome[0].lower() <= 's':
        nomes.append(nome)
        idades.append(idade)

print("Nomes que começam com as letras de L a S:")
for nome in nomes:
    print(nome)