#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0 
contagem = 0 
for a in range(1,7):
    n = int(input(f'Digite o {a} valor:'))
    if n % 2 == 0:
        soma += n
        contagem += 1
print(f'A soma dos {contagem} números pares, desconsiderando os ímpares, escolhidos é de {soma}!')