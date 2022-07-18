#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
# pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
from typing import Counter




dados = dict()
pessoas = list()
totPessoas = 0
totIdade = 0
while True:
    dados.clear
    dados['nome'] = str(input("Nome: "))
    while True: 
        dados['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()
        if dados['sexo'] in 'MF':
            break
        print("ERRO! Responda apenas com M ou F")
    dados['idade'] = int(input("Idade: "))
    totIdade += dados['idade']
    totPessoas += 1
    pessoas.append(dados.copy())
    while True: 
        continuar = str(input("Quer continuar [S/N]? ")).upper()
        if continuar in 'SN':
            break
        if continuar not in 'SN':
            print("Erro! Responda apenas S ou N.")
    if continuar == 'N':
        break


media = totIdade/totPessoas
print(f'Ao todo temos {totPessoas} cadastradas')
print(f'A media de idade e de {media:.2f}')

print("As mulheres cadastradas foram", end='')
for p in pessoas:
    if p['sexo'] in'F':
        print(f' {p["nome"].capitalize()}', end='')

print("\nLista das pessoas que estao acima da media: ")
for p in pessoas:
    if p['idade'] >= media:
        print(f'nome: {p["nome"]}; sexo:{p["sexo"]}; idade:{p["idade"]}')
