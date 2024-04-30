import random

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')

aluno = [aluno1, aluno2, aluno3, aluno4] 
escolhido = random.choice(aluno)

print(f'O aluno escolhido foi: {escolhido}')