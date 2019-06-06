frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {frase.count("a")}')
print(f'A letra A aparece primeiro na posição {frase.find("a")+1}')
print(f'A letra A aparece por ultimo na posição {frase.rfind("a")+1}')
