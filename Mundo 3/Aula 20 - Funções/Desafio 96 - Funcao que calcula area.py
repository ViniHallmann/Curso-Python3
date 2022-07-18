#Faça um programa que tenha uma função chamada área(), que receba as dimensões 
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l,c):
    area = 0
    area = l*c
    print(f'A area de um terreno de {l} x {c} e de {area} metros quadrados')


print("Controle de Terrenos")
print("-"*20)
l =float(input("Largura (m): "))
c= float(input("Comprimento (m): "))
area(l,c)
