from datetime import date

print('Sistema de avaliação de alistamento militar')
print('-'*44)

anonasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anonasc

if idade <= 17:
    tempoapresentar = (18 - idade) + date.today().year
    print(f'Você tem {idade} anos.')
    print('Você ainda não tem idade para ao alistamento.')
    print(f'Você deve se apresentar no ano de {tempoapresentar}')
elif idade == 18:
    print(f'Você tem {idade} anos.')
    print('Você precisa se apresentar ao serviço militar este ano.')
else:
    anoalistamento = date.today().year - (idade - 18)
    print(f'Você tem {idade} anos.')
    print('Você já passou da idade para o alistamento militar.')
    print(f'O ano que você deveria ter se apresentado foi em {anoalistamento}')
