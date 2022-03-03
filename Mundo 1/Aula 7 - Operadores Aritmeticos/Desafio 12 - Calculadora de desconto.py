#Faça um algoritimo que leia o preço de um produto 
#e mostre seu novo preço, com 5% de desconto

valor_original = float (input ('Preço do produto sem o desconto:R$ '))
desconto= (valor_original*0.05)
valor_final = valor_original - desconto
print(f'Novo preço do produto com o desconto de 5% aplicado:R$ {valor_final:.3}')