soma = maior = menor = contador = 0
while True:
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if contador == 1:
        maior = numero
        menor = numero
    if numero >= maior:
        maior = numero
    if numero <= menor:
        menor = numero
    if continuar == 'n':
        break
media = soma / contador
print(f'Média dos {contador} números: {media:.2f}')
print(f'O maior número foi {maior} e o menor é {menor}')
