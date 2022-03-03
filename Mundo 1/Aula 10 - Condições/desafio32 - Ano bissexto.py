#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Digite o ano que você quer analisar (Digite 0 caso queira analisar o ano atual): '))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano analisado ({ano}) É BISSEXTO')
else:
    print(f'O ano analisado ({ano}) NÃO É BISSEXTO')