primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for counter in range(primeiro, decimo + razao, razao):
    print(f'{counter}', end=' → ')
print('FIM!')
