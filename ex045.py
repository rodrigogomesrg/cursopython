#eu deveria ter considerado o computador e ter criado um else no final
#com isso não teria como dar erro de input do usuário
#assim quando o input não for 1, 2 ou 3, retornaria uma jogada invalida

from random import randint
from time import sleep

print('Pedra - Papel - Tesoura')
print('-'*30)
computador = randint(1, 3)
print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
      ''')
player = int(input('Você escolhe...: '))
sleep(0.5)
if player == 1:
    print('Jogador: PEDRA')
    if computador == 1:
        sleep(1)
        print('Computador: PEDRA')
        sleep(1)
        print('Empate!!!')
    elif computador == 2:
        sleep(1)
        print('Computador: PAPEL')
        sleep(1)
        print('Computador venceu!!!')
    elif computador == 3:
        sleep(1)
        print('Computador: TESOURA')
        sleep(1)
        print('Você venceu!!!')

if player == 2:
    print('Player: PAPEL')
    if computador == 1:
        sleep(1)
        print('Computador: PEDRA')
        sleep(1)
        print('Você venceu!!!')
    elif computador == 2:
        sleep(1)
        print('Computador: PAPEL')
        sleep(1)
        print('Empate!!!')
    elif computador == 3:
        sleep(1)
        print('Computador: TESOURA')
        sleep(1)
        print('Computador venceu!!!')
if player == 3:
    print('Player: TESOURA')
    if computador == 1:
        sleep(1)
        print('Computador: PEDRA')
        sleep(1)
        print('Computador venceu!!!')
    elif computador == 2:
        sleep(1)
        print('Computador: PAPEL')
        sleep(1)
        print('Você venceu!!!')
    elif computador == 3:
        sleep(1)
        print('Computador: TESOURA')
        sleep(1)
        print('Empate!!!')
if player >=4:
    print('Escolha errada. Tente novamente')
