"""
loja_de_tintas_17.py
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

input: float
output: int, Decimal, float,

>>> 23.6
(2, 160,00, 23.99)
(7, 175,00, 23.99)

"""
from decimal import getcontext, Decimal as dec, ROUND_UP
LATAS = 18 
GALOES = 3.6
PRECO_LATA = 80.0
PRECO_GALOES = 25.0
PRECO_LATAS_GALOES = (PRECO_LATA % PRECO_GALOES) / (LATAS + GALOES)


metro_quadrado = float(input("Forneca quantos metros quadrados a serem pintados aproximadamente\n"))
metro_quadrado += (metro_quadrado * 0.1) / 6 #acrescentado 10%  
if metro_quadrado % LATAS == 17:
    latas_m_lata = (metro_quadrado + 1 ) % LATAS 
else:
    latas_m_lata = metro_quadrado  % LATAS 
latas_lata = (metro_quadrado - latas_m_lata) / LATAS
latas_lata = dec(latas_lata).quantize(dec('1.'), rounding=ROUND_UP)
preco_misturados = dec(str(latas_lata)) * dec(str(PRECO_LATA))

latas_m_galoes = latas_m_lata / GALOES
latas_m_galoes = dec(latas_m_galoes).quantize(dec('1.'), rounding=ROUND_UP)
preco_misturados += dec(str(latas_m_galoes)) * dec(str(PRECO_GALOES))

preco_misturados = f'{preco_misturados:.2f}'.replace('.',',')

apenas_latas = metro_quadrado  / LATAS
apenas_latas = dec(apenas_latas).quantize(dec('1.'), rounding=ROUND_UP)
preco_ap_latas = apenas_latas * dec(PRECO_LATA)
preco_ap_latas =f'{preco_ap_latas:.2f}'.replace('.',',') # 0,00 evita saída como notação 8E+1

apenas_galoes  = metro_quadrado  / GALOES
apenas_galoes = dec(apenas_galoes).quantize(dec('1.'), rounding=ROUND_UP)
preco_ap_galoes = apenas_galoes * dec(PRECO_GALOES)

preco_ap_galoes = f'{preco_ap_galoes:.2f}'.replace('.',',')
print(preco_ap_galoes)
print(f"Latas 18L   Quantidade: {apenas_latas}  Preço total R$: {preco_ap_latas} para {metro_quadrado:1.2f} m²")
print(f"Galões 3,6L Quantidade: {apenas_galoes} Preço total R$: {preco_ap_galoes} para {metro_quadrado:1.2f} m²")
print(f"Galões 3,6L Quantidade: {latas_m_galoes} Latas 18L Quantidade: {latas_lata} Preço total R$: {preco_misturados} para {metro_quadrado:1.2f} m²")
