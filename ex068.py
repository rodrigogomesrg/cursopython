from random import randint

vComputador = vJogador = 0
print('-' * 35)
print('PAR ou ÍMPAR - Vença com 3 vitórias')
print('-' * 35)
while True:
    numero = int(input('Escolha um número: '))
    escolha = str(input('Par ou Ímpar [P/I]: ')).strip().lower()
    computador = randint(0, 10)
    resultado = numero + computador
    if escolha == 'p':
        if resultado % 2 == 0:
            vJogador += 1
            print(f'Computador escolheu {computador}')
            print('Resultado foi PAR. Você venceu a rodada')
            print(f'Jogador {vJogador} x {vComputador} Computador')
            print(' ')
        else:
            vComputador += 1
            print(f'Computador escolheu {computador}')
            print('Resultado foi ÍMPAR. Computador venceu a rodada')
            print(f'Jogador {vJogador} x {vComputador} Computador')
            print(' ')
    if escolha == 'i':
        if resultado % 2 == 0:
            vComputador += 1
            print(f'Computador escolheu {computador}')
            print('Resultado foi PAR. Computador venceu a rodada')
            print(f'Jogador {vJogador} x {vComputador} Computador')
            print(' ')
        else:
            vJogador += 1
            print(f'Computador escolheu {computador}')
            print('Resultado foi ÍMPAR. Você venceu a rodada')
            print(f'Jogador {vJogador} x {vComputador} Computador')
            print(' ')
    if vJogador == 3 or vComputador == 3:
        break
print('Fim da partida')
print(f'Resultado: Jogador{vJogador} x {vComputador}Computador')
if vJogador == 3:
    print('VOCÊ VENCEU!!!')
elif vComputador == 3:
    print('VOCÊ PERDEU!!!')
