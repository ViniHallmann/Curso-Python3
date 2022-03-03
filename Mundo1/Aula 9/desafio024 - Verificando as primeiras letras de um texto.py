#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
nome = str(input('Digite o nome de uma cidade: '))
cidade = nome.title().strip()
print(cidade)
print(cidade[:5] == 'Santo')
