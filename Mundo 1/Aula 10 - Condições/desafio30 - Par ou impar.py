#crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
num = int(input('Digite um número inteiro: '))
verificação = (num%2)
if verificação == 0:
    print('O número escolhido é par')
else: 
    print('O número escolhido é impar')

