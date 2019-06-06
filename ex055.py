maiorPeso = menorPeso = 0

for pesos in range(0, 5):
    pesopessoa = float(input(f'Informe o peso da {pesos+1}º pessoa: '))
    if pesos == 0:
        maiorPeso = pesopessoa
        menorPeso = pesopessoa
    if pesopessoa >= maiorPeso:
        maiorPeso = pesopessoa
    if pesopessoa <= menorPeso:
        menorPeso = pesopessoa

print(f'O menor peso é de {menorPeso}kg.')
print(f'O maior peso é de {maiorPeso}kg.')
