s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'Os seguimentos podem formar um triângulo.')
else:
    print(f'Os seguimentos não podem formar um triângulo.')