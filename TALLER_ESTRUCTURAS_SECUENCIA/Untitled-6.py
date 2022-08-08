
# Entradas
H = int(input("Digite la cantidad de hombres\n"))
M = int(input("Digite la cantidad de mujeres\n"))

# Caja negra
PH = (H*100)/(H+M)
PM = (M*100)/(H+M)
 
# Salida
print("El porcentaje de hombres es",PH,"%""El porcentaje de mujeres es",PM,"%\n")