'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim',)

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))
print(lanche)

print('Comi muito')
pessoa = ('Jean', 38, 'M', 1.75, 68.9)
print(pessoa)'''
from unicodedata import numeric

'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso.
de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
      num = int(input('Digite um numero entre 0 e 20: '))
      if 0 <= num <= 20:
          break
      print('Tente Novamente. ', end='')
print(f'Voçê digitou o numero {cont[num]}')
