'''Faça um programa que leia uma frase pelo teclado e mostre:
-> Quantas vezes apareceu a letra "A".
-> Em que posição ela aparece a primeira vez.
-> EM que posição ela aparece a última vez.'''

frase=str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.find('A')+1))
print('Ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))