nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

if media <= 4.9:
    print(f'A média das notas foi: {media}')
    print('Aluno foi REPROVADO')
elif 5.0 <= media <= 6.9:
    print(f'A média das notas foi: {media}')
    print('Aluno está em RECUPERAÇÃO')
else:
    print(f'A média das notas foi: {media}')
    print('O aluno foi APROVADO')
