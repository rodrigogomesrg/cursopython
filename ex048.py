soma = contador = 0
for counter in range(1, 501, 2):
    if counter % 3 == 0:
        soma += counter
        contador += 1
print(f'A soma dos {contador} números ímpares multiplos de 3 é: {soma}')
