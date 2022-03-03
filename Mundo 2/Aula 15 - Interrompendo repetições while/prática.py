n =  s = 0
#while n != 999:
    #n = int(input('Digite um número: '))
    #s += n
#print(f'A soma vale {s-999}') ISSO AQUI É GAMBIARRA, JEITO ERRADO DE SE FAZER


#JEITO CERTO COM A FUNÇÃO BREAK
while True:
    n = (int(input('Digite um valor: ')))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')