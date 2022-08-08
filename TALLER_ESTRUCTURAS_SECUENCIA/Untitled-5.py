
# Entradas
n0 = float(input("la nota del primer parcial\n"))
n1 = float(input("la nota del segundo parcial\n"))
n2 = float(input("la nota del tercer parcial\n"))
n3 = float(input("la nota del examen final\n"))
n4 = float(input("la nota del trabajo final\n"))

# Caja negra
a = float((n0+n1+n2)/3) * 0.55
b = float(n3 * 0.3)
c = float(n4 * 0.15)
d = a + b +c 

# Salidas
print("La nota final es",d)