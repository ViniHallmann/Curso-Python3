#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavra = ('Mercado', 'Curso', 'Notebook')
for a in palavra:
    print(f'\nNa palavra {a} temos ',end ='')
    for v in a:
        if v.lower() in 'aeiou':
            print(v, end=' ')