from cmath import sqrt
import math
#entradas
a=float(input("ingrese lado a: "))#float
b=float(input("ingrese lado b: "))#float
c=float(input("ingrese lado c: "))#float
#caja negra
s=(a+b+c)/2#float
area=math.sqrt(s*(s-a)*(s-b)*(s-c))#float
#salidas
print("Promedio: "+str(area))