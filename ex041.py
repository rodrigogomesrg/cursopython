from datetime import date

anonasc = int(input('Informe o ano de nascimento: '))
idade = date.today().year - anonasc

if idade <= 9:
    print(f'Sua idade é {idade} e sua categoria é MIRIM.')
elif 10 <= idade <=14:
    print(f'Sua idade é {idade} e sua categoria é INFANTIL')
elif 15 <= idade <= 19:
    print(f'Sua idade é {idade} e sua categoria é JUNIOR')
elif 20 <= idade <= 25:
    print(f'Sua idade é {idade} e sua categoria é SÊNIOR')
else:
    print(f'Sua idade é {idade} e sua categoria é MASTER')
