valor = int(input('Digite o valor do produto: R$'))
desconto = int(input('Desconto em %: '))
vdesconto = valor * desconto / 100
vfinal = valor - vdesconto
print(f'Valor total do produto: R${valor:.2f}')
print(f'Desconto de {desconto:.0f}%')
print(f'Valor do desconto é de R${vdesconto:.2f}')
print(f'Valor total a pagar é de R${vfinal:.2f}')
