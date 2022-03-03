from math import sqrt,floor,ceil
num = int(input ('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz}')
print(f'A raiz de {num} arredondada para cima é {ceil(raiz)}')
print(f'A raiz de um {num} arredondado para baixo é {floor (raiz)}')
