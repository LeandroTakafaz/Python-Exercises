"""
Exercício Python N°2:
Criar um programa para armazenar nome e salário de 20 pessoas. Calcular
e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir
uma listagem numerada com nome e novo salário.
"""

nomes = []
salarios = []

for i in range(20):
    nome = input("Digite o nome da pessoa: ")
    nomes.append(nome)
    
    salario = float(input("Digite o salário da pessoa: "))
    salarios.append(salario)
    
novos_salarios = [salario * 1.08 for salario in salarios]

print("Listagem de Salários Reajustados:")
for i in range(20):
    print(f"{i+1}. {nomes[i]} - Novo Salário: R${novos_salarios[i]:.2f}")