'''Escreva um programaque leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão
1 - para binario
2 para octal
3 para hexadecimal'''

numero = int(input('Digite um numero inteiro qualquer: '))
print(''' Escolha uma das opções: 
[1]- Converter para Binario 
[2]- Converter para Octal
[3]- Converter para Hexadecimal''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(numero, hex(numero)[2:]))
else:
    print('Digite uma das opções mostrada [1], [2] , [3]')