#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
par = 0
num = (int(input("Digite um valor de 0 a 9: ")),
int(input("Digite um valor de 0 a 9: ")),
int(input("Digite um valor de 0 a 9: ")),
int(input("Digite um valor de 0 a 9: ")))
   

print(f'Total de numeros 9: {num.count(9)}')

if 3 in num:
    print(f'Valor 3 apareceu na posicao: {num.index(3)+1}')
else:
    print('Valor 3 nao foi digitado na tupla')

for a in num:
    if a%2==0:
        par+=1
print(f'Valores pares: {par}')