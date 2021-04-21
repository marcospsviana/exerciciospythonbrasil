"""
base_com_expoentes_11.py
 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

     a. o produto do dobro do primeiro com metade do segundo .
     b. a soma do triplo do primeiro com o terceiro.
     c. o terceiro elevado ao cubo.

     input: int , int, float
     output: float
>>> 8
>>> 5
>>> 6
Item a: 40.0
Item b: 126.0
Item c: 216.0
>>> 9
>>> 5
>>> 7
Item a: 45.0
Item b: 142.0
Item c: 343.0

"""

a = int(input())
b = int(input())
c = float(input())
a = 2 * a * (b / 2)
b = (3 * a) + c
c = c ** 3
print(f"Item a: {a}")
print(f"Item b: {b}")
print(f"Item c: {c}")