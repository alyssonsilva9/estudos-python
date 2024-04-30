import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#h1 = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)

print(f'A hipotenusa vai medir: {hi}')