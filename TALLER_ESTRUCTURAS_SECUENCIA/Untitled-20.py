
# Entrada
Pc = float(input("\nDigite el valor del Computador pagando de contados\n"))
Cu = float(input("\nDigite el valor por cada cuota\n "))

# Caja negra
Cu = Cu*12
a = (((Cu*100)/Pc)-100)
b = (((Cu*100)/Pc)-100)/12
# Salida 
print(f"Por recargo el porcentaje es de {a}% y por cuota es de {b}%")