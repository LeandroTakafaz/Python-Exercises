'''
Exercício Python Nº3:
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

# Ler o nome
while True:

    nome = input('Informe seu nome: (Maior do que 3 caracteres ')
    if len(nome) > 3:
        break
    print('Seu nome deve ter mais do que 3 caracteres')

# Ler a idade    
while True:
    
    idade = int(input('Informe sua idade: (Entre 0 e 150) '))
    if idade > 0 and idade <= 150:
        break
    print('Sua idade deve estar entre 0 e 150')

# Ler o salário    
while True:
    
    salário = float(input('Informe o seu salário: '))
    if salário > 0:
        break
    print('Seu salário deve ser maior que 0')

# Ler o sexo    
while True:
    sexo = input('Informe o seu sexo: (m ou f) ')
    if sexo == 'M' or sexo == 'F':
        break
    print('O sexo deve ser m ou f')

# Ler o estado civil    
while True:
    Est_Civil = input('Informe seu estado civil (s, c, v, d) ')
    if Est_Civil == 's' or Est_Civil == 'c' or Est_Civil == 'v' or Est_Civil == 'd':
        break
    print('O seu estado civil deve ser colocado como s, c, v, d')

# Mostrar as informações válidas    
print('\nSeu nome é: ', nome)
print('\nSua idade é: ', idade)
print('\nSeu salário é: ', salário)
print('\nSeu sexo é: ', sexo)
print('\nSeu estado civil é: ', Est_Civil)
