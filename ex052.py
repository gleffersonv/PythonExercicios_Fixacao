'''52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

numero=int(input('Digite um numero inteiro: '))
tot = 0
for i in range (1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print(' \n\033[mO número {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('É por isso ele É PRIMO!')
else:
    print('É por isso ele NÃO É PRIMO!')
