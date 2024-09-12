# O programa deve receber 4 notas correspondentes aos 4 bimestres do ano letivo e deve retornar 
# a média do aluno. Extra: primeiro "if"

primeirob = float(input('Informe a nota do primeiro bimestre: '))
segundob = float(input('Informe a nota do segundo bimestre: '))
terceirob = float(input('Informe a nota do terceiro bimestre: '))
quartob = float(input('Informe a nota do quarto bimestre: '))
resultado = (primeirob + segundob + terceirob + quartob) / 4 

if resultado >= 7.0:
  print(f'Parabéns, você passou! Sua média é {resultado:.2f}')
elif resultado >= 6.0:
  print(f'Você ficou de recuperação! Sua média é {resultado:.2f}')
else:
  print(f'Se fudeu! Sua média é {resultado:.2f}')