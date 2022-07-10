a=float(input('Qual a altura da sua parede?'))
l=float(input('Qual a largura da sua parede?'))
area= a*l
tinta=area/2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².Para pintar essa parede,você precisará de {:.2F}L de tinta.'.format(a,l,area,tinta))
