#n = int(input('Digite um número: '))
#for c in range(1, n+1): #Como o python desconsidera a ultima casa, se colocar o +1 ele irá contar a ultima casa junto!!!!
    #print(c)

#i = int(input('Início da contagem: '))
#f = int(input('Fim da contagem: '))
#p = int(input('Passo?'))
##for a in range(i,f+1,p):
    #print(a)
s = 0
for b in range(0,3):
    n = int(input('Digite um valor:'))
    s = n + s
print(f'A soma dos valores é {s}')