carteira = float(input('Quanto de dinheiro você tem?: R$'))
taxadolar = float(input('Taxa atual do dolar: R$'))
conversor = carteira * taxadolar
print(f'Com R${carteira:.2f} você compra US${conversor:.2f}')
