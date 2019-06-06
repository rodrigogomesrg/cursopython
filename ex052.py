numero = int(input('Digite um número: '))
total = 0
for counter in range(1, numero + 1):
    if numero % counter == 0:
        print('→', end='')
        total += 1
    else:
        print('', end='')
    print(f'{counter}', end=' ')
print(f'\nO número {numero} foi dividido {total} vezes.')
if total == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')
