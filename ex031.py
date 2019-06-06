distancia = int(input('Distância da viagem: '))

if distancia <= 200:
    print(f'A distância da viagem é de {distancia}.')
    print(f'Valor da passagem R${distancia*0.50}.')
else:
    print(f'A distância da viagem é de {distancia}.')
    print(f'Valor da passagem R${distancia*0.45}')
