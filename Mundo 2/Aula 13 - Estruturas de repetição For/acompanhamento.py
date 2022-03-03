#for a in range(1,2):
    #print('Acabou')
#O comando acima só vai dar um print escrito 'acabou' pois o python desconsidera a ultima casa sempre, ou seja, se eu escrever
# for a in range (1,5) ele irá printar no 1, no 2, no 3 e no 4 *APENAS 4 PRINTS EM VEZ DE 5*
#for b in range(1,5):
    #print('TESTE')

#Se eu quiser 5 prints em vez de 4, como no exemplo acima. Tenho q escrever o código da seguinte forma.
#Primeiro exemplo:
#for c in range(0,5):
    #print('a')
#Segundo exemplo:
#for d in range(1,6):
    #print('A')

#for a in range(1,5):  #Contagem para frente
    #print(a)
#print('Contagem até 4 finalizada')

#for b in range(4,0,-1): #Contagem para trás(precisa colocar o -1 no final)
    #print(b)

for c in range(0,10, 2): #Contagem pulando as casas(colocar quantas casa a contagem deve pular no final)
    print(c)