#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
media = 0
velho = 0
nomevelho = 0
contmulher = 0
for p in range (1,5):
    print(f'--- {p}ª Pessoa ---')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:'))
    soma += idade
    if p == 1 and sexo.upper() == 'M':
        velho = idade
        nomevelho = nome
    if sexo.upper() == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo.upper() == 'F' and idade < 20:
        contmulher += 1

media = soma /4 
print(f'A média de idade do grupo é de {media}.')
print(f'O homem mais velho tem {velho} anos e seu nome é {nomevelho}.')
print(f'Ao todo são {contmulher} mulheres no grupo com menos de 20 anos.')
