#crie um programa que leia o nome compelto de uma pessoa e mostre:
#nome com todas as letras maiusculas
#o nome com todas minúsculas
#quantas letras ao todo(sem considerar espaços)
#quantas letras tem o primeiro nome
nome = str(input('Digite seu nome: ')).strip()

print('Seu nome em letra maiúscula é', nome.upper())
print('Seu nome em letra minúscula é', nome.lower())
total = len(nome) - nome.count(' ')
print(f'O seu nome tem ao todo {total} letras')
#print('O seu primeiro nome tem',nome.find(' '),'letras')
separa = nome.split()
print(separa)
print(f'Seu primeiro nome é {separa[0]} e ele possui {len(separa[0])} letras')