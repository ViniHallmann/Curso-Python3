#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
print('='*14) 
print('LOJAS \033[0;34mHALLMANN \033[m')
print('='*14)
preço = float(input('Qual o valor total das compras? R$:'))
print('''Formas de pagamento:
[0] À vista no dinheiro/cheque
[1] À vista no Cartão
[2] Em até 2x no cartão
[3] 3x ou mais no cartão''')
pagamento = int(input('Qual a forma de pagamento? '))

if pagamento == 0:
    desconto = preço * 10/100
    final = preço - desconto
    print(f'Pagando à vista no Dinheiro/Cheque o desconto será de {desconto} reais, o preço do produto final será de R${final}')
elif pagamento == 1:
    desconto = preço * 5/100
    final =  preço - desconto
    print(f'Pagando à vista no cartão o desconto será de {desconto} reais, o preço do produto final será de R${final}')
elif pagamento == 2:
    print(f'Pagando em até 2x no cartão não há desconto a ser aplicado, o preço do produto final é de R${preço}')
elif pagamento == 3:
    juros = preço * 20/100
    print(f'Pagando em 3x ou mais no cartão, há um juros 20% porcento aplicado no valor de {juros} reais. Valor do produto final é de R${preço + juros}')
else: 
    erro = 'Opção de pagamento inválida. Tente novamente'
    print('\033[0;31m ', erro.upper())