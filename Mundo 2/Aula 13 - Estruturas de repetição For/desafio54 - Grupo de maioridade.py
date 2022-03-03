#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
contmenor = 0
contmaior = 0

for a in range(1,8):
    ano = int(input(f'Digite em que ano a {a}° pessoa nasceu: '))
    idade = atual - ano
    if  idade >= 18:
        contmaior += 1
    else:
        contmenor += 1

print(f'Ao todo, {contmenor} pessoas são menor de idade', end = ' ')   
print(f'E {contmaior} são maior de idade')

