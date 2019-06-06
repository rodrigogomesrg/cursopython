salario = int(input('Informe o salário: R$'))
salario15 = ((salario * 15) / 100) + salario
salario10 = ((salario * 10) / 100) + salario

if salario <= 1250:
    print(f'Aumento de 15%. Novo salário: R${salario15}')
else:
    print(f'Aumento de 10%. Novo salário: R${salario10}')
