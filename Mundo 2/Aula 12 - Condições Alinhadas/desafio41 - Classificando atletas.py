#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#  e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Sua categoria na natação é: MIRIM')
elif idade <= 14 and idade > 9:
    print('Sua categoria na natação é: INFANTIL')
elif idade <= 19 and idade > 14:
    print('Sa categoria na natação é: JÚNIOR')
elif idade <= 25 and idade > 19:
    print('Sua categoria na natação é: SÊNIOR')
else:
    print('Sua categoria na natação é: MASTER')

