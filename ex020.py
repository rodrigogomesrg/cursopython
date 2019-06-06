from random import shuffle
alunos = list()
for counter in range(0, 4):
    nome = str(input('Nome do aluno: '))
    alunos.append(nome)
shuffle(alunos)
print(f'A ordem de apresentação é:')
print(f'{alunos} ')
