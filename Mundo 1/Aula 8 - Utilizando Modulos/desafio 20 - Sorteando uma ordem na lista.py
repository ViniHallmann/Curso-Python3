#faça um programa que leia o nome dos 4 alunos e mostra em ordem o sorteio 
import random
print('SORTEIO DOS NOMES')
a= str(input('Digite o nome do primeiro aluno: '))
b= str(input('Digite o nome do segundo aluno: '))
c= str(input('Digite o nome do terceiro aluno: '))
d= str(input('Digite o nome do quarto aluno: '))

lista = [a,b,c,d]
random.shuffle(lista)

print('A ordem de apresentação será')
print(lista)
