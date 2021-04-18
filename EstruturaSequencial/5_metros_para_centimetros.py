"""
5_metros_para_centimetros.py
Faça um Programa que converta metros para centímetros.
O programa recebera a entrada do usuário e retornará o equivalente ao digitado em centímetro 
python version: 3.9.2
1 m = 100 cm
input: float
output: float

>>> 1.0
100.0
>>> 3.5
350.0
>>> 450.5
4505.0
"""

metro = float(input()) 
print("O valor {:0.2f} em metros equivale a {:0.2f} em centímetros!".format(metro, metro * 100))