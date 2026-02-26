cliente = str(input('Nome do cliente: ')).upper()
corte_cabelo = 40.00
corte_barba = 35.00
corte_maquina = 30.00
sombrancelha = 10.00

print('\nOla! é um prazer ter voçê em nossa barbearia: {}\nsegue abaixo a lista de preços!\nCorte de cabelo R$ {:.2f}\nBarba R$ {:.2f}\nCorte so maquina R$ {:.2f}\nSombrancelha R$ {:.2f}'.format(
        cliente, corte_cabelo, corte_barba, corte_maquina, sombrancelha))

combo1 = (corte_cabelo + corte_barba + sombrancelha) * 0.9)
combo2 = (corte_cabelo + corte_barba) * 0.9)
combo3 = (corte_cabelo + sombrancelha) * 0.9)
combo4 = (corte_barba + sombrancelha) * 0.9)

print('\nCombo 1 (Cabelo,Barba,Sombrancelha) ficaria um total: R$ {:.2f}'.format(combo1))
print('Combo 2 (Cabelo,Barba) ficaria um total: R$ {:.2f}'.format(combo2))
print('Combo 3 (Cabelo+sombrancelha) ficaria um total: R$ {:.2f}'.format(combo3))
print('Combo 4 (Barba,Sombrancelha) ficaria um total: R$ {:.2f}'.format(combo4))

print('''\nEscolha uma opção abaixo!
[ 9 ] Agendamento 
[ 10 ] Cancelamento''')

opção = int(input('Digite uma opção: '))

if opção == 9:
    print('''\nSegue abaixo as opções de serviços para escolher!
[ 1 ] - CORTE de CABELO R$ 40.00
[ 2 ] - BARBA R$ 35.00
[ 3 ] - CORTE SÓ MAQUINA
[ 4 ] - SOMBRANCELHA R$ 10.00
[ 5 ] - COMBO 1 (Cabelo,barba,sombrancelha) R$ 76.50
[ 6 ] - COMBO 2 (Cabelo,barba) R$ 67.50
[ 7 ] - COMBO 3 (Cabelo,Sombrancelha) R$ 45.00
[ 8 ] - COMBRO 4 (Barba,Sombrancelha) R$ 40.50''')


    serviços = int(input('Qual voce gostaria? '))

    if serviços == 1:
        print('Serviço de: Corte de cabelo! R${:.2f} '.format(corte_cabelo))
    elif serviços == 2:
        print('Serviço de: Barba R${:.2f}!'.format(corte_barba))
    elif serviços == 3:
        print('Serviço de: Corte Maquina R${:.2f}! '.format(corte_maquina))
    elif serviços == 4:
        print('Serviço de: Sombrancelha R${:.2f}'.format(sombrancelha))
    elif serviços == 5:
        print('Combo 1 - Cabelo,barba,sombrancelha: 10% Desconto R${:.2f}'.format(combo1))
    elif serviços == 6:
        print('Combo 2 - Cabelo,barba: 10% Desconto R${:.2f}'.format(combo2))
    elif serviços == 7:
        print('Combo 3 - Cabelo,sombrancelha: 10% Desconto R${:.2f}'.format(combo3))
    elif serviços == 8:
        print('Combo 4 - Barba,sombrancelha: 10% Desconto R${:.2f}'.format(combo4))

    print('Seu serviço foi agendado no nosso sistema, ate logo')

elif opção == 10:
    print( 'Nenhum dos nossos Serviços lhe interresou? Que pena, deixa para a próxima. Barbearia agradece por sua atenção!!')

else:
    print('OPÇÃO INVÁLIDA !')
