#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado 
# ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    """
    -> Calcula o fatorial de um numero.
    :param num: O numero a ser calculado.
    :param show: (Opcional) Mostra ou nao a conta do fatorial.
    :return: O valor do fatorial de um numero num.
    """
    fatorial = 1
    for a in range(num, 0 , -1):
        fatorial *=a
    if show == True:
        for a in range(num, 0, -1):
            if a>1:
                print(f'{a} x ', end = '')
            else: print(f'{a} = ', end = '')
    return fatorial

print(fatorial(5, show = True))
