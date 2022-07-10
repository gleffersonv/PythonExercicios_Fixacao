salario=float(input('Qual é salario do Funcionario? R$'))
aumento=salario+(salario*15/100)
print('Um funcionario que recebia R${:.2f} de salario, com 15% de aumento passa a receber {:.2f}'.format(salario,aumento))