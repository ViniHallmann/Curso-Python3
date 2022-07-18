def aumentar(preco):
    return preco*0.10+preco
def dobro(preco):
    return preco*2
def metade(preco):
    return preco/2
def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.',',')