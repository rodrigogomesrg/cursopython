from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)
print(f'CO={co} CA={ca} hipotenusa é {hip:.4f}')
