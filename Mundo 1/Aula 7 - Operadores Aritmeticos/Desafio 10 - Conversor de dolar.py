#crie um programa que leia quanto de dinheiro uma pessoa tem na carteira 
#e mostre quantos dólares ela pode comprar
print('=====Corretora Hallmann=====')
a = float (input('Quanto você está disposto a gastar para comprar em Dólar? R$:'))
print('\nCotação do dólar do dia (18/05/2020): 1 Dólar Americano : 5.30 Real brasileiro \n')
b = (a/5.30)

print('Com o seu orçamento é possivel comprar U$', round(b,2),'dólares')