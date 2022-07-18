#interactive help
#help()
#help(print)

def contador(i,f,p):
    #docstring
    """
    -> faz uma contagem e mostra na tela.
    - Parametro i: inicio da contagem
    - Parametro f: fim da contagem
    - Parametro p: passo da contagem
    - return: sem retorno
    """
    c = i
    print(f'O contador vai comecar no {i}, vai ate o {f} de {p} em {p}')
    while c<=f:
        print(f'{c}', end =' ')
        c+=p
    print('FIM!')
contador(2,10,2)

help(contador)