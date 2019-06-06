salario = float(input('Salário atual R$'))
aumento = int(input('Aumento %: '))
calc = (salario*aumento/100) + salario
print(f'Salário atual de R${salario:.2f}')
print(f'Aumento de {aumento}%: R${calc:.2f}')
