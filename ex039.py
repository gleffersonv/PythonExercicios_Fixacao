'''Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade:
se ele ainda vai se alistar ao servico militar
se e a hora de se alistar
se ja passou do tempo do alistamento.Seu programa tambem mostra o temqpo que falta ou que passou do prazo'''

from datetime import date
atual = date.today().year
ano=int(input('Digite ano de seu nascimento: '))
idade =  atual - ano
print('Você nasceu em {} e tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTO!')
elif idade > 18:
    print('Você ja deveria ter se alistado há {} ano.'.format(idade-18))
    print('Seu alistamento foi em {}'.format(atual -(idade-18)))
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento sera em {}'.format(atual + (18-idade)))



