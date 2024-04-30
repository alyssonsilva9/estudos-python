valor = float(input('Qual o valor do produto? R$'))

desconto = valor - (valor*5/100)

print(f'O produto de R${valor}, com um desconto de 5% vai custar R${desconto:.2f}')