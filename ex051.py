'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Digite o PRIMEIRO termo: '))
razao = int(input('Digite a RAZÃO: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao , razao):
    print('{}'.format(i), end=' -> ')
print('ACABOU')