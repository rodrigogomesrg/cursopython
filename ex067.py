while True:
    numero = int(input('Informe o número: '))
    for multiplicador in range(1, 10):
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    if continuar == 'n':
        break
