setNome = str(input('Digite seu nome: ')).strip()
getNome = setNome.split()
print(f'Seu primeiro nome é {getNome[0]}')
print(f'Seu ultimo nome é {getNome[len(getNome)-1]}')
