
# Entradas 
from re import A
from tkinter import X


a=int(input("Digite el precio del lote de naranjas "))
b=float(input("Digite el precio por decena de las naranjas "))
c=float(input("Digite el dinero de la venta de naranjas "))
# Caja negra
Dec = (a/12)
x = b * Dec
ganancia = c - x
t = (ganancia / x)*100
# Salida
print(f"El porcentaje es de {t}%")