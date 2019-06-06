print('-'*30)
print('Calculadora de tinta')
print('-'*30)
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
m2 = largura * altura
qtytinta = m2 / 2
print(f'Sua parede tem {m2}m² e vai precisar de {qtytinta:.0f}lt de tinta.')
