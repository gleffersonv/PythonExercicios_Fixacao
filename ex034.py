'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
para salarios superior a R$1.200,calcule aumento 10%
para os inferiores ou iguais o aumento e de 15%'''

salario=float(input('Qual é salário do funcionario? R$'))
if salario <= 1.250:
    novo= salario + (salário * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,novo))