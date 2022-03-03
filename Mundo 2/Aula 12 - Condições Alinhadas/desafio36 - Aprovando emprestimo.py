#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('EMPRÉSTIMO BANCÁRIO')
casa = float (input('Digite o valor total da casa: R$ '))
salario = float (input('Digite o valor total do seu salário: R$'))
tempo = int (input('Quantos anos de financiamento? '))
prestação = casa / (tempo * 12)
minimo = salario * 30/100
print(minimo)
print(f'Para pagar uma casa de R${casa} em {tempo} anos, a prestação será de {prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')
