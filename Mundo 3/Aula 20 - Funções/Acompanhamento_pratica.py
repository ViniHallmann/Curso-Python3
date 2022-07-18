#a = 4   
#b = 5
#s = a+b
#print(s)  

#a = 4
#b = 3
#s = a+b
#print(s)

def soma(a,b):
    print(f'A = {a} e B ={b}')
    s = a+b
    print(f'Soma A + B = {s}')

soma(4,5) # Passando parâmetros
soma(4,3)
soma(8,9)

#def contador(*num):
    #print(num)
    #for v in num:
        #print(v)
def contador(*num):
    tamanho = len(num)
    print(f'{num} tem {tamanho} numeros')

contador(2,1,7)
contador(2,1,7,8,4,2)
contador(2,1,7,3,4,7,6,5,4,1)


def dobraValores(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos +=1


valores = [0,1,2,3,4,5]
dobraValores(valores)
print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s +=num
    print(f'Somando os valores {valores} temos {s}')
soma(5,2)
soma(2,9,4)




