inserirnome = str(input('Seu nome: ')).strip()
print(f'Seu nome em maiúscula: {inserirnome.upper()}')
print(f'Seu nome em minúscula: {inserirnome.lower()}')
print(f'Seu nome tem ao todo {len(inserirnome) - inserirnome.count(" ")} letras')
print(f'Seu primeiro nome tem: {inserirnome.find(" ")} letras')
