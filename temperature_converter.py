unidade = input('Digite "C" para Celsius e "F" para Fahrenheit: ') 

if unidade == 'F' or unidade == 'f':     
    fahrenheit = float(input('Insira a temperatura em Celsius: '))
    resultado = (fahrenheit * 1.8) + 32
    print(f'Está fazendo {resultado:.2f}°F.' )
elif unidade == 'C' or unidade == 'c': 
    celsius = float(input('Insira a temperatura em Fahrenheit: '))
    resultado = (celsius - 32) / 1.8
    print(f'Está fazendo {resultado:.2f}°C.')
else:
    print('Você deve digitar "C" ou "F".')






