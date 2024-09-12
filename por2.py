salário = float(input('Qual o seu salário? R$' ))
resultado = salário + (salário * 15 / 100)
print(f'Com o seu novo reajuste, seu salário será de R${resultado:.2f}')