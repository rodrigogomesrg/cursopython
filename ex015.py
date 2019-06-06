dias = int(input('Dias alugados: '))
kms = int(input('Kms rodados: '))
calcdias = dias * 60
calckms = kms * 0.15
print(f'Valor das diários: R${calcdias:.2f}')
print(f'Valor da Kms: R${calckms:.2f}')
