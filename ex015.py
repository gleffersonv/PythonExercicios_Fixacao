km=float(input('Qual a quantidade de Km percorrido? '))
d=int(input('Para quantos dias foi alugado? '))
total= (d*60) + (km*0.15)
print('Total a pagar pelo aluguel é de R${:.2F}'.format(total))
