#leia uma frase e diga quantas vezes aparece a letra 'A'
#em que posição ela aparece por primeiro
#em que posição ela aparece por ultimo
frase = str(input('Digite uma frase:')).lower()
a = frase.count('a')
print(f'A letra A aparece na frase {a} vezes')
b = frase.find('a')+1
print(f'A primeira letra A aparece na posição {b}°')
c = frase.rfind('a')+1
print(f'A última letra A aparece na posição {c}')