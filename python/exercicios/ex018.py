import math

valor = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(valor)) 
cos = math.cos(math.radians(valor))
tan = math.tan(math.radians(valor))

print(f'O ângulo de {valor} tem o SENO de {sen:.2f}')
print(f'O ângulo de {valor} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {valor} tem a TANGENTE de {tan:.2f}')