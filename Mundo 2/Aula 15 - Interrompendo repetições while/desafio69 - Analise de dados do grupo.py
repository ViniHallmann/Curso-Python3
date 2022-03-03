#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
a = 0
b = 0
c = 0
while True:
    print('='*19)
    print('CADASTRE UMA PESSOA')
    print('='*19)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
        print('Opção inválida. Tente Novamente!')
    continuar = str(input('DESEJA CONTINUAR [S/N]:')).strip().upper()[0]
    if idade > 18:
        a += 1
    if sexo.strip().upper()[0] == 'M':
        b += 1
    if sexo.strip().upper()[0] == 'F':
        if idade < 20:
            c += 1
    if continuar == 'N':
        break
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida. Tente Novamente!')
        continuar = str(input('DESEJA CONTINUAR [S/N]:')).strip().upper()[0]

print('='*43)
print(f'{a} Pessoas cadastradas com mais de 18 anos')
print(f'{b} Pessoas cadastradas como homens')
print(f'{c} Mulheres cadastradas com menos de 20 anos')
print('='*43)