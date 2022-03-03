#Dsenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

print('Olá, digite suas notas a baixo e eu calcularei a sua média.', end = '\n\n')

a=  float(input('Nota de matemática: '))
b=  float(input('Nota de Português: '))
c= (a+b)/2

print('\nCalculando........', end = '\n\n')
print('A sua média é')
print(f'{c:.^11}')