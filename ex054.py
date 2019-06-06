from datetime import date
counterMaior = counterMenor = 0

for cadastro in range(0, 7):
    anoNascimento = int(input(f'Digite o ano de nascimento da {cadastro+1}º pessoa: '))
    idade = date.today().year - anoNascimento
    if idade <= 17:
        counterMenor += 1
    else:
        counterMaior += 1
print(f'Temos ao todo, {counterMenor} menores de idade.')
print(f'Temos ao todo, {counterMaior} maiores de idade.')
