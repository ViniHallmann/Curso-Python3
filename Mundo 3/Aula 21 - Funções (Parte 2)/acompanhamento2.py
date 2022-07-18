#parametros opcionais
def somar(a = 0,b = 0,c = 0):
    s = a+b+c
    print(f'Soma vale {s}')


somar(3,2,5)
somar(8,4) #precisa colar c = 0, se nao da erro
somar()
somar(b = 4, c =2)

# escopos
def teste(b):
    global a # faz com que a receba 8 e nao crie uma variavel local A
    a = 8 #cria uma variavel local A com outro valor se nao tiver escrito global A
    b+=4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
#print(f'B fora vale {b}')# da erro por que B e uma variavel local da funcao teste
#print(f'C fora vale {c}')# o mesmo vale para C
