#Aprimore o desafio anterior, mostrando no final:                         
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.
lista = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = 0
somaTC = 0
maior = 0
for l in range (0,3):
    for c in range (0,3):
        lista[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
        lista.append(lista[l][c])
        if lista[l][c] % 2 == 0:
            somaPar = somaPar + lista[l][c]
        if lista[1][c] > maior:
            maior = lista[1][c]
for l in range(0,3):
    somaTC += lista[l][2]

for l in range (0,3):
    for c in range (0,3):
        print(f'[{lista[l][c]}]', end='')
    print()

print(f'A soma dos valores pares e {somaPar}')
print(f'A soma dos valores da terceira coluna e {somaTC}')
print(f'O maior valor da segunda linha e {maior}')

