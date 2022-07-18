# estrutura try e except
#try:
    # faz a operacao
#except:
    # se falhou a operacao
#else: 
    # se a operacao deu certo
#finally:
    # acontece independente se der erro ou certo a operacao

try: 
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por zero!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: 
    print(f'O resultado da divisao e {r}')
finally:
    print('Volte sempre! Muito obrigado!')