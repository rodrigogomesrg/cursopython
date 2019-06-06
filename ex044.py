vcompra = float(input('Valor da compra: R$'))
print('''
[1] A vista no dinheiro
[2] A vista no cartão
[3] Parcelado em até 2x no cartão
[4] Parcelado em 3x ou mais no cartão
      ''')
parcela = int(input('Opição de pagamento: '))

if parcela == 1:
    valor = vcompra - (vcompra * 10 / 100)
    print('Pagamento a vista no dinheiro: 10% de desconto')
    print(f'Valor da compra: R${vcompra:.2f}')
    print(f'Total a pagar com desconto: R${valor:.2f}')
elif parcela == 2:
    valor = vcompra - (vcompra * 5 / 100)
    print('Pagamento a vista no cartão: 5% de desconto')
    print(f'Valor da compra: R${vcompra:.2f}')
    print(f'Total a pagar com desconto: R${valor:.2f}')
elif parcela == 3:
    print('Pagamento em até 2x no cartão: valor integral')
    print(f'Total a pagar: R${vcompra:.2f}')
elif parcela == 4:
    valor = vcompra + (vcompra * 20 / 100)
    print('Pagamento em 3x ou mais no cartão: juros de 20%')
    print(f'Valor da compra: R${vcompra:.2f}')
    print(f'Total a pagar com juros: R${valor:.2f}')
else:
    print('Opição inválida. Tente novamente')
