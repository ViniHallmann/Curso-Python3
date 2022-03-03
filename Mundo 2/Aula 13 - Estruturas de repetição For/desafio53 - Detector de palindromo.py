#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: '))
frase1 = frase.strip().upper().replace(' ','' )
frase2 = frase[::-1].strip().upper().replace(' ','' )
print(f'O inverso da frase {frase1} é {frase2}')
if frase1 == frase2:
    print('Essa frase é um Palíndromo')
else:
    print('Essa frase não é um Palíndromo')
