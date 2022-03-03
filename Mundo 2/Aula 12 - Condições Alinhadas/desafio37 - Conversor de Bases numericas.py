#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para CONVERSÃO
[1] Converter para binário
[2] Converter para OCTAL
[3] Converter para hexadecimal''')
opção = int(input('Digite a base de CONVERSÃO escolhida: '))
if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente')
