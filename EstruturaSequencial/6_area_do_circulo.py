"""
6_area_do_circulo.py
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
O programa recebera a entrada do usuário, esta entrada será atribuida a variavel de nome raio
e retornará o equivalente a área de um círculo
python version: 3.9.2

Cálculo da área de um circulo é proporcional ao produto de seu raio ao quadrado com pi:
Fórmula:
A = π . r2
A saida será dada com adicional de 3 casas decimais em representação de ponto flutante. Exemplo 700.538
constante: PI 3.141592
input: float
output float 
>>> 15.6
764.538 cm²
>>> 12.3 
475.291 cm²
>>> 23.564
1744.407 cm²
"""

PI = 3.141592

raio = float(input())
area_circulo = (raio * raio) * PI

print("A área do cículo de raio: {:0.3f}, é aproximadamente: {:0.3f} cm²".format(raio, area_circulo))