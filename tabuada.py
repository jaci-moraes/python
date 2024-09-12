valor = int(input('Digite o número para a tabuada:'))
print('-' * 10)
for numero in range(10): # Aqui eu faço uma iteração de 10 numeros começando com 0 e excluindo o último (0 a 9)
  indice = numero + 1 # Aqui eu somo 1 para que o indice da iteração vá de 1 a 10 
  resultado = valor * indice# Aqui eu armazeno o produto (multiplicação) do valor recebido no input * o indice
  print(f'{valor} X {indice} = {resultado}')
print('-' * 10)