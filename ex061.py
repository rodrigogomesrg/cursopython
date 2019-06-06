numero = int(input('Digite o termo: '))
passo = int(input('Digite o passo: '))

termo = numero
count = 1

while count <= 10:
    print(f'{termo} → ', end='')
    termo += passo
    count += 1
