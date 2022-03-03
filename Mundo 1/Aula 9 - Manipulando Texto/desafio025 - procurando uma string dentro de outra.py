#crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
a = str(input('Digite seu nome: ')).strip()
b = 'silva'in a.lower()
print(f'Seu nome tem Silva? {b}')
