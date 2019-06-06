maior = menor = contador = 0

for counter in range(0, 3):
    valor = int(input('Digite um valor: '))
    if contador == 0:
        maior = valor
        menor = valor
        contador += 1
    if valor >= maior:
        maior = valor
    if valor <= menor:
        menor = valor

print(f'O menor valor informado foi {menor}')
print(f'O maior valor informado foi {maior}')
