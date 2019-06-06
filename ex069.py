idadeMaior = sexoMasculino = mulheresMenor20 = 0

while True:
    sexo = str(input('Informe o sexo [M/F]: ')).strip().lower()
    idade = int(input('Informe a idade: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    
    if idade >= 18:
        idadeMaior += 1
    
    if sexo == 'm':
        sexoMasculino += 1
    
    if sexo == 'f':
        if idade <= 19:
            mulheresMenor20 += 1
    
    if continuar == 'n':
        break

print(f'Temos {idadeMaior} pessoas maiores de 18 anos.')
print(f'Temos um total de {sexoMasculino} homens cadastrados.')
print(f'Temos um total de {mulheresMenor20} mulheres com menos de 20 anos.')
