#desafio um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
nomes = print('Digite o nome dos alunos:')
a =str(input('Aluno 1: '))
b =str(input('Aluno 2: '))
c=str(input('Aluno 3: '))
d=str(input('Aluno 4: '))

import random 
lista = [a,b,c,d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')