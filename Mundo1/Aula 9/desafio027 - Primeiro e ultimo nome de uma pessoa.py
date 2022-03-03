#programa que leia o nome completo da pessoa, mostrando e seguida o primeiro e o ultimo nome separadamente
n = str(input('Digite seu nome compelto: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
