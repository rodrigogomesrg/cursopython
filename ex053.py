frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
if inverso == juntar:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
