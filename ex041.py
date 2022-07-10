'''A confederação nacional de  natação precisa de um  programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo
com a idade:
ate 9 anos:mirim
ate 14 anos:infanil
ate 19 anos : junior
ate 20 anos senior
acima : master'''

from datetime import date
atual= date.today().year
nasc=int(input('Digite o ano de NASCIMENTO: '))
idade= atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade == 20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')

