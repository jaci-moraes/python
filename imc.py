peso = input('Qual o seu peso? ') # aqui eu uso a string "qual o seu peso?" para a variável "peso"
altura = input('Qual sua altura? ') # aqui eu uso a string "qual sua altura?" para a variável "altura"
altura_convertida = float(altura) / 100  # aqui eu divido a minha altura em cm para metros "quebrados"
#usando o "float", de 190, ele passa a ser 1.9. Lembrando que o float serve para usar a função de número 
# quebrado enquanto a "int" serve para numeros inteiros 
resultado = int(peso) / (altura_convertida ** 2) # aqui eu uso o "int" pois a variável "peso" é num. inteiro,
# dividindo o peso pela altura convertida para float usando a divisão por 100, potencializada por 2 
print(f'Seu imc é: {resultado:.2f}') #aqui eu printo, uso o "f" para trazer as variáveis sem juntar com + entre as
# palavas/variáveis, abro a variável "resultado" em forma de {} pois é assim que trazemos os valores da fstring (f)
# uso o .2f para formatar o resultado para a qtd de casa decimal correta. (. para informar qtas casas eu quero
#2 quantidade de casas) 
                     