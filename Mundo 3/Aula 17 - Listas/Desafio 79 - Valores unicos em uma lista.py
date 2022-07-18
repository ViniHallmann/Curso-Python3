#crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

continuar ='S'
lista = []
while continuar !='N':
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso!")
    else: print("Valor duplicado, nao vou adicionar a lista")
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    lista.sort()
print(lista)
