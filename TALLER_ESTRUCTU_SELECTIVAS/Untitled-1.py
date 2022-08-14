
# Entradas
A = float(input("\nCuanto dinero tienes invertido en el banco? "))
B = float(input("Cuales son los intereses (%) de tu banco por inversión "))

# Caja negra 
B = B/100
C = A * B
E = C + A 

# Salidas 
print("\nEl dinero de su cuenta es",E,"\n")  if C > 100000 else print("\nEl dinero de su cuenta es",A,"\n")