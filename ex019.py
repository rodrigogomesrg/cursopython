from random import choice
lista = list()
for counter in range(0, 5):
    aluno = str(input('Nome do aluno: '))
    lista.append(aluno)
sorteio = choice(lista)
print(f'O aluno sorteado foi {sorteio}')
