#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
#verificação do menor número
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificação do maior número
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor} e o maior valor digitado foi {maior}')

