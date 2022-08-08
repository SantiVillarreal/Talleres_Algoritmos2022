

# Entradas
Base = float(input("Digite su sueldo base\n"))
V0 = float(input("Digite el valor de la venta 1\n"))
V1 = float(input("Digite el valor de la venta 2\n"))
V2 = float(input("Digite el valor de la venta 3\n"))

# Caja negra
Comisiones = (V0+V1+V2) * 0.1
Total = (Comisiones + Base)

# Salidas
print (f"El valor por comisines de ventas es {Comisiones} Y el total es {Total}")