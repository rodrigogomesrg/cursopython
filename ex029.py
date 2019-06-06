velocidade = int(input('Velocidade do veículo: '))

if velocidade <= 80:
    print(f'Velocidade registrada {velocidade}km/s. Situação OK!')
else:
    limite = velocidade - 80
    print(f'Velocidade registrada {velocidade}km/s. {limite}km/s ACIMA DO LIMITE!')
    print(f'Gerando multa no valor de R${limite*7}.')
