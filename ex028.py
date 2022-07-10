'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador'''
from random import randint
from time import sleep
n1= randint(0,5)
print('-=-'*25)
print('Olá meu amigo,vamos brincar? Vou pensar em um numero e você temque acertar.')
print('-=-'*25)
numero=int(input('Digite um numero de 0 a 5: '))
print('Pensando...')
sleep(2)
if numero==n1:
    print('IHUUUUU,numero correto é {}, e você ACERTOU'.format(n1))
else:
    print('ERROUUUUU,numero correto é {}, e você digitou {}'.format(n1,numero))
print('FIM DO JOGO')