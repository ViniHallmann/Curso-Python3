#Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# 
# Importante: use cores.

def ajuda(com):
    help(com)
    
def titulo(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))

comando = ''
while True:
    titulo('SYSTEMA DE AJUDA PyHELP')
    comando = str(input("Funcao ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!')