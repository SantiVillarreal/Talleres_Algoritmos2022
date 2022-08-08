
# Entradas
eM = float(input("\n Digite la nota de su examen final de Matemáticas ")) 
M1 = float(input("\n Digite las notas de sus tres tareas de Matemáticas\n"))
M2 = float(input()) 
M3 = float(input())
eF = float(input("\n Digite la nota de su examen final de Física ")) 
F1 = float(input("\n Digite las notas de sus dos tareas de Física\n"))
F2 = float(input()) 
eQ = float(input("\n Digite la nota de su examen final de Química ")) 
Q1 = float(input("\n Digite las notas de sus tres tareas de Química\n"))
Q2 = float(input()) 
Q3 = float(input())

# Caja negra
Matematicas = (eM * 0.90) + ((M1+M2+M3)/3)*0.10
Física = (eF * 0.80) + ((F1+F2)/2)*0.20
Química = (eQ * 0.85) + ((Q1+Q2+Q3)/3)*0.15
Prom = (Matematicas + Física + Química)/3

# Salida	
print("\nEn Matematicas su nota es de: ",Matematicas,"\nen Física su nota es de: ",Física,"\n en Química su nota es de: ",Química,"\n Y su promedio general en",Prom)
	