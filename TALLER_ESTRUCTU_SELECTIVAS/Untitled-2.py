

# Entradas 
A =float(input("\nDigite tu salario actual "))

# Caja negra 
if A < 900000: 
    B = (A * 0.15) + A
else:
    B = (A * 0.12) + A
    
# Salidas 
print("Tu salario neto es de",B,"\n")