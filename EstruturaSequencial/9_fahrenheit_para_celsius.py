"""
9_fahrenheit_para_celsius.py
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Fórmula da conversão do Celsius para Fahrenheit C = 5 * ((F-32) / 9).
O programan receberá um valor onde este será atribuído à variável fahrenheit
o retorno sera o valor correspondente em graus Celsius
input: float
# output: float °C
>>> 5
- 15 °C
>>> 32
0 ° C

"""

fahrenheit = float(input())

celcius = 5 * ((fahrenheit-32) / 9)


print("Temperatufa em Fahrenheit fornecida: {:0.1f}, resultado em °Celsius: {:0.1f} °C".format(fahrenheit, celcius))