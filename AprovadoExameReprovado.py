assiduidade = float(input('Digite a porcentagem de assiduidade: '))
nota = float(input('Digite a nota (0 a 20:'))
situação = ""

if assiduidade < 75:
    situação = 'Reprovado por faltas'

else:

 if nota < 5:
     situação = 'Reprovado por nota'

 if nota >= 5 and nota < 9.5:
     situação = 'Exame'

 if nota >= 9.5:
     situação = 'Aprovado'

 print('O aluno teve {}% de presença e nota {}. situação: {}'.format(assiduidade,nota,situação))

