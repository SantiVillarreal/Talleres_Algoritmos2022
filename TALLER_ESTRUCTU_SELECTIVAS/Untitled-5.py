
# Entradas
A = float(input("\nDigite la ventas del departamento 1 "))
B = float(input("Digite la ventas del departamento 2 "))
C = float(input("Digite la ventas del departamento 3 "))
D = float(input("Digite el sueldo de los vendedores "))

# Caja negra 
Total = (A + B + C)*.33

if A > Total:
    E = D + D*.20 
else:
    E = D
    
if B > Total:
    F = D + D*.20 
else:
    F = D
    
if C > Total:
    G = D + D*.20 
else:
    G = D
    
print(f"\nEl sueldo para el departamento 1: {E}\nEl sueldo para el departamento 2: {F}\nEl sueldo para el departamento 3: {G}\n")