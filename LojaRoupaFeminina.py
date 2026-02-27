print('============== Botique da NÕ ==============')
valor = float(input('\nQual o valor do produto? R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] Á vista dinheiro/Cheque
[ 2 ] Á vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou Mais no Cartão''')
opção = int(input('\nQual é a opção? '))
if opção == 1:
    opção = valor - (valor * 0.10)
    print('Opção 1! Pagamento Á vista no dinheiro/cheque é R$ {:.2f}!'.format(opção))
elif opção == 2:
    opção = valor - (valor * 0.05)
    print('Opção 2! Pagamento Á vista no cartão é R$ {}!'.format(opção))
elif opção == 3:
    opção = valor == valor
    parcela = valor / 2
    print('Sua compra de R$ {} Ficara em 2x de {} !Sem juros'.format(valor, parcela))
elif opção == 4:
    opção = valor + (valor * 20 / 100)
    total_parc = int(input('Quantas parcelas ?'))
    parcela = opção / total_parc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(total_parc,parcela))
    print('Sua compra de R${}, vai custar R${} no final'.format(valor, opção))
else:
    opção = 0
    print('\033[1:31mOPÇÂO INVALIDA! Tenta novamente')

