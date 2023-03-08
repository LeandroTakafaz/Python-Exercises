'''
Exercício Python Nº2:
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    # Ler o nome de usuário e a senha
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    
    # Verificar se a senha é igual ao nome de usuário
    if password == username:
        print("Erro: A senha não pode ser igual ao nome de usuário.")
        continue  # pedir novamente as informações
    
    # Se chegou aqui, as informações são válidas
    break  # sair do loop

# Mostrar as informações válidas
print("Nome de usuário:", username)
print("Senha:", password)
