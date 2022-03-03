#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, 
# calcule e mostre o comprimento da hipotenusa
import math

print('CALCULADORA DE HIPOTENUSA')
co = float (input('Qual o comprimento do Cateto Oposto? '))
ca = float (input('Qual o comprimento do cateto adjacente? '))
h = float (math.sqrt(co**2 + ca**2))
print(f'O comprimento da hipotenusa é: {h}')

#Diferentes maneiras de fazer o programa

co = float (input('Digite o cateto oposto: '))
ca = float (input('Digite o cateto adjacente: '))
h = math.hypot(co, ca)
print(f'O valor da sua hipotenusa é:{h}')


