sal = float(input('Qual o valor do seu salário? R$'))

novoSal = sal + (sal*15/100)

print(f'O seu salário de R${sal}, com 15% de aumento, passa a ser R${novoSal:.2f}')