from random import randint
from time import sleep
computador = randint(0, 6)
print('=-'*24)
print('Pensei em um número entre 0 e 5. Tente advinhar')
print('=-'*24)
escolha = int(input('Digite seu número: '))
print('PROCESSANDO...')
sleep(2)
if escolha != computador:
    print(f'Computador escolheu {computador}')
    sleep(0.3)
    print('Você perdeu')
else:
    print(f'Computador escolheu {computador}')
    sleep(0.3)
    print('Você venceu')
sleep(0.3)
print('Obrigado por jogar')
