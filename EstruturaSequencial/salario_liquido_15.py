from decimal import getcontext, Decimal as dec
"""
salario_liquido_15.py
 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
 o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$ 4000,00
        - IR (11%) : R$ 440,00
        - INSS (8%) : R$ 320,00
        - Sindicato ( 5%) : R$ 200,00
        = Salário Liquido : R$ 3040,00

     input: float , int
     output: Decimal

A saída terá a  formatação da moeda BR R$ 0,00


>>> 20.0
>>> 201
4020,00
321,60
201,00
3055,00

"""
getcontext().prec = 4 # 34.00

hora = float(input("Quanto você ganha por hora?\n"))
print(f'hora {hora}')
horas_trabalhadas = int(input("Quantas horas trabalhadas no mês?\n"))

salario_bruto =  hora  * horas_trabalhadas

INSS = salario_bruto * 0.08
IR = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_liquido = dec(str(salario_bruto)) - (dec(str(INSS)) + dec(str(IR)) + dec(str(sindicato)))  #evita 1.555558884844688...

salario_bruto = f'{salario_bruto:.2f}'.replace('.', ',')
INSS = f'{INSS:.2f}'.replace('.', ',')
sindicato = f'{sindicato:.2f}'.replace('.', ',')
salario_liquido = f'{salario_liquido:.2f}'.replace('.', ',')

print(f"Salario bruto   : R$ {salario_bruto};")
print(f"INSS            : R$ {INSS};")
print(f"Sindicato       : R$ {sindicato};")
print(f"Salario liquido : R$ {salario_liquido};")
