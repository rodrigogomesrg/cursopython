soma = 0

for counter in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos números pares é: {soma}')
