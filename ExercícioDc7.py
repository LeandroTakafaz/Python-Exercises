"""
Exercício Python N°7:
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input('Informe o seu salário: '))

if salario <= 280:
    aumento = salario * 0.2
    novo_sal = aumento + salario

    print('\nSeu salário era de: ',salario)
    print('\nSeu salário aumentou em 20%')
    print('\nEsse é o aumento do seu salario: ',aumento)
    print('\nSeu novo salário é de: ',novo_sal)

if salario > 280 and salario <= 700:
    aumento = salario * 0.15
    novo_sal = aumento + salario

    print('\nSeu salário era de: ',salario)
    print('\nSeu salário aumentou em 15%')
    print('\nEsse é o aumento do seu salario: ',aumento)
    print('\nSeu novo salário é de: ',novo_sal)

if salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    novo_sal = aumento + salario

    print('\nSeu salário era de: ',salario)
    print('\nSeu salário aumentou em 10%')
    print('\nEsse é o aumento do seu salario: ',aumento)
    print('\nSeu novo salário é de: ',novo_sal)


if salario > 1500:
    aumento = salario * 0.05
    novo_sal = aumento + salario

    print('\nSeu salário era de: ',salario)
    print('\nSeu salário aumentou em 5%')
    print('\nEsse é o aumento do seu salario: ',aumento)
    print('\nSeu novo salário é de: ',novo_sal)