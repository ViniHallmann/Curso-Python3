#faca um programa que leia 5 valores numericos e guarde os em uma lista.
# no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.
lista = []
valor_menor = 0
valor_maior = 0
for a in range(0,5):
    lista.append(int(input(f'Digite um valor na posicao {a+1}: ')))
    if a == 0:
        valor_menor = valor_maior = lista[a]
    else:
        if lista[a] > valor_maior:
            valor_maior = lista[a]
        if lista[a] < valor_menor:
            valor_menor = lista[a]
print(lista)
print(f'Maior valor digitado foi {valor_maior} nas posicoes')
for c, v in enumerate(lista):
    if v == valor_maior:
        print(f'{c}. ', end = '')
print(f'\nMenor valor digitado foi {valor_menor} nas posicoes')
for c, v in enumerate(lista):
    if v == valor_menor:
        print(f'{c}. ', end = '')