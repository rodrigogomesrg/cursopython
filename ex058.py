from random import randint

computador = randint(0, 10)
print('Acabei de pensar em um número.')
counter = 0
while True:
    player = int(input('Tente advinhar qual foi: '))
    counter += 1
    if player > computador:
        print('Foi um número menor')
    elif player < computador:
        print('Foi um número maior')
    else:
        break

print(f'Você acertou com {counter} tentativas.')
