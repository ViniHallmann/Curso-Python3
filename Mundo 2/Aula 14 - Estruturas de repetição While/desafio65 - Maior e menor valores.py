#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
contagem = soma = maior = menor = 0
continuação = 'S'
while continuação in 'S':
    num = int(input('Digite um número inteiro: '))
    contagem += 1
    soma += num
    continuação = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if contagem == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

if contagem == 1:
    print(f'O único número digitado foi {contagem}, tente novamente para conseguir mais informações sobre os valores (Maior e Menor)')
    print(f'A Média do valor digitado é igual a {contagem}')
média = soma / contagem
if contagem > 1:
    print(f'Você digitou {contagem} números e a média dos valores digitado foi de {média:.2f}')
    print(f'O maior número digitado foi {maior} e o menor foi {menor}')


