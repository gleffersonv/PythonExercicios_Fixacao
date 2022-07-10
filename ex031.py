'''Desenvolva um programa que pergunta a distancia de uma viagem em km
calcule o preco da passagem,cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas'''


distancia=float(input( "Até 200km/h = R$0,50 por km rodado \nAcima de 200km/h = R$0,45 km rodado"
                     " \nQual a distância que você quer percorrer?"))
if distancia <= 200:
    print('O valor de sua pasagem é R${:.2f}'.format(distancia*0.50))
else:
    print('O valor de sua passagem é R${:.2f}'.format(distancia*0.45))
