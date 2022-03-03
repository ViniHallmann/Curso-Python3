#crie um programa que leia um número real qualquer pelo teclado e mostra a sua porção inteira


from math import trunc
n = float (input ('Me diga um número qualquer: '))
print(f'A porção inteira desse número é: {trunc (n)}')

#Duas maneira diferentes de escrever o código
n = float (input('me diga um valor: '))
print(f'seu número numa porção inteira é {int(n)}')