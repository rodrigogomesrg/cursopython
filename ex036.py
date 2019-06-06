valor = int(input('Valor do imóvel: R$'))
renda = int(input('Renda mensal: R$'))
anospagar = int(input('Quantidade de anos para pagamento: '))

prestacao = valor / (anospagar * 12)
limitepres = (renda * 30) / 100

if prestacao > limitepres:
    print(f'Valor da prestação R${prestacao:.2f}')
    print('Financiamento NÃO APROVADO!')
else:
    print(f'Valor da prestação R${prestacao:.2f}')
    print('Financiamento APROVADO')
