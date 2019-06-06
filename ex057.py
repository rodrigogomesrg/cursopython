sexo = str(input('Informe seu sexo [F/M]: ')).strip().lower()
while sexo not in 'fm':
    sexo = str(input('Dados inválidos, digite novamente: ')).strip().lower()
print(f'Sexo {sexo} cadastrado com sucesso')
