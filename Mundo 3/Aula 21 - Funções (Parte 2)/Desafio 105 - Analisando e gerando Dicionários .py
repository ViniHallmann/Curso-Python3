#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
# e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                  
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)
def Notas(*valores, sit = False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param valores: recebe uma ou varias notas dos alunos
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao.
    :return: dicionario com informacoes dos alunos e da turma.
    """
    a = dict()
    a['total'] = len(valores)
    a['maior'] = max(valores)
    a['menor'] = min(valores)
    a['media'] = sum(valores)/len(valores)
    
    if sit == True:
        if a['media']>=9 and a['media'] <=10:
            a['situacao'] ='Otima!'
        if a['media']>=6 and a['media'] <=8:
            a['situacao'] = 'Boa!'
        if a['media']>=3 and a['media'] <6:
            a['situacao'] ='Ruim'
        if a['media'] < 3 and a['media'] <=0:
            a['situacao'] ='Pessima...'
        
    return a

resposta = Notas(9,10,2,1,3, sit = True)
print(resposta)

