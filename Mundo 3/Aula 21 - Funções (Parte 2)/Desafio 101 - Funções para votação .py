#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade >= 18 and idade < 65:
        voto = 'VOTO OBRIGATORIO'
    elif idade == 16 or idade == 17 or idade >=65:
        voto = 'VOTO OPCIONAL'
    elif idade <= 15:
        voto = 'NAO VOTA'
    
    print(f'Com {idade} anos: {voto}')
#programa
nascimento = int(input("Em que ano voce nasceu? "))
voto(nascimento)
