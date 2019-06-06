somaIdade = counter = maiorIdadeH = mulhermenos20 = 0
nomeHomemMaior = ' '

for cadastro in range(0, 3):
    print(f'---{cadastro+1}º pessoa---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] '))
    somaIdade += idade
    counter += 1
    if counter == 0 and sexo in 'Mm':
        maiorIdadeH = idade
        nomeHmemMaior = nome
    if sexo in 'Mm' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeHomemMaior = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
        
mediaIdade = somaIdade / counter
print(f'A média de idade do grupo é de {mediaIdade:.0f} anos.')
print(f'O homem mais velho é {nomeHomemMaior} e ele tem {maiorIdadeH} anos.')
print(f'Ao todo temos {mulhermenos20} mulheres com menos de 20 anos.')
