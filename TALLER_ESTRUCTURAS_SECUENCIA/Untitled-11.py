
# Entradas
n = str(input("\n¿Digite es su nombre? "))
h = float(input("¿Cuantas horas normales ha trabajado? ")) 
p = float(input("¿Cuanto le pagan por hora normal? "))
e = float(input("¿Cuantas horas extras ha realizado? "))
hi = int(input("¿Cuantos hijos tiene? ")) 

# Caja negra
Base = h * p
e = e * (p + p * 0.25)
Sueldob = Base + e 
Dec = Sueldob * 0.14
f = 430000 + 173000 * hi
Sueldo = Sueldob - Dec + f 

# Salidas
print(f"\n{n} Por asignaciones usted tiene un total de {f}\n sus deducciones son un total de: {Dec}\ntu sueldo neto es de: {Sueldo}\n")