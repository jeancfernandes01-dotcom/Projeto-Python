salario = float(input('Qual o seu salario mensal: R$ '))
ano = 12
print('''Quanto porcentos do seu salario voçê consegue guardar por mês?
[1] - 10%
[2] - 15%
[3] - 20%
''')
opção = int(input('Qual opção desejada?'))
if opção == 1:
    reserva = salario - (salario * 0.90)
    ano = reserva * 12
    print('Voçê guardando a quantia de R${}, correspondendo a 10% do seu salario'.format(reserva))
    print('Sua reserva finançeira de 1 ano será de R${} '.format(ano))
elif opção == 2:
    reserva = salario - (salario * 0.85)
    ano = reserva * 12
    print('Voçê guardando a quantia de R${}, correspondendo a 15% do seu salario'.format(reserva))
    print('Sua reserva finançeira de 1 ano será de R${} '.format(ano))
elif opção == 3:
    reserva = salario - (salario * 0.80)
    ano = reserva * 12
    print('Voçê guardando a quantia de R${}, correspodendo a 20% do seu salario'.format(reserva))
    print('Sua reserva finançeira de 1 ano será de R${} '.format(ano))
else:
    print('\033[1:31mOPÇÂO INVÁLIDA!!! Tente novamente.')

