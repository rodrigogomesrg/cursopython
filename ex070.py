contador = totalCompra = produtoMil = menorValor = 0
produtoBarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    continuar = str(input('Deseja continuar? [S/N]: '))
    totalCompra += valor
    contador += 1
    
    if valor >= 1000:
        produtoMil += 1

    if contador == 1:
        menorValor = valor
        produtoBarato = produto
    
    if valor <= menorValor:
        menorValor = valor
        produtoBarato = produto
    
    if continuar == 'n':
        break
print(f'Total da compra foi de R${totalCompra:.2f}')
print(f'Temos ao total {produtoMil} produtos valendo mais de R$1000.00')
print(f'O produto mais barato foi {produtoBarato} no valor de R${menorValor:.2f}')
