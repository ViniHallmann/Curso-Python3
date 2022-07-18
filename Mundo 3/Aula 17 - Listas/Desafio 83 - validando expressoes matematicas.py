#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está 
# com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressao: '))
lista = []
for a in expressao:
    if a == '(':
        lista.append('(') # coloca um parenteses na lista
    elif a == ')':
        if len(lista) > 0: #se a lista tiver um parenteses
            lista.pop() # remove aquele parenteses. 'fecha o parenteses' no caso
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressao valida!')
else:
    print('Expressao invalida...')
