frase = 'Curso em Vídeo Python'
#Fatiamento = fatiar string(Frase)
print(frase)
print(frase[9])
#print frase[9] significa que apenas a letra 9 irá aparecer
print(frase[9:13])
#print(fase[9:13]) significa que irá da letra 9 até a letra 12,o 13 fica de fora(Víde)
print(frase[9:14])
#mesma coisa do de cima mas nesse exmeplo a frase será da letra 9 até a 13(Vídeo)
print(frase[9:21])
print(frase[9:21:2])
#esse :2 significa que irá pular uma letra, ou seja: Escolhe a letra 9(V) pula o (í) escolhe o (D) pula o (E) assim por diante...
print(frase[:5])
#se não tem nada antes dos dois pontos(:) o print irá começar da primeira letra da string(C)7
#[:x]  indica o final
print(frase[15:])
#se não tem nada depos dos dois pontos(:) o print irá até o final da frase, começando onde foi determinado dentro dos conchetes
#[x:] indica o inicio
print(frase[9::3])
#esse exemplo mostra o inicio, não mostra o final ali no meio dos dois pontos e mostra que pula 3 casas e escolhe a proxima casa dps de pular as tres letras
#(A primeira sempre aparece, ou seja, a letra 9)

#len = qual o comprimento da frase?
print(len(frase))

#count = conta algo
print(frase.count('o'))
print(frase.count('o',0,13))
#0 e 13 representam o inicio e o final de até onde irá contar o número de letra (O)

#find = me mostra algo que quero encontrar
print(frase.find('deo'))
#o find vai mostrar onde começa o que quero encontrar, no caso DEO, e a letra D começa na posição 11

#in = me diz se tal palavra existe na programação me dizendo TRUE ou FALSE
print('Curso' in frase)

#replace = trocar palavra dentro da minha frase
print(frase.replace('Python','Android'))

#Upper e Lower(Transforma em maiusculo e minusculo)
#sempre colocar 2 parenteses dps do upper e lower
print(frase.upper())
print(frase.lower())

#capitalize = transforma todas letras em minusculo e deixa apenas a primeira letra em maiusculo 
print(frase.capitalize())

#tittle = analise quantas palavras tem a frase e depois transforma o inicio de cada palavra em maiusculo
print(frase.title())

frase2 = '   Aprenda Python   '
#strip = remover espaços inuteis no inicio e no final da frase
print(frase2)
print(frase2.strip())
#rstrip = só remove os espaços do lado direito da frase(R = RIGHT)
print(frase2.rstrip())
print(frase2.lstrip())
#L = Left remove os espaços do lado esquerdo da frase

#split = divisão dentro da frase entre os espaços de cada palavra
print(frase.split())

#join = junção de palavras
print(''.join(frase))
print('.'.join(frase))
print('-'.join(frase))
