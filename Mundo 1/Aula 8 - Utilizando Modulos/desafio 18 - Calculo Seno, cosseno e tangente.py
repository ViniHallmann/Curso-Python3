#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
a =  float (input('Digite o valor do ângulo:'))


print(f'O valor do seno é: {math.sin(math.radians(a)):.2f}')
print(f'O valor do cosseno é: {math.cos(math.radians(a)):.2f}')
print(f'O valor da tangente é: {math.tan(math.radians(a)):.2f}')