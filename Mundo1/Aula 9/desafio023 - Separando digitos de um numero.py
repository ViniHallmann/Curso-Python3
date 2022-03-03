#crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#mostre unidade,dezena,centena e milhar

numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'O número informado foi {numero}')
print(f'Unidade do número = {u}')
print(f'Dezena do número = {d}')
print(f'Centena do número = {c}')
print(f'Milhar do número = {m}')
