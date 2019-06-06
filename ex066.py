soma = quantidade = 0

while True:
    numero = int(input('Informe um número: [999 PARAR]'))
    if numero != 999:
        soma += numero
        quantidade += 1
    else:
        break

print(f'Total de {quantidade} número e a soma deles é: {soma}')
