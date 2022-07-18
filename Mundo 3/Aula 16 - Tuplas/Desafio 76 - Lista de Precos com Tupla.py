#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tabela = ('Lapis', 1.75, 
'Borracha', 2, 
'Caderno', 15.90,
'Estojo', 25,
'Transferidor', 4.50,
'Compasso', 2.99,
'Mochila', 120.99,
'Canetas', 1.99,
'Livro',34.90)
print('-'*26)
print('    LISTAGEM DE PRECOS')
print('-'*26)
for a in range(0,len(tabela)):
    if a%2 ==0:
        print (f'{tabela[a]:.<20}', end = '')
    else:
        print(f'R${tabela[a]:>6.2f}')
print('-'*26)