'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h,mostra uma mensagem dizendo que ele foi multado
A multa vai custar R$7.00 por cada km acima do limite'''

limite=80
multa=7
velocidade=float(input('Por favor,digite sua velocidade km/h: '))
acima = velocidade - limite
if velocidade > limite:
    print('Você foi multado, e sera cobrado R$7,00 por cada km/h ultrapassado.')
    print('Valor total de sua multa é {}, referente a {} km/h ultrapassado.'.format(acima*7, acima))
else:
    print('Excelente continue mantendo o limite permitido de {} km/h'.format(limite))
