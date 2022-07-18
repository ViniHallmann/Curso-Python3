def aumentar(preco, formato = False):
    res = preco*0.10+preco
    return res if formato is False else moeda(res)
def dobro(preco, formato = False):
    res = preco*2
    return res if formato is False else moeda(res)
def metade(preco, formato = False):
    res =  preco/2
    return res if formato is False else moeda(res)
def moeda(preco = 0, moeda = 'R$', formato = False):
    res = f'{moeda}{preco}'.replace('.',',')
    return res if formato is False else moeda(res)