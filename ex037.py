numero = int(input('Digite um número: '))
print('Escolha uma das opções:')
print('''
[1] Converter em binário
[2] Converter em octal
[3] Converter em hexadecimal
''')
escolha = int(input('Digite a opção: '))

if escolha == 1:
    print(f'{numero} convertido para binário: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para Octal: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para Hexadecimal: {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente')
